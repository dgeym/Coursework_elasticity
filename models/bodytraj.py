from typing import List
from models.materialpoint import MaterialPoint


class PointTraj:
     """
    Класс траектории отдельной материальной точки
    """
    def __init__(self, p_tr_id=None, mat_point_tr: List[MaterialPoint] = None, time_grid: List[float] = None):
        """
        Конструктор класса траектории материальной точки. Инициализирует переменные класса.

        :param p_tr_id: id траектории
        :param mat_point_tr: позиции точек траектории
        :param time_grid: соответствующие этим позициям времена
        """

        self.p_tr_id = p_tr_id
        self.mat_point_tr = mat_point_tr
        self.time_grid = time_grid

    def add_new_position(self, new_position: MaterialPoint):
        """
        Функция добавления новой позиции точки

        :param new_position: новая позиция
        """
        self.mat_point_tr.append(new_position)

    def add_new_time(self, new_time):
        """
        Функция добавления времени, соответствующего новой позиции точки

        :param new_time: новое время
        """
        self.time_grid.append(new_time)


class BodyTraj:
    """
    Класс траектории материального тела.
    """
    def __init__(self, mat_points_tr: List[PointTraj] = None, time_grid: List[float] = None, radius=None, center_x=None, center_y=None):
        """
        Конструктор класса траектории материального тела. Инициализирует переменные класса.

        :param mat_points_tr: траектории материальных точек тела
        :param time_grid: соответствующие времена
        :param radius: радиус окружности материального тела
        :param center_x: координата центра по оси абсцисс
        :param center_y: координата центра по оси ординат
        """
        self.mat_points_tr = mat_points_tr
        self.time_grid = time_grid
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y

    def add_new_point_tr(self, new_point_tr: PointTraj):
        """
        Функция добавления новой траектории материальной точки

        :param new_point_tr: новая траектория
        """
        self.mat_points_tr.append(new_point_tr)

    def add_new_time(self, new_time: float):
        """
        Функция добавления нового времени к соответствующей траектории (то есть времени, соотвествующего набору всех материальных точек данного тела)

        :param new_time: новое время
        """
        self.time_grid.append(new_time)
