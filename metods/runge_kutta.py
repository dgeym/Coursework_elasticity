import numpy as np
from metods.def_func import f_x1, f_x2
from models.bodytraj import PointTraj
from models.materialpoint import MaterialPoint


'n = 100'


t = 0
def runge_kutta(x_r, t, f):
    h = 0.01
    a = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0.5, 0, 0, 0],
        [0, 0, 0.5, 0, 0],
        [0, 0, 0, 1, 0],
    ])
    b = np.array([0, 1 / 6, 2 / 6, 2 / 6, 1 / 6])
    c = np.array([0, 0, 0.5, 0.5, 1])
    k1 = f(t, x_r)
    k2 = f(t + c[2] *h , x_r + a[2, 1] * h * k1)
    k3 = f(t + c[3] *h, x_r + a[3, 1] * h * k1 + a[3, 2] * h * k2)
    k4 = f(t + c[4] *h, x_r + a[4, 1] * h * k1 + a[4, 2] * h * k2 + a[4, 3] * h * k3)
    x_mass = (x_r + h * (k1 * b[1] + k2 * b[2] + k3 * b[3] + k4 * b[4]))
    return x_mass

def integr_rungekutta(mat_point: MaterialPoint, t: float, times_num: int):
    point_traj = PointTraj(mat_point.p_id, [], [])
    h = 0.01

    for i in range(100):
        point_traj.add_new_time(h*(i+1))

    point_traj.add_new_position(mat_point)
    x1 = point_traj.mat_point_tr[0].coord_x1
    y1 = point_traj.mat_point_tr[0].coord_x2
    for i in range(times_num-1):
        x2 = runge_kutta(x1, point_traj.time_grid[i], f_x1)
        y2 = runge_kutta(y1, point_traj.time_grid[i], f_x2)
        point_traj.mat_point_tr.append(MaterialPoint(mat_point.p_id, x2, y2))
        x1 = x2
        y1 = y2

    return point_traj