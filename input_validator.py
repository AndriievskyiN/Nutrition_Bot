from typing import Any

class InputValidator:
    def __init__(self):
        pass

    @staticmethod
    def validate_type(value: Any, type: type) -> bool:
        """
        Checks if the type of a value is what it is supposed to be
        -------------------------
        Arguments:
            value (Any): value to be checked
            type (type): type to check for
        -------------------------
        Returns:
            bool: True if the value corresponds to the type, False otherwise
        """
        return isinstance(value, type)


    