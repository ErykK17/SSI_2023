import matplotlib.pyplot as plt


def generuj_styl(index):
    series_index = index % 10
    colors = ('blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'purple', 'orange', 'pink')
    styles = ('-', '--', ':', '-.')
    marker_styles = ('.', ',', 'o', 'v', '^', '<', '>', '+', 'x', '*')
    style = {
        'color': colors[series_index],
        'linestyle': styles[series_index % 4],
        'marker': marker_styles[series_index]
    }
    return style


def wykres_linie_rysuj(wartosci_x, wartosci_y, index):
    style_index = index % 10
    styl = generuj_styl(style_index)
    plt.plot(wartosci_x, wartosci_y, **styl)


def wykres_linie_kropki_rysuj(wartosci_x, wartosci_y, index):
    style_index = index % 10
    styl = generuj_styl(style_index)
    plt.scatter(wartosci_x, wartosci_y, **styl)


if __name__ == "__main__":
    fig = plt.figure()
    wykres_linie_rysuj([1, 3], [5, 8], 0)
    wykres_linie_rysuj([0, 8], [0, 6], 1)
    wykres_linie_kropki_rysuj([0, 2, 4], [2, 4, 6], 2)
    wykres_linie_kropki_rysuj([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], 7)
    plt.show()


