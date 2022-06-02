from engine.willoughby import WilloughbyEngine
from battery.nubbin import NubbinBattery

class Rorschach(WilloughbyEngine, NubbinBattery):
    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False