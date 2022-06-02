from engine.capulet import CapuletEngine
from battery.nubbin import NubbinBattery

class Thovex(CapuletEngine, NubbinBattery):
    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False