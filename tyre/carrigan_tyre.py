from tyre.tyre import Tyre


class CarriganTyre(Tyre):
    def __init__(self, tyre_wear):
        self.tyre_wear = tyre_wear
        self.tyre_need_to_service = 0.9

    def needs_service(self):
        for tyre in self.tyre_wear:
            if tyre >= self.tyre_need_to_service:
                return True
        return False