from models.bodytraj import BodyTraj
from models.materialpoint import MaterialPoint
from models.materialbody import MaterialBody
import numpy as np


def rot(x: float, y: float, r: float):
    """
    Функция перевода из полярных координат в декартовы
    (для удобства построения набора материальных точек,
    из которых состоит материальное тело)

    :param p: полярный радиус
    :param phi: полярный угол
    :return: rx - координата по x, ry - координата по y
    """
    rx = (x * np.cos(r)) - (y * np.sin(r))
    ry = (y * np.cos(r)) + (x * np.sin(r))
    return rx, ry


def create_circle(body: BodyTraj, knots_num: int):
    """
    Функция создания массива точек, принадлежащему материальному телу

    :param body: материальное тело
    :param knots_num: узловые точки для шага
    :return:
    """
    arc = (2 * np.pi) / knots_num
    mat_body = MaterialBody([]) 'Создание экземпляра класса MaterialBody'
    for p in range(knots_num):
        [x, y] = rot(0, body.radius, arc * p)
        x += body.center_x
        y += body.center_y
        new_point = MaterialPoint(p, x, y)
        mat_body.add_new_point(new_point)

    return mat_body
