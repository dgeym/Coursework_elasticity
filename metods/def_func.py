import numpy as np
"""
Определение дифференциальных уравнений, заданных в условии
"""

def f_x1(t, x1):
    return - np.exp(t) * x1

def f_x2(t, x2):
    return np.exp(t) * x2
