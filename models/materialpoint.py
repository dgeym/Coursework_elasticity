class MaterialPoint:
    def __init__(self, p_id: int, coord_x1=None, coord_x2=None, vel1=None, vel2=None, time=None):
        self.p_id = p_id
        self.coord_x1 = coord_x1
        self.coord_x2 = coord_x2
        self.vel1 = vel1
        self.vel2 = vel2
        self.time = time