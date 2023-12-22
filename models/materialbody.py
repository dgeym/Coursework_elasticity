from typing import List
from models.materialpoint import MaterialPoint


class MaterialBody:
    def __init__(self, b_id: int, mat_points: List[MaterialPoint] = None):
        self.b_id = b_id
        self.mat_points = mat_points

    def add_new_point(self, new_point: MaterialPoint):
        self.mat_points.append(new_point)