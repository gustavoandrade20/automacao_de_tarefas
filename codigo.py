import pyautogui
from time import sleep

pyautogui.PAUSE = 1 


pyautogui.press('win')
pyautogui.write('Chrome')
pyautogui.press('enter')

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press('enter')
sleep(3)

pyautogui.click(x=523, y=407)

pyautogui.write("pythonimpressionador@gmail.com")

pyautogui.click(x=572, y=501)

pyautogui.write("Sua senha")

pyautogui.click(x=689, y=563)
sleep(3)

import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:
    pyautogui.click(x=471, y=291)

    codigo = tabela.loc[linha, "codigo"]

    pyautogui.write(str(codigo))

    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]

    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

