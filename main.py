import numpy as np
import matplotlib.pyplot as plt
from water_tank import WaterTank

w = WaterTank(2, 2.0, 1.5, 5)
t0 = abs(int(input('Podaj punkt w czasie w którym chcesz sprawdzić stan wody w zbiorniku: ')))

interval = np.linspace(0, t0, num = 100 if t0 > 0 else 1, endpoint=True)

plt.plot(interval, [w.water_height(t) for t in interval])
plt.suptitle('Poziom wody w zbiorniku / czas')
plt.xlabel('czas [s]')
plt.ylabel('poziom wody w zbiorniku [m]')

plt.show()