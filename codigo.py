import pyautogui
#pip install pyautogui
import time 
import pandas
#pip install pandas numpy openpyxl

  

pyautogui.PAUSE = 2
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email= "a@b.com"
senha="123456"

#Abre o navegador
pyautogui.press("win")
pyautogui.write("brave") # altere para seu navegador de preferencia
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
pyautogui.click(x=1535, y=31) #usar o auxiliar.py pra captar a posição (click maximizar tela do navegador)
time.sleep(3)
pyautogui.press("tab")
pyautogui.write(email)
pyautogui.press("tab")
pyautogui.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)


tabela= pandas.read_csv("produtos.csv")

pyautogui.press("tab")

for linha in tabela.index:
    
    pyautogui.write(tabela.loc[linha,"codigo"])

    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha,"marca"])

    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha,"tipo"])

    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"categoria"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))

    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))

    pyautogui.press("tab")
    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs )

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(1000)
    pyautogui.click(x=818, y=240) #Use o auxiliar.py para modificações em coordenadas (click campo código com scroll total em cima)









