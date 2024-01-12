class MaterialPoint:
    """
    Класс материальной точки
    """
    def __init__(self, p_id: int, coord_x1=None, coord_x2=None, vel1=None, vel2=None):
        """
        Конструктор класса материальной точки. Инициализирует переменные класса.

        :param p_id: id материальной точки
        :param coord_x1: первая координата
        :param coord_x2: вторая координата
        :param vel1: первая координата скорости
        :param vel2: вторая координата скорости
        """
        self.p_id = p_id
        self.coord_x1 = coord_x1
        self.coord_x2 = coord_x2
        self.vel1 = vel1
        self.vel2 = vel2
