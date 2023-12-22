class SpacePoint:
    def __init__(self, p_id: int, coord_x=None, coord_y=None, vel_x=None, vel_y=None, time=None):
        self.p_id = p_id
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.time = time