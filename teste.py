
import pygetwindow as gw

janelas_abertas = gw.getAllTitles()
for titulo in janelas_abertas:
    print(titulo)