from abc import abstractmethod
import queue
import threading

class Broker:
    """
    This class represents the broker. The broker is the bridge between the sender process and the
    receiver process. It receives each message to be sent from the sender, and it sends the message
    to the receiver.

    Attributes
    ----------
    processMessagesQueue: Queue
        This is the queue where all the message to be sent are put by the senders.
    processDictionary: dict
        Dictionary that contains all the instances of the processes that are part of the
        systems.
    thread: Thread
        Broker thread in which it receives the messages in its queue and send the message
        to the destination.

    """
    def __init__(self):
        # Queue used by all IPC members to send a message. All sent messages are put into this queue.
        self.processMessagesQueue = queue.Queue()

        # IPC members processDictionary
        self.processDictionary = {}

        #Broker thread
        self.thread = threading.Thread(target = self.main, name="Broker", daemon = True)

    def __keepAlive(self) -> bool:
        """
        This private method checks if the broker must keep its own thread alive. For that purpose,
        this method check if there is at least one instance of the process dictionary that
        keeps its thread alive. When all the thread are killed, then the broker
        ends its own thread.

        Returns
        -------
        bool
            Boolean flag indicating if the broker must keep its own thread alive or not.

        """
        return any(instance.thread.is_alive() for instance in self.processDictionary.values())

    def registerProcessMember(self, tag: str, instance):
        """
        This method allows to add the IPC members to the members dictionary. Each time a new
        member is created, it must be added to this dictionary invoking this function.

        Arguments
        ---------
        tag: str
            It is a string tag that represents the IPC member, and it is used as the dictionary
            key.
        instance
            It is the IPC process instance to be added to the dictionary and that now takes part of
            the IPC system.

        Returns
        -------
        None

        """
        # Set broker queue to IPC member. Each IPC member has no access to the broker queue when
        # it is created. Then the broker queue is set when the ipc member is added to the IPC system.
        # Every IPC member must be instance of a class that inherits from the Service class.
        instance.registerProcessMessagesQueue(self.processMessagesQueue)

        # Add IPC member to IPC dictionary
        self.processDictionary[tag] = instance

    def start(self):
        """
        This method starts all the IPC members threads.
        """
        # Start each IPC modules members
        for instance in self.processDictionary.values():
            instance.start()

        # Start own process
        self.thread.start()

    def main(self):
        """
        main function that represents the thread activity. It is the thread target function.
        """
        while self.__keepAlive() == True :
            
            # Avoid blocking the thread, so that check if the queue has pending messages.
            if not self.processMessagesQueue.empty():
            
                # Receive a new message.
                msg = self.processMessagesQueue.get()

                # Check message destination
                destination = self.processDictionary.get(msg.destination)

                if destination != None:

                    # Put the new message into the destination queue. The processDictionary contains the instances
                    # of the IPC members/processes. All processes inherit from Service class where the
                    # inputQueue is defined.
                    destination.inputQueue.put(msg)

                # It is a broadcast message.
                else:

                    for tag, instance in self.processDictionary.items():

                        # Send message to all the IPC members except the emitter.
                        if tag != msg.origin:
                            instance.inputQueue.put(msg)