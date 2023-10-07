def load_samples_with_text(plik_z_wartosciami, plik_z_atr):
    data = []
    czy_atr_symb = []
    nazwa_atr = []
    with open(plik_z_wartosciami) as file:
        for line in file:
            data.append(line.strip('\n').split('\t'))

    with open(plik_z_atr) as file:
        for lines in file:
            line = lines.split()
            nazwa_atr.append(line[0])
            if line[1] == 'r':
                czy_atr_symb.append(True)
            else:
                czy_atr_symb.append(False)
    return data, czy_atr_symb, nazwa_atr

if __name__ == "__main__":
    data, czy_atr_symb, nazwa_atr = load_samples_with_text("iris.txt", "iris_type.txt")
    print(data[100][3])
    print(czy_atr_symb[2])
    print(nazwa_atr[2])
