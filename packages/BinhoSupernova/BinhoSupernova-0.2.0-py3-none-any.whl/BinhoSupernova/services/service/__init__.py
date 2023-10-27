__all__ = ["logger", "uartReceiver", "usbReceiver", "usbTransmitter"]

from enum import Enum
from ...commands.definitions import *

class IpcMsgOpcode(Enum):
    """
    This enum represents the different IPC messages types.

    REQUEST_FROM_HOST_TO_DEVICE         = 0 - Request that is sent from the USB Host to the USB device.
    RESPONSE_FROM_DEVICE_TO_HOST        = 1 - Response that is sent from the USB device to the USB Host as response to a previous request.
    NOTIFICATION_FROM_DEVICE_TO_HOST    = 2 - Notification sent by the USB device.
    SYSTEM_MESSAGE                      = 3 - System message sent between processes or sent by by the system to the USB Host.
    LOG                                 = 4 - Log messages.

    """
    REQUEST_FROM_HOST_TO_DEVICE         = 0                     
    RESPONSE_FROM_DEVICE_TO_HOST        = 1
    NOTIFICATION_FROM_DEVICE_TO_HOST    = 2
    SYSTEM_MESSAGE                      = 3                     
    LOG                                 = 4


"""
IPC Modules Tag

Add here the definition of the string tag used to identify each IPC module.
""" 
BROADCAST           = "BROADCAST"
DISPATCHER          = "DISPATCHER"
LOGGER              = "LOGGER"
USB_TRANSMITTER     = "USB_TRANSMITTER"
USB_RECEIVER        = "USB_RECEIVER"
UART_RECEIVER       = "UART_RECEIVER"
USB_HOST            = "USB_HOST"