from models.bodytraj import BodyTraj
from models.materialpoint import MaterialPoint
from models.materialbody import MaterialBody
import numpy as np


def rot(p: float, phi: float):
    rx = np.cos(phi) - p * np.sin(phi)
    ry = p * np.cos(phi) + np.sin(phi)
    return rx, ry


def create_circle(body: BodyTraj, knots_num: int):
    arc = (2 * np.pi) / knots_num
    mat_body = MaterialBody([])
    for p in range(knots_num):
        [x, y] = rot(body.radius, arc * p)
        x += body.center_x
        y += body.center_y
        new_point = MaterialPoint(p, x, y)
        mat_body.add_new_point(new_point)

    return mat_body
