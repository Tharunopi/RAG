from typing import Optional

class dynamicINT():
    """
    Keeps track of certain integer values
    """
    def __init__(self):
        self.value = 0

    def update(self, to_add:int) -> bool:
        """
        Adds an integer to values
        """
        try:
            self.value += to_add
            return True
        
        except Exception as e:
            print(f"update: {e}")
            return False
        
    def subtract(self, to_sub:int) -> bool:
        """
        Subtracts an integer from value
        """
        try:
            self.value += to_sub
            return True
        
        except Exception as e:
            print(f"subtract: {e}")
            return False
        
    def get_value(self) ->Optional[int]:
        """
        Returns the value
        """
        try:
            return self.value
        
        except Exception as e:
            print(f"get_value: {e}")
            return None