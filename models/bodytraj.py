from typing import List
from models.materialpoint import MaterialPoint


class PointTraj:
    def __init__(self, p_tr_id=None, mat_point_tr: List[MaterialPoint] = None, time_grid: List[float] = None):
        self.p_tr_id = p_tr_id
        self.mat_point_tr = mat_point_tr
        self.time_grid = time_grid

    def add_new_position(self, new_position: MaterialPoint):
        self.mat_point_tr.append(new_position)

    def add_new_time(self, new_time):
        self.time_grid.append(new_time)


class BodyTraj:
    def __init__(self, mat_points_tr: List[PointTraj] = None, time_grid: List[float] = None, radius=None, center_x=None, center_y=None):
        self.mat_points_tr = mat_points_tr
        self.time_grid = time_grid
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y

    def add_new_point_tr(self, new_point_tr: PointTraj):
        self.mat_points_tr.append(new_point_tr)

    def add_new_time(self, new_time: float):
        self.time_grid.append(new_time)
