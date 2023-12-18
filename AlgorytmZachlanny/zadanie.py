import matplotlib.pyplot as plt
import numpy as np


def odleglosc_euklidesowa(x, y):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5


def czarne_punkty(bitmapa):
    for y, wiersz in enumerate(bitmapa):
        for x, piksel in enumerate(wiersz):
            if piksel == 1:
                yield x, y


def miara_niepodobienstwa(bitmapa1, bitmapa2):
    miara = 0

    for (pax, pay) in czarne_punkty(bitmapa1):
        odl_min = float('inf')

        for (pbx, pby) in czarne_punkty(bitmapa2):
            odl_akt = odleglosc_euklidesowa((pax, pay), (pbx, pby))
            odl_min = min(odl_min, odl_akt)

        miara += odl_min

    return miara


def miara_podobienstwa_obustronnego(bitmapa1, bitmapa2):
    return -(miara_niepodobienstwa(bitmapa1, bitmapa2) + miara_niepodobienstwa(bitmapa2, bitmapa1))


def znajdz_najbardziej_podobna(bitmapa_testowa, bitmapy_wzorcowe):
    najlepsza_miara = -float('inf')
    najlepsza_bitmapa = None

    for numer, wzorcowa in enumerate(bitmapy_wzorcowe):
        miara = miara_podobienstwa_obustronnego(bitmapa_testowa, wzorcowa)
        print(f"Miara Podobienstwa Testowa - Wzorcowa {numer + 1}: ", miara)

        if miara > najlepsza_miara:
            najlepsza_miara = miara
            najlepsza_bitmapa = numer + 1

    return najlepsza_bitmapa


def wizualizuj_bitmapy(bitmapy, tytul):
    fig, axs = plt.subplots(1, len(bitmapy), figsize=(5 * len(bitmapy), 5))

    for i, bitmapa in enumerate(bitmapy):
        axs[i].imshow(np.array(bitmapa), cmap='binary')
        axs[i].axis('off')
        axs[i].set_title(f'Bitmapa {i + 1}')

    plt.suptitle(tytul)
    plt.show()


bitmapy_wzorcowe = [
    [[1, 1, 0, 0], [0, 1, 1, 0], [1, 0, 1, 0], [0, 1, 0, 0], [1, 0, 1, 1]],
    [[0, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 0], [0, 1, 0, 1]],
    [[1, 1, 1, 1], [1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 1, 0], [1, 0, 1, 1]]
]

bitmapy_testowe = [
    [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1], [0, 0, 1, 1]],
    [[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [1, 0, 0, 1], [1, 1, 1, 0]],
    [[0, 0, 1, 1], [1, 1, 0, 0], [1, 0, 1, 1], [0, 0, 0, 1], [0, 0, 1, 0]]
]

wizualizuj_bitmapy(bitmapy_wzorcowe, 'Bitmapy wzorcowe')
wizualizuj_bitmapy(bitmapy_testowe, 'Bitmapy testowe')

for numer, testowa in enumerate(bitmapy_testowe):
    print(f"Testowa bitmapa {numer + 1}")
    najbardziej_podobna = znajdz_najbardziej_podobna(testowa, bitmapy_wzorcowe)
    print(f"Testowa bitmapa {numer + 1} jest najbardziej podobna do wzoru {najbardziej_podobna}")
