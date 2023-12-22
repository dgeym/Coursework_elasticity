from models.bodytraj import BodyTraj
from models.materialpoint import MaterialPoint
from models.materialbody import MaterialBody
import numpy as np


def rot(x: float, y: float, r: float):
    rx = (x * np.cos(r)) - (y * np.sin(r))
    ry = (y * np.cos(r)) + (x * np.sin(r))
    return rx, ry


def create_circle(body: BodyTraj, knots_num: int):
    arc = (2 * np.pi) / knots_num
    mat_body = MaterialBody(1, [])
    for p in range(knots_num):
        [x, y] = rot(0, body.radius, arc * p)
        x += body.center_x
        y += body.center_y
        new_point = MaterialPoint(p, x, y)
        mat_body.add_new_point(new_point)

    return mat_body
