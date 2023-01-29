from typing import Any, Union

class InputValidator:
    @staticmethod
    def __is_valid_type(value: Any, type: type) -> bool:
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

    @staticmethod
    def is_valid_number(value: str, command: str): # edit
        if value.startswith("pass") and command == "/editmeal":
            return True

        elif value.startswith("pass") and command == "/addmeal":
            return False

        try:
            float(value)
            return True

        except ValueError:
            return False
