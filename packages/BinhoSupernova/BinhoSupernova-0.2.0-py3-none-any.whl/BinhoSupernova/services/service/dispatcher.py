from . import IpcMsgOpcode, DISPATCHER, USB_TRANSMITTER, LOGGER
from ..ipc.service import Service
from ...commands.definitions import *
from ...utils.system_message import SystemMessageOpcode

class Dispatcher(Service):
    '''
    This class represents the service responsible for receiving messages (commands/request)
    from the USB Host application, and sending them to the respective middleware services
    responsible for creating the corresponding USB commands.

    This process receives an IPC message from the USB HOST containing a dictionary with the
    descritption of the command, then looks for the service that handles the command and sends
    the information to that service.
    '''
    def __init__(self, activateLogger  = False):
        super().__init__(name="Dispatcher")
        self.onEventCallback = None
        self.responsesMap = {}
        self.run = False
        self.logEnable = activateLogger

    def activateLogger(self, activate: bool) -> None:
        """
        This method activates or deactivates log messages. If it is activated,
        then the __sendLogMessage method put the log messages into the process message queue.

        Parameters
        ----------
        activate : bool
            Boolean flag that indicates if the logger is activated or not. If it is activated,
            then the log messages received in the inputQueue must be append in the log file, else
            they are discarded.

        Returns
        -------
        None

        """
        # Enable/Disable log messages.
        self.logEnable = activate

    def __sendLogMessage(self, message: str):
        """
        This function receives an string and send a IPC message to the Logger service to save the
        log message into the log file.
        """
        if self.logEnable:
            self.sendMessage(origin=DISPATCHER, destination=LOGGER, opcode=IpcMsgOpcode.LOG, payload=message)

    def setOnEventCallback(self, callback) -> None:
        self.onEventCallback = callback

    def start(self):
        '''
        This function starts the Thread target function.
        '''
        self.run = True
        self.thread.start()

    def main(self, args, **kwargs):
        """
        This function is the Thread target function.
        """
        while self.run == True:

            # Receive new IPC message.
            ipcMsg = self.inputQueue.get()

            # Print logg message.
            self.__sendLogMessage(f'Message received from {ipcMsg.origin} opcode {ipcMsg.opcode}')

            # The message is a request from USB Host to USB device.
            if (ipcMsg.opcode == IpcMsgOpcode.REQUEST_FROM_HOST_TO_DEVICE):
                # Get request
                request = ipcMsg.payload
                # Match request and response
                self.responsesMap[request["id"]] = request["response"]
                # Get collection of transfers
                usbTransfers = request["requests"]

                for transfer in usbTransfers:
                    # Send request to USB host adapter.
                    self.sendMessage(origin=DISPATCHER, destination=USB_TRANSMITTER, opcode=IpcMsgOpcode.REQUEST_FROM_HOST_TO_DEVICE, payload=transfer.data)

            # The message is a response from USB device.
            elif (ipcMsg.opcode == IpcMsgOpcode.RESPONSE_FROM_DEVICE_TO_HOST):

                usbHostAdapterMessage = ipcMsg.payload

                # Get command id to search the response in the transfers map.
                id = (usbHostAdapterMessage[ID_LSB_INDEX] | usbHostAdapterMessage[ID_MSB_INDEX] << 8)

                # Look for the receiver of the message.
                command = usbHostAdapterMessage[COMMAND_CODE_INDEX]

                # Check if the message command exists in the diccionary command.
                if command in COMMANDS_DICTIONARY.keys():

                    # Check if the message from the USB Host Adapter corresponds to a request from the USB Host.
                    if COMMANDS_DICTIONARY[command]["type"] == CommandType.REQUEST_RESPONSE:

                        # Get response from response map with the id.
                        response = self.responsesMap.get(id)

                        if response != None:
                            isComplete = response.set(usbHostAdapterMessage)
                            if isComplete:
                                # Invoke callback
                                self.onEventCallback(response.toDictionary(), None)
                        else:
                            # TODO: Raise an Unexpected response exception or similar.
                            pass

                    # If the message is a notification
                    elif COMMANDS_DICTIONARY[command]["type"] == CommandType.NOTIFICATION:

                        # Identify what notification it is.
                        if command == I3C_IBI_NOTIFICATION:
                            ibiType = usbHostAdapterMessage[IBI_TYPE_INDEX]

                            if ibiType == I3cIbiType.IBI_NORMAL.value:
                                response = I3cIbiNotification_t.from_buffer_copy(usbHostAdapterMessage)
                            else:
                                response = I3cHotJoinIbiNotification_t.from_buffer_copy(usbHostAdapterMessage)

                            # Invoke callback
                            self.onEventCallback(response.toDictionary(), None)
                        else:
                            # TODO: Raise a "command not supported exception" or similar.
                            pass

                # If the command doesn't exist in the command dictionary.
                else:
                    # TODO: Raise a "command not supported exception" or similar.
                    pass

            # If an error happened
            elif (ipcMsg.opcode == IpcMsgOpcode.SYSTEM_MESSAGE):

                # Get the message.
                message = ipcMsg.payload

                if (message.opcode == SystemMessageOpcode.UNEXPECTED_DISCONNECTION):

                    # Print log message
                    self.__sendLogMessage('Supernova disconnected. Kill process.')

                    # Invoke callback to communicate the error to the USB host.
                    if self.onEventCallback is not None:
                        self.onEventCallback(None, message.toDictionary())

                    # Kill process
                    self.run = False

                elif (message.opcode == SystemMessageOpcode.CLOSE_CONNECTION_REQUEST):

                    self.__sendLogMessage('Close Supernova connection. Kill process.')

                    # Invoke callback to communicate the reception of the order.
                    if self.onEventCallback is not None:
                        self.onEventCallback(None, message.toDictionary())

                    # Kill process
                    self.run = False

        self.__sendLogMessage('Thread end.')