from serviceable import Serviceable


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
