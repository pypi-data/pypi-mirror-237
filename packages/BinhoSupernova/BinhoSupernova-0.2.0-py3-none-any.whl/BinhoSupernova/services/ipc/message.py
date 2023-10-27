class Message:
    '''
    This class represents a message. A message is the abstraction of the data shared
    between processes.

    Attributes
    ----------
    origin: str
        Process who sends the message
    destination: str
        Process that receives the message
    ocpode: int
        A number that identifies the type of information contained in the payload.
    payload: list/ctype array
        Tha message contain. It can be a python list or cytpe array depending of the
        sender/receiver

    '''
    def __init__(self, origin: str, destination: str, opcode: int, payload):
        self.origin = origin
        self.destination = destination
        self.opcode = opcode
        self.payload = payload