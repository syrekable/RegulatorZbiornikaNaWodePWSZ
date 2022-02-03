class WaterTank:
  '''
  A water tank model. Works under the invariant that qi and qo are constants.

  Args:
    * a: tank's cross section [m^2]
    * qi: inflow volume [m^3/s]
    * qo: outflow volume [m^3/s]
    * max_height: maximal height of water in the tank [m]
  '''
  a: float
  qi: float
  qo: float
  max_height: float

  def __init__(self, a, qi, qo, max_height, regulator: str = 'CLOSED'):
    self.a = a
    self.qi = qi
    self.qo = qo
    self.max_height = max_height
    self.v = self.qi-self.qo # according to lab notes, this holds true whenever 'qi' and 'qo' are constants

  def water_height(self, t: float) -> float:
    h = self._water_height(t)

    return h if h <= self.max_height else self.max_height 

  def _water_height(self, t: int) -> float:
    return (self.v*t) / self.a

  def regulator(self, t: float) -> str:
    h = self._water_height(t)

    if h == 0:
      return 'OPENED'
    elif h <= self.max_height:
      return 'OPEN'
    else:
      return 'CLOSED'