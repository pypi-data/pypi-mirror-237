from . import IpcMsgOpcode, USB_RECEIVER, DISPATCHER, LOGGER, BROADCAST
from ..ipc.service import Service
from ...utils.system_message import SystemMessage, SystemMessageOpcode

class UsbReceiver(Service):
    '''
    This class represents the process/service responsible for receiving USB HID
    INTERRUPT IN transfers, sent by the USB Host Adapter.
    When a new transfer is received, it is sent to the DISPATCHER who knows how
    to manage the message.

    Attributes
    ----------
    usbHostAdapter: hid usbHostAdapter
        This is the instance of the USB port.
    endpointSize: int
        Number that identifies the size of the IN ENDPOINT.
        usbHostAdapters based on MCU LPC5536 are USB Full Speed usbHostAdapters and the size is 64.
        usbHostAdapters based on MCU LPC55S16 are USB High Speed usbHostAdapters and the size is 1024.
    '''
    def __init__(self, usbHostAdapter, endpointSize, activateLogger = False):
        super().__init__(name="UsbReceiver")
        self.usbHostAdapter = usbHostAdapter
        self.endpointSize = endpointSize
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
            self.sendMessage(origin=USB_RECEIVER, destination=LOGGER, opcode=IpcMsgOpcode.LOG, payload=message)

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

            try:

                # Block for 100 ms to wait for a new message receive in the USB port from the Supernova.
                usbHostAdapterMessage = bytes(self.usbHostAdapter.read(self.endpointSize, 100))

                # If the Supernova sent a new message, process it.
                if usbHostAdapterMessage:

                    # Print log message
                    self.__sendLogMessage("New message from USB host adapter.")

                    # Send message received from the USB Host to the dispatcher.
                    self.sendMessage(origin=USB_RECEIVER, destination=DISPATCHER, opcode=IpcMsgOpcode.RESPONSE_FROM_DEVICE_TO_HOST, payload=usbHostAdapterMessage)

                # Check if an IPC messages arrived, without blocking.
                if self.inputQueue.empty() == False:

                    # Receive new IPC message.
                    ipcMsg = self.inputQueue.get()

                    # Print logg message
                    self.__sendLogMessage(f'Message received from {ipcMsg.origin} with opcode {ipcMsg.opcode}')

                    if (ipcMsg.opcode == IpcMsgOpcode.SYSTEM_MESSAGE):

                        # Get the error.
                        message = ipcMsg.payload

                        if (message.opcode == SystemMessageOpcode.CLOSE_CONNECTION_REQUEST):

                            self.__sendLogMessage('Close Supernova connection. Kill process.')

                            # Kill process
                            self.run = False


            except OSError:     # This exception is raised from self.usbHostAdapter.read when the Supernova is removed.

                # Create a custom error.
                error = SystemMessage(SystemMessageOpcode.UNEXPECTED_DISCONNECTION, f"Error {SystemMessageOpcode.UNEXPECTED_DISCONNECTION.name}: Unexpected Supernova disconnection.")

                # Notify to the broker.
                self.sendMessage(origin=USB_RECEIVER, destination=BROADCAST, opcode=IpcMsgOpcode.SYSTEM_MESSAGE, payload=error)

                # Kill process
                self.run = False

        self.__sendLogMessage('Thread end.')