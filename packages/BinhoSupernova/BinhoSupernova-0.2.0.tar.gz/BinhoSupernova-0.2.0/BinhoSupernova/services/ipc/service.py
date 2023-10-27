from abc import abstractmethod
import queue
import threading

from .message import Message

class Service:
    '''
    This class represents the micro-services that are part of the whole system. It is the base class, then different
    classes that represent different processes must inherit from this class.

    Attributes
    ----------
    processMessagesQueue: Queue
        This is the broker queue. The services must use this queue to send messages. This attributes
        is assigned None when a new instance is created, and the correct broker queue is assigned
        when the instance is registered by the system.
    inputQueue: Queue
        This is the queue used to receive messages.
    thread: Thread
        Service main process thread.
    '''

    def __init__(self, name, **kwargs):
        # Queue where the broker will put the messages.
        self.inputQueue = queue.Queue()
        # Queue used to send message to another services. This queue is shared by all the services.
        self.processMessagesQueue = None
        # Service thread.
        self.thread = threading.Thread(target = self.main, name=name, args = [self.inputQueue], kwargs = kwargs, daemon=True)

    def registerProcessMessagesQueue(self, queue):
        '''
        Public method used to set the processMessagesQueue with an external queue shared by all the servies
        that are part of the whole system.
        '''
        self.processMessagesQueue = queue

    def sendMessage(self, origin, destination, opcode, payload):
        '''
        This method is used to send a new message. The method creates a message and put it into the
        processMussagesQue.
        '''
        message = Message(origin, destination, opcode, payload)
        self.processMessagesQueue.put(message)

    @abstractmethod
    def start(self):
        '''
        Method to be overridden, will contain the logic of the module to start the target thread.
        '''
        pass

    @abstractmethod
    def main(self, args, **kwargs):
        '''
        Method to be overridden, will contain the logic of the module and be used as target for the thread
        '''
        pass