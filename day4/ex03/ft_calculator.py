

class calculator:
    """calculator class"""
    def __init__(self, inst):
        self.inst = inst
    def __add__(self, object) -> None:
        """overloading add operator"""
        for i in range(len(self.inst)):
            self.inst[i] += object
        print(self.inst)
        return self.inst
        
        
    def __mul__(self, object) -> None:
        """overloading add operator"""
        for i in range(len(self.inst)):
            self.inst[i] *= object
        print(self.inst)
        return self.inst
        
    def __sub__(self, object) -> None:
        """overloading add operator"""
        for i in range(len(self.inst)):
            self.inst[i] -= object
        print(self.inst)
        return self.inst
        
    def __truediv__(self, object) -> None:
        """overloading add operator"""
        if object != 0:
            for i in range(len(self.inst)):
                self.inst[i] /= object
            print(self.inst)
            return self.inst