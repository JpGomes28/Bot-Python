import pyautogui
import time

#Bot para abrir um site 

#Tempo entre uma função e outra
pyautogui.PAUSE = 2

#Abrir o navegador Opera
pyautogui.press('win')
pyautogui.write('Opera GX')
pyautogui.press('enter')

#Pesquisar o site
time.sleep(3)
pyautogui.write('https://www.linkedin.com/feed/')
pyautogui.press('enter')

#Finalizar escrevendo 'Obrigado por assistir' x556, y151

#Pegando as coordenadas do mouse
#while True:
#    print(pyautogui.position())

#Escrevendo a mensagem
time.sleep(3)
pyautogui.click(556,151)
pyautogui.write('Obrigado por assistir <3')
