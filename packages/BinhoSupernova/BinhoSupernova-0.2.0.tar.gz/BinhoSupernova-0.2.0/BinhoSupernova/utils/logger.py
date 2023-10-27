import datetime
from pathlib import Path, WindowsPath, PosixPath

# =================== Logs path ====================== #

# Enable/Disable logger
# True  -> Enable
# False -> Disable
LOGGER_ENABLED       = True

# String format for log file name and log message timestamp.
FILE_NAME_FORMAT     = "Binho-Log-{year}-{month:02d}-{day:02d}-{hour:02d}.log"
LOG_TIMESTAMP_FORMAT = "[{hour:02d}:{minute:02d}:{second:02d}:{millis:07.03f}] "

# Create an empty log directory path. This global variable is initialized in the
# initLogPath function.
LOG_PATH = Path()

# =================== Logger API ====================== #

def initLogPath() -> None:
    """
    This function initializes the global LOG_PATH variable with a default
    log directory that it is under the HOME directory of each Operating System:

    Windows: ~/AppData/Roaming/BinhoSupernova
    MacOS: ~/Library/Logs/BinhoSupernova
    Linux: ~/.config/BinhoSupernova

    This function must be called before neither print nor printFormat functions.
    """

    # Get HOME directory.
    global LOG_PATH
    LOG_PATH = Path.home()

    # Check if the OS is Windows
    if isinstance(LOG_PATH, WindowsPath):
        LOG_PATH = LOG_PATH / "AppData" / "Roaming" / "BinhoSupernova"

    # Else check if it is MacOS or Linux.
    elif isinstance(LOG_PATH, PosixPath):
        # Check if it is MacOS 
        if Path.exists(LOG_PATH / "Library" / "Logs"):
            LOG_PATH = LOG_PATH / "Library" / "Logs" / "BinhoSupernova"
        
        # Else it is Linux.
        else:
            LOG_PATH = LOG_PATH / ".config" / "BinhoSupernova"
    
    # Check if the directory exists, otherwise create it.
    if not Path.exists(LOG_PATH):
        Path.mkdir(LOG_PATH)

def getLogFileName() -> str:
    """
    This function creates the file name using the FILE_NAME_FORMAT constant
    and the current date and time.

    Returns
    -------
    str
        The log file name string.
    """
    timestamp = datetime.datetime.today()
    fileName = FILE_NAME_FORMAT.format(year=timestamp.year,
                                        month=timestamp.month, 
                                        day = timestamp.day,
                                        hour = timestamp.hour )
    return fileName

def getLogTimestamp() -> str:
    """
    This function creates the log timestamp, using the LOG_TIMESTAMP_FORMAT constant
    and the current date and time.

    Returns
    -------
    str
        A timestamp string.
    """
    currentDateTime = datetime.datetime.today()
    timestamp = LOG_TIMESTAMP_FORMAT.format(hour = currentDateTime.hour,
                                            minute = currentDateTime.minute,
                                            second = currentDateTime.second,
                                            millis = currentDateTime.microsecond / 1000)
    return timestamp

def printFormat(strFormat: str, *args) -> None:
    """
    This function must be call from application code to format and print messages in the 
    log file. This function open the log file, write the message and close
    the file. If log file does not exist, then it is created.
    
    Parameters
    ----------
    strFormat : str
        This parameters is a string formater used to format a string using the String.format method.
    *arg:
        Variable lenght arguments list used to repalce the palceholderes in strFormat.

    Returns
    -------
    None

    """

    # Just if logger is enabled.
    if LOGGER_ENABLED:

        # Get file name.
        logFile = LOG_PATH / Path(getLogFileName())
        
        # Format string message.
        message = getLogTimestamp()
        message = message + strFormat.format(*args)
        message = message + "\r"

        # Write log message
        with open(logFile,'a') as file:
            file.write(message)
            file.close()

def print(logMessage: str) -> None:
    """
    This function must be call from application code to print messages in the 
    log file. This function open the log file, write the message and close
    the file. If log file does not exist, then it is created.

    Parameters
    ----------
    logMessage : str
        The log message string to be append in the log file.

    Returns
    -------
    None
    
    """

    # Just if logger is enabled.
    if LOGGER_ENABLED:

        # Get file name.
        logFile = LOG_PATH / Path(getLogFileName())
        
        # Format string message.
        message = getLogTimestamp()
        message = message + logMessage
        message = message + "\r"

        # Write log message
        with open(logFile,'a') as file:
            file.write(message)
            file.close()