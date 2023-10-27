from . import IpcMsgOpcode, UART_RECEIVER, LOGGER
from ..ipc.service import Service
from ...utils.system_message import SystemMessageOpcode

class UartReceiver(Service):
    '''
    This class represents the process/service responsible for receiving messages
    sent by the USB device over the UART, using the pyserial library.
    Until now, each message received is sent to the LOGGER to print the message in
    the log file.
    '''
    def __init__(self, serialPort, activateLogger = False):
        super().__init__(name="UartReceiver")
        self.serialPort = serialPort
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
            self.sendMessage(origin=UART_RECEIVER, destination=LOGGER, opcode=IpcMsgOpcode.LOG, payload=message)

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

            # Check if arrived some data from the Serial Port
            if self.serialPort.in_waiting > 0:

                # Read and decode string.
                msg = self.serialPort.readline().removesuffix(b'\r\n').decode()

                # Send message to the logger to print in logger file.
                self.sendMessage(UART_RECEIVER, LOGGER, IpcMsgOpcode.LOG, msg)

            # Check if a IPC messages arrevied, without blocking.
            if self.inputQueue.empty() == False:

                # Received new IPC message.
                ipcMsg = self.inputQueue.get()

                # Print log message
                self.__sendLogMessage(f'Message received from {ipcMsg.origin} with opcode {ipcMsg.opcode}')

                # Check if it is an error, if so kill the process.
                if (ipcMsg.opcode == IpcMsgOpcode.SYSTEM_MESSAGE):

                    # Get the error.
                    message = ipcMsg.payload

                    if (message.opcode == SystemMessageOpcode.UNEXPECTED_DISCONNECTION):

                        self.__sendLogMessage(f'Supernova disconnected. Kill process.')

                        # Kill process
                        self.run = False

                    elif (message.opcode == SystemMessageOpcode.CLOSE_CONNECTION_REQUEST):

                        self.__sendLogMessage(f'Close Supernova connection. Kill process.')

                        # Kill process
                        self.run = False

        self.__sendLogMessage(f'Thread end.')