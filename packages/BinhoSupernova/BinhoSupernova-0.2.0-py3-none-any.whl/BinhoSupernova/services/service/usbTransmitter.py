from . import IpcMsgOpcode, USB_TRANSMITTER, LOGGER
from ..ipc.service import Service
from ...utils.system_message import SystemMessageOpcode

class UsbTransmitter(Service):
    '''
    This class represents the process/service responsible for sending USB HID
    OUT INTERRUPT transfers, sent by the USB Host, using the hid library as the driver.
    The data to be sent to the USB Host Adapter is the payload of the IPC message received
    in the process queue.

    Attributes
    ----------
    usbHostAdapter: hid usbHostAdapter
        This is the instance of the USB port.
    endpointId: int
        Output endpoint id.
    '''
    def __init__(self, usbHostAdapter, inEndpointId, activateLogger = False):
        super().__init__(name="UsbTransmitter")
        self.usbHostAdapter = usbHostAdapter
        self.inEndpointId = inEndpointId                        # TODO: In a near future, this thread shoud add the endpoint id at the beginning of the bytes stream to be sent to the USB Host Adapter, not in the command serializer.
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
            self.sendMessage(origin=USB_TRANSMITTER, destination=LOGGER, opcode=IpcMsgOpcode.LOG, payload=message)

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

            # Recieved new IPC message.
            ipcMsg = self.inputQueue.get()

            # Print logg message
            self.__sendLogMessage(f'Message received from {ipcMsg.origin} with opcode {ipcMsg.opcode}')

            if (ipcMsg.opcode == IpcMsgOpcode.REQUEST_FROM_HOST_TO_DEVICE):

                # Send ipc message payload over an OUTPUT INTERRUPT TRANSFER.
                self.usbHostAdapter.write(bytes(ipcMsg.payload))

            # Check if it is an error, if so kill the process.
            elif (ipcMsg.opcode == IpcMsgOpcode.SYSTEM_MESSAGE):

                # Get the error.
                message = ipcMsg.payload

                if (message.opcode == SystemMessageOpcode.UNEXPECTED_DISCONNECTION):

                    self.__sendLogMessage('Supernova disconnected. Kill process.')

                    # Kill process
                    self.run = False

                elif (message.opcode == SystemMessageOpcode.CLOSE_CONNECTION_REQUEST):

                    self.__sendLogMessage('Close Supernova connection. Kill process.')

                    # Kill process
                    self.run = False

        self.__sendLogMessage('Thread end.')
