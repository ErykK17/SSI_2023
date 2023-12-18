import numpy as np
from matplotlib import pyplot as plt


class AlgorytmHopfielda:
    def __init__(self, rozmiar):
        self.rozmiar = rozmiar
        self.siec = np.zeros((rozmiar, rozmiar))

    def zeronaminus1(self, obraz):
        przerobiony_obraz = [np.array(x).flatten() * 2 - 1 for x in obraz]
        return przerobiony_obraz

    def nauczObrazy(self, obrazy):
        for obraz in obrazy:
            przerobiony_obraz = self.zeronaminus1(obraz)
            self.siec += np.outer(przerobiony_obraz, przerobiony_obraz)

    def rozpoznajObraz(self, obraz, max_iter=10):
        naprawiony = obraz.copy()
        for _ in range(max_iter):
            for i in range(self.rozmiar):
                suma = np.sum(self.siec[i, :] * naprawiony)
                naprawiony[i] = 1 if suma >= 0 else -1

        return naprawiony


wzorzec_1 = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

wzorzec_2 = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1]
]

wzorzec_3 = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

test_1 = [
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0]
]

test_2 = [
    [0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1]
]

test_3 = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1]
]

wzorce = [wzorzec_1, wzorzec_2, wzorzec_3]
testy = [test_1, test_2, test_3]

plt.figure(figsize=(10, 5))
for i in range(len(wzorce)):
    plt.subplot(1, len(wzorce), i + 1)
    plt.imshow(wzorce[i], cmap='binary')
    plt.title(f'Wzorzec {i + 1}')

plt.figure(figsize=(10, 5))
for i in range(len(testy)):
    plt.subplot(1, len(testy), i + 1)
    plt.imshow(testy[i], cmap='binary')
    plt.title(f'Test {i + 1}')

plt.show()

wzorce = [np.array(wzorzec).flatten() * 2 - 1 for wzorzec in wzorce]
testy = [np.array(test).flatten() * 2 - 1 for test in testy]

siec = AlgorytmHopfielda(25)
siec.nauczObrazy(wzorce)

for i in range(len(testy)):
    plt.subplot(121)
    plt.imshow(testy[i].reshape((5, 5)), cmap='binary')
    plt.title(f"Zepsuty")
    plt.subplot(122)
    plt.imshow(siec.rozpoznajObraz(testy[i]).reshape((5, 5)), cmap='binary')
    plt.title(f"Naprawiony")
    plt.suptitle(f"Obraz {i + 1}")
    plt.show()
