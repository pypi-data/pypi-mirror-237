from . import IpcMsgOpcode
from ..ipc.service import Service
from ...utils import logger
from ...utils.system_message import SystemMessageOpcode
import time

class Logger(Service):
    """
    This class represents the process responsible for printing log messages in the log file,
    using the logger utility. This process receives an IPC message from the system that
    contains a log message in its payload.

    Attributes
    ----------
    active : bool
        Boolean flag that indicates if the logger is activated or not. If it is activated,
        then the log messages received in the inputQueue must be append in the log file, else
        they are discarded.

    run : bool
        Boolean flag used to control the own thread life.

    Methods
    -------
    enable(activate: bool)
        This method activates or deactivates the logger. It can be used to activate or deactivate
        the logger after it was created.

    start()
        This method starts the Thread target function.

    join()
        This method waits until the Thread target function terminates.

    main(self, args, **kwargs)
        This method is the Thread target function.

    """
    def __init__(self, activate: bool =True):
        super().__init__(name="Logger")
        self.active=activate
        self.run = False
        logger.initLogPath()

    def activate(self, activate: bool) -> None:
        """
        This method activates or deactivates the logger. It can be used to activate or deactivate
        the logger after it was created.

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
        # Enable/Disable logger.
        self.active = activate

    def start(self) -> None:
        """
        This method starts the Thread target function.
        """
        self.run = True
        self.thread.start()

    def main(self, args, **kwargs):
        """
        This method is the Thread target function.
        """
        while ( self.run == True or ( self.run == False and ( not self.inputQueue.empty() ) ) ):

            # Receive new IPC message
            ipcMsg = self.inputQueue.get()

            if (self.active and ipcMsg.opcode == IpcMsgOpcode.LOG):
                # Create log message indicating the origin and the content.
                # Create a String object from the payload to make possible to write it in the file.
                logMsg = '[' + ipcMsg.origin + '] -> ' + str(ipcMsg.payload)
                logger.print(logMsg)

            elif (ipcMsg.opcode == IpcMsgOpcode.SYSTEM_MESSAGE):

                # Get the message.
                message = ipcMsg.payload

                if (message.opcode == SystemMessageOpcode.UNEXPECTED_DISCONNECTION):

                    if self.active:
                        logger.print("[LOGGER] -> Supernova disconnected. Wait until printing the last log message and Kill process.")

                    # Let the broker to put the last messages in the logger queue.
                    time.sleep(0.1)

                    # Kill process
                    self.run = False

                elif (message.opcode == SystemMessageOpcode.CLOSE_CONNECTION_REQUEST):

                    if self.active:
                        logger.print("[LOGGER] -> Close Supernova connection. Wait until printing the last log message and Kill process.")

                    # Let the broker to put the last messages in the logger queue.
                    time.sleep(0.1)

                    # Kill process
                    self.run = False

        if self.active:
            logger.print("[LOGGER] -> Thread end.")