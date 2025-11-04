class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

class BaseRobot:
    def __init__(self, name: str, weight: int, coords=None):
        if coords is None:
            coords = [0, 0]
        self.name = name
        self.weight = weight
        self.coords = coords


    def go_forward(self, step: int = 1):
        self.coords = [self.coords[0], self.coords[1] + step]


    def go_right(self, step: int = 1):
        self.coords = [self.coords[0] + step, self.coords[1]]


    def go_back(self, step: int = 1):
        self.coords = [self.coords[0], self.coords[1] - step]


    def go_left(self, step: int = 1):
        self.coords = [self.coords[0] - step, self.coords[1]]

    def get_info(self):
        return f"Robot: {self.name}, Weight: {self.weight}"

class FlyingRobot(BaseRobot):
    def __init__(self, name: str, weight: int, coords=None):
        if coords is None:
            coords = [0, 0, 0]
        super().__init__(name, weight, coords)


    def go_up(self, step: int):
        self.coords = [self.coords[0], self.coords[1], self.coords[2] + step]


    def go_down(self, step: int):
        self.coords = [self.coords[0], self.coords[1], self.coords[2] - step]

class DeliveryDrone(FlyingRobot):
    def __init__(self, name: str, weight: int, coords, max_load_weight: int, current_load: Cargo):
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load


robot = BaseRobot(name="Walle", weight=34, coords=[3, -2])
robot.go_forward()
print(robot.coords) # == [3, -1]
robot.go_right(5)
print(robot.coords) # == [8, -1])

flying_robot = FlyingRobot(name="Mike", weight=11)
flying_robot.go_up(10)
flying_robot.go_down(5)
print("flying_robot.coords=", flying_robot.coords) # = [0, 0, 10]

ppp = DeliveryDrone("Df", 45, [0,0,0,], 3)

print(ppp.coords)



