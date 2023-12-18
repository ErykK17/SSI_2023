import numpy as np
from matplotlib import pyplot as plt


class AlgorytmHopfielda:
    def __init__(self, rozmiar):
        self.rozmiar = rozmiar
        self.siec = np.zeros((rozmiar, rozmiar))

    def zeronaminus1(self, obraz):
        obraz_zamieniony = [np.array(x).flatten() * 2 - 1 for x in obraz]
        return obraz_zamieniony

    def nauczObrazy(self, obrazy):
        for obraz in obrazy:
            obraz_zamieniony = self.zeronaminus1(obraz)
            self.siec += np.outer(obraz_zamieniony, obraz_zamieniony)
            np.fill_diagonal(self.siec, 0)

    def rozpoznajObraz(self, obraz, max_iter=10):
        obraz_naprawiony = obraz.copy()
        for _ in range(max_iter):
            for i in range(self.rozmiar):
                suma = np.sum(self.siec[i, :] * obraz_naprawiony)
                obraz_naprawiony[i] = 1 if suma >= 0 else -1

        return obraz_naprawiony


# Przykładowe bitmapy wzorcowe i testowe

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

# Liczba wzorców
liczba_wzorcow = len(wzorce)
liczba_testow = len(testy)

# Utwórz subplot
plt.figure(figsize=(10, 5))
for i in range(liczba_wzorcow):
    plt.subplot(1, liczba_wzorcow, i + 1)
    plt.imshow(wzorce[i], cmap='binary', vmin=0, vmax=1)
    plt.title(f'Wzorzec {i + 1}')

plt.figure(figsize=(10, 5))
for i in range(liczba_testow):
    plt.subplot(1, liczba_testow, i + 1)
    plt.imshow(testy[i], cmap='binary', vmin=0, vmax=1)
    plt.title(f'Test {i + 1}')

plt.show()

wzorce = [np.array(wzorzec).flatten() * 2 - 1 for wzorzec in wzorce]
# wzorce = [np.where(np.array(x) == 0, -1, x).flatten() for x in wzorce]
# testy = [np.where(np.array(x) == 0, -1, x).flatten() for x in testy]

testy = [np.array(test).flatten() * 2 - 1 for test in testy]
print(testy)
siec = AlgorytmHopfielda(25)
siec.nauczObrazy(wzorce)

for i in range(len(testy)):
    plt.subplot(121)
    plt.imshow(testy[i].reshape((5, 5)), cmap='binary', vmin=-1, vmax=1)
    plt.title(f"Zepsuty")
    plt.subplot(122)
    plt.imshow(siec.rozpoznajObraz(testy[i]).reshape((5, 5)), cmap='binary', vmin=-1, vmax=1)
    plt.title(f"Naprawiony")
    plt.suptitle(f"Obraz {i + 1}")
    plt.show()
