from tyre.tyre import Tyre


class OctoprimeTyre(Tyre):
    def __init__(self, tyre_wear):
        self.tyre_wear = tyre_wear
        self.tyre_need_to_service = 3.0

    def needs_service(self):
        return sum(self.tyre_wear) >= self.tyre_need_to_service