import pyautogui
import pygetwindow as gw
import time
import keyboard

# Encontrar janelas com títulos específicos
# Obter uma lista de todas as janelas abertas
# janelas_abertas = gw.getAllTitles()

# # Exibir os títulos das abas abertas
# for titulo in janelas_abertas:
#     print(titulo)

def pos():
    x, y = pyautogui.position()


    # Move o mouse para uma nova posição
    new_x, new_y = 715, 406 # Coordenadas Note Paul
    # new_x, new_y = 827, 385 # Coordenadas PC Roberto

    pyautogui.moveTo(new_x, new_y, duration=1)
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.click(x=744,y=801) # clique note Paul
    # pyautogui.click(x=950,y=985) #Clique pc Roberto


def exc():
    time.sleep(10)
    pyautogui.click(x=744,y=801) # click PC Roberto
    # pyautogui.click(x=827,y=385) # click PC Roberto
    pyautogui.press('esc')

def f11():
    pyautogui.press('f11')
    time.sleep(5)
    pyautogui.press('f11')
    time.sleep(1)

def alternar_tela():
    # Obter uma lista de todas as janelas abertas
    janelas_abertas = gw.getAllTitles()
    janela1 = gw.getWindowsWithTitle('SIM Next')[0]
    janela2 = gw.getWindowsWithTitle('Google')[0]

    # Alternar entre as janelas
    while True:
        if keyboard.is_pressed('f'):
            break
        janela1.maximize()
        if keyboard.is_pressed('f'):
            break  # ativar a janela 1
        pos()
        if keyboard.is_pressed('f'):
            break
        exc()
        if keyboard.is_pressed('f'):
            break
        time.sleep(1)
        if keyboard.is_pressed('f'):
            break # aguardar 5 segundos
        janela1.minimize()
        if keyboard.is_pressed('f'):
            break
        # time.sleep(1)  # aguardar 5 segundos
        janela2.maximize()
        if keyboard.is_pressed('f'):
            break  # ativar a janela 2
        f11()
        if keyboard.is_pressed('f'):
            break
        janela2.minimize()
        if keyboard.is_pressed('f'):
            break

if __name__ == '__main__':
    alternar_tela()