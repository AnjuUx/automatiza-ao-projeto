import pyautogui as py
import time
import pandas as pd



py.PAUSE = 0.9 # a cada comodando do pyautogui  esperar esse tempo 

#entrando no navegador 

py.press ("win")
py.write ("chrome")
py.press ("enter")
time.sleep (1)
py.click (x=726, y=521) #usuario do google
time.sleep (3)

#entrando no site
py.click (x=318, y=60)
py.hotkey ("ctrl", "a")
py.write ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
py.press ("enter")

#login
time.sleep (2)
py.click (x=596, y=390)
py.hotkey ("ctrl", "a")
py.write ("juan.15.braga@gmail.com")

#senha
time.sleep(1)
py.click(x=619, y=479)
py.hotkey ("ctrl","a")
py.write ("JuanAnju")

#confirmar 
py.click (x=786, y=533)


produtos = pd.read_csv ("produtos.csv")


for linha in produtos.index:

    #codigo 
    py.click (x=677, y=259)
    codigo = str(produtos.loc[linha, "codigo"])
    py.write(codigo)
    
    #marca 
    marca = str (produtos.loc[linha, "marca"])
    py.press("tab")
    py.write(marca) 

    #tipo
    tipo = str (produtos.loc[linha, "tipo"])
    py.press ("tab")
    py.write(tipo)

    #categoria
    categoria= str (produtos.loc [linha, "categoria"])
    py.press("tab")
    py.write(categoria)

    #preço unitario 
    preco_unitario = str (produtos.loc[linha, "preco_unitario"])
    py.press("tab")
    py.write(preco_unitario)

    #custo
    custo = str (produtos.loc[linha, "custo"])
    py.press("tab")
    py.write(custo)

    #obs
    obs = str (produtos.loc[linha, "obs"])
    if obs != "nan":
        py.write(obs)
    py.press ("tab")
    py.write(obs)
    py.press("tab")
    py.press("enter")
    py.scroll (5000)





