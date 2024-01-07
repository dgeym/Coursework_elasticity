from typing import List
from models.spacepoint import SpacePoint


class Space:
    def __init__(self, b_id: int, sp_points: List[SpacePoint] = None):
        #Инициализация переменных экземпляра класса: id материального тела и
                                     #массива из принадлежащих ему материальных
                                     #точек. Через каждый элемент массива могут быть вызваны переменные,
                                     #связанные с соотвествующим экземпляром класса SpacePoint
        self.b_id = b_id
        self.sp_points = sp_points

    def add_new_point(self, new_point: SpacePoint):
        self.sp_points.append(new_point)
