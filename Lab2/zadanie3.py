import matplotlib.pyplot as plt
import numpy as np
from zadanie2 import wykres_linie_kropki_rysuj, wykres_linie_rysuj

fig = plt.figure()
plt.grid(True)
axes = plt.gca()
axes.set_aspect(1)
wykres_linie_rysuj([0, 0.8], [2, 1.9], 0)
wykres_linie_rysuj([-0.8, 0], [1.9, 2], 0)
wykres_linie_rysuj([-1.4, -0.8], [1.4, 1.9], 0)
wykres_linie_rysuj([0.8, 1.4], [1.9, 1.4], 0)
wykres_linie_rysuj([-1.9, -1.4], [0.8, 1.4], 0)
wykres_linie_rysuj([1.4, 1.9], [1.4, 0.8], 0)
wykres_linie_rysuj([-2, -1.9], [0, 0.8], 0)
wykres_linie_rysuj([1.9, 2], [0.8, 0], 0)

wykres_linie_rysuj([-2, -1.9], [0, -0.8], 0)
wykres_linie_rysuj([1.9, 2], [-0.8, 0], 0)
wykres_linie_rysuj([-1.9, -1.4], [-0.8, -1.4], 0)
wykres_linie_rysuj([1.4, 1.9], [-1.4, -0.8], 0)
wykres_linie_rysuj([-1.4, -0.8], [-1.4, -1.9], 0)
wykres_linie_rysuj([0.8, 1.4], [-1.9, -1.4], 0)
wykres_linie_rysuj([0, 0.8], [-2, -1.9], 0)
wykres_linie_rysuj([-0.8, 0], [-1.9, -2], 0)

wykres_linie_kropki_rysuj([-1, 0, 1], [1, 0, 1], 2)

x = np.linspace(-1, 1, 1000)
y = np.cos(x) * -1
wykres_linie_rysuj(x, y, 4)

fig.show()
