# external package imports.
from abc import abstractmethod

# our package imports.
from .bstutils import export

@export
class SoundTouchModelRequest:
    """
    A class representing a model that can issue a POST request with an
    xml payload that gets placed in the request body.
    """
    
    def __init__(self) -> None:
        """
        Initializes a new instance of the class.
        """
        # nothing to do here - subclasses just need to implement methods.
        pass


    @abstractmethod
    def ToXmlRequestBody(self, encoding:str='utf-8') -> str:
        """ 
        Returns a POST request body for updating a configuration.
        
        Returns:
            An xml string that can be used in a POST request to update a
            device configuration.
        """
        raise NotImplementedError("The '%s' class has not overridden the RequestBody() method." % (self.__name__))
