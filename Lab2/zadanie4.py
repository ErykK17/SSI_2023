import matplotlib.pyplot as plt
from Lab1.zadanie1 import load_samples_with_text
from zadanie2 import wykres_linie_kropki_rysuj,wykres_linie_kropki_rysuj

dane, czy_atr_symb, nazwa_atr = load_samples_with_text("iris.txt", "iris_type.txt")

klasa1 = []
klasa2 = []
klasa3 = []


for i in dane:
    if int(i[4]) == 1:
        klasa1.append(i[:4])
    elif int(i[4]) == 2:
        klasa2.append(i[:4])
    elif int(i[4]) == 3:
        klasa3.append(i[:4])

fig = plt.figure()
plt.subplot(2,2,1)
wykres_linie_kropki_rysuj([sublist[2] for sublist in klasa1],[sublist[3] for sublist in klasa1],0)
wykres_linie_kropki_rysuj([sublist[2] for sublist in klasa2],[sublist[3] for sublist in klasa2],4)
wykres_linie_kropki_rysuj([sublist[2] for sublist in klasa3],[sublist[3] for sublist in klasa3],8)
plt.subplot(2,2,2)
wykres_linie_kropki_rysuj([sublist[1] for sublist in klasa1],[sublist[3] for sublist in klasa1],0)
wykres_linie_kropki_rysuj([sublist[1] for sublist in klasa2],[sublist[3] for sublist in klasa2],4)
wykres_linie_kropki_rysuj([sublist[1] for sublist in klasa3],[sublist[3] for sublist in klasa3],8)
plt.subplot(2,2,3)
wykres_linie_kropki_rysuj([sublist[0] for sublist in klasa1],[sublist[3] for sublist in klasa1],0)
wykres_linie_kropki_rysuj([sublist[0] for sublist in klasa2],[sublist[3] for sublist in klasa2],4)
wykres_linie_kropki_rysuj([sublist[0] for sublist in klasa3],[sublist[3] for sublist in klasa3],8)
plt.subplot(2,2,4)
wykres_linie_kropki_rysuj([sublist[1] for sublist in klasa1],[sublist[2] for sublist in klasa1],0)
wykres_linie_kropki_rysuj([sublist[1] for sublist in klasa2],[sublist[2] for sublist in klasa2],4)
wykres_linie_kropki_rysuj([sublist[1] for sublist in klasa3],[sublist[2] for sublist in klasa3],8)

fig.show()

