import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5  # pausa entre cada comando

# PASSO 1: abrir navegador e acessar o site
pyautogui.press('win')
pyautogui.write('chrome')  # corrigido
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# PASSO 2: login
time.sleep(2)  # esperar site carregar
pyautogui.click(x=678, y=410)
pyautogui.write('kaianebts@gmail.com')
pyautogui.press('tab')
pyautogui.write('123456')
pyautogui.press('enter')

# PASSO 3: importar dados
time.sleep(2)
tabela = pandas.read_csv('produtos.csv')

# PASSO 4 e 5: preencher formulário
for linha in tabela.index:
    pyautogui.click(x=674, y=295)

    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(10000)
