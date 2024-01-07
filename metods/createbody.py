from models.bodytraj import BodyTraj
from models.materialpoint import MaterialPoint
from models.materialbody import MaterialBody
import numpy as np


def polar(p: float, phi: float):
    """
    Функция перевода из полярных координат в декартовы
    (для удобства поточечного просчета материального тела)

    :param p: полярный радиус
    :param phi: полярный угол
    :return: rx - координата по x, ry - координата по y
    """
    rx = p * np.cos(phi)
    ry = p * np.sin(phi)
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
        [x, y] = polar(body.radius, arc * p)
        x += body.center_x
        y += body.center_y
        new_point = MaterialPoint(p, x, y) 'Каждая итерация массива создает новый экземпляр,'
        mat_body.add_new_point(new_point) 'который добавляется в массив класса - mat_points'

    return mat_body
