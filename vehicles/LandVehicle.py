from.Vehicle import Vehicle

class LandVehicle(Vehicle):
  def __init__(self):
    self.sound = "ooga ooga"

  def blowHorn(self):
    print(self.sound)