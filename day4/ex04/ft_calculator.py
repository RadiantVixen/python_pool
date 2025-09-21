
from typing import List

class calculator:
    """calculator class"""
        
    @staticmethod
    def dotproduct(V1, V2) -> None:
        # decorator
        V3 = []
        for i in range(len(V1)):
            V3.append( V1[i] * V2[i])
        print(sum(V3))
    
    @staticmethod
    def add_vec(V1, V2) -> None:
        # decorator
        # decorator
        V3 = []
        for i in range(len(V1)):
            V3.append( V1[i] + V2[i])
        print(V3)
    
    @staticmethod
    def sous_vec(V1, V2) -> None:
        # decorator
        V3 = []
        for i in range(len(V1)):
            V3.append( V1[i] - V2[i])
        print(V3)

