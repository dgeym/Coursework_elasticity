from typing import List
from models.materialpoint import MaterialPoint


class MaterialBody:
    """
    Класс материального тела
    """
    def __init__(self, b_id: int, mat_points: List[MaterialPoint] = None):
        """
        Конструктор класса материального тела. Инициализирует переменную класса.

        :param mat_points: массив принадлежащих ему материальных точек
        """
        self.mat_points = mat_points

    def add_new_point(self, new_point: MaterialPoint):
        """
        Функция, добавляющая в массив материальных точек данного тела новую материальную точку

        :param new_point: добавляемая точка
        """
        self.mat_points.append(new_point)
