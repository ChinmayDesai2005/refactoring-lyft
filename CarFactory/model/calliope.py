from engine.capulet import CapuletEngine
from battery.spindler import SpindlerBattery

class Calliope(CapuletEngine, SpindlerBattery):
    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False