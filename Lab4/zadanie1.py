import matplotlib.pyplot as plt
import numpy as np

rozrzut = 10
l_iteracji = 100
wsp_przyrostu = 1.1


def funkcja_przystosowania(x):
    return np.sin(x / 10) * np.sin(x / 200)


x = np.random.uniform(0, 100)
y = funkcja_przystosowania(x)
obecny_rozrzut = rozrzut
x_result = []
y_result = []
print(f'Iteracja 0, x = {x}, y = {y}, rozrzut = {obecny_rozrzut}')
for i in range(1, l_iteracji+1):
    xpot = x + np.random.uniform(-obecny_rozrzut, obecny_rozrzut)
    if xpot < 0:
        xpot = 0
    elif xpot > 100:
        xpot = 100
    ypot = funkcja_przystosowania(xpot)
    if ypot >= y:
        x = xpot
        y = ypot
        obecny_rozrzut *= wsp_przyrostu
    else:
        obecny_rozrzut /= wsp_przyrostu
    x_result.append(x)
    y_result.append(y)
    print(f'Iteracja {i}, x = {x}, y = {y}, rozrzut = {obecny_rozrzut}')


x_values = np.linspace(0, 100, 1000)
y_values = funkcja_przystosowania(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label="Funkcja przystosowania")
plt.scatter(x_result, y_result, c='red', s=20, label="Wyniki algorytmu")
plt.xlabel('x')
plt.ylabel('F(x)')
plt.legend()
plt.title('Algorytm 1+1')
plt.show()
