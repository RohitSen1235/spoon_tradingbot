from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from openpyxl import load_workbook
import pygetwindow as gw
import pyautogui
import pyperclip
import os

def Copy_Crypto_Bublle():
    print("Função def Copy_Crypto_Bublle sendo chamada.")

    # Inicialize o driver do Chrome
    driver = webdriver.Chrome()
    # Encontre a janela do Chrome
    chrome_window = gw.getWindowsWithTitle('Crypto Bubble')

    # Verifique se a janela foi encontrada
    if chrome_window:
        # Restaure a janela se estiver minimizada
        if chrome_window[0].isMinimized:
            chrome_window[0].restore()

            # Maximize a janela (opcional)
            chrome_window[0].maximize()

            # Traz a janela para frente
            chrome_window[0].activate()

            # Aguarde um breve momento para a janela se ajustar
            time.sleep(3)

            # Agora você pode enviar comandos para o Chrome, como abrir uma nova guia e navegar para uma página da web
            # Esperando a página carregar completamente
            # Simular "Ctrl+A" para selecionar todo o texto na página
            pyautogui.hotkey('ctrl', 'a')

            # Aguardar um momento para que a seleção seja processada
            time.sleep(1)

            # Simular "Ctrl+C" para copiar o texto selecionado
            pyautogui.hotkey('ctrl', 'c')
    
            # Aguardar um momento para que a seleção seja processada
            time.sleep(1)
    
            # Minimize a janela
            chrome_window[0].minimize()
    
            # Substitua 'seu_arquivo.xlsx' pelo caminho do seu arquivo Excel
            caminho_arquivo1 = 'C:/Users/marco/Desktop/Trading Bot/Excel/REG1.xlsx'

            # Verifica se o arquivo existe
            if os.path.exists(caminho_arquivo1):
                # Abre o arquivo Excel com o programa padrão associado
                os.startfile(caminho_arquivo1)

                # Aguarda um momento para o Excel abrir
                time.sleep(5)

                # Define a célula que queremos selecionar
                celula = "A1"

                # Simula a tecla F5 para abrir a caixa de diálogo 'Ir para'
                pyautogui.press('f5')

                # Aguarda um momento para que a caixa de diálogo 'Ir para' apareça
                time.sleep(3)

                # Digita a referência da célula que queremos selecionar e pressiona Enter
                pyautogui.write(celula)
                pyautogui.press('enter')

                # Aguarda um momento para que a célula seja selecionada
                time.sleep(3)
            else:
                print(f'O arquivo {caminho_arquivo1} não foi encontrado.')
        
            # Aguardar um momento para que a seleção seja processada
            time.sleep(3)
    
            # Simular "Ctrl+C" para copiar o texto selecionado
            pyautogui.hotkey('ctrl', 'v')
    
            # Aguarda um momento para que o arquivo seja salvo
            time.sleep(3)
    
            # Simula as teclas Alt+F4 para fechar o Excel
            pyautogui.hotkey('alt', 'f4')
    
            # Aguarda um momento para que o arquivo seja salvo
            time.sleep(3)
    
            # Simular "Ctrl+C" para copiar o texto selecionado
            pyautogui.press('enter')
    
    else:
        print("Janela do Google Chrome não encontrada.")
        
    # Substitua 'seu_arquivo.xlsx' pelo caminho do seu arquivo Excel
    caminho_arquivo2 = 'C:/Users/marco/Desktop/Trading Bot/Excel/REG.xlsx'
    
    # Aguarda um momento para que o arquivo seja salvo
    time.sleep(10)
    
    # Verifica se o arquivo existe
    if os.path.exists(caminho_arquivo2):
        # Abre o arquivo Excel com o programa padrão associado
        os.startfile(caminho_arquivo2)

        # Aguarda um momento para o Excel abrir
        time.sleep(10)
        
        # Simula as teclas Alt+F4 para fechar o Excel
        pyautogui.hotkey('alt', 'f4')
    
        # Aguarda um momento para que o arquivo seja salvo
        time.sleep(3)
    
        # Simular "Ctrl+C" para copiar o texto selecionado
        pyautogui.press('enter')
        
    else:
        print(f'O arquivo {caminho_arquivo2} não foi encontrado.')
        
    # Substitua 'seu_arquivo.xlsx' pelo caminho do seu arquivo Excel
    caminho_arquivo3 = 'C:/Users/marco/Desktop/Trading Bot/Excel/Bot_Read.xlsx'
        
    # Aguarda um momento para que o arquivo seja salvo
    time.sleep(10)
    
        # Verifica se o arquivo existe
    if os.path.exists(caminho_arquivo3):
        # Abre o arquivo Excel com o programa padrão associado
        os.startfile(caminho_arquivo3)

        # Aguarda um momento para o Excel abrir
        time.sleep(10)
        
        # Simula as teclas Alt+F4 para fechar o Excel
        pyautogui.hotkey('alt', 'f4')
    
        # Aguarda um momento para que o arquivo seja salvo
        time.sleep(3)
    
        # Simular "Ctrl+C" para copiar o texto selecionado
        pyautogui.press('enter')
        
    else:
        print(f'O arquivo {caminho_arquivo3} não foi encontrado.')

# Agora, se você quiser chamar esse programa de outro lugar, basta chamar a função Copy_Crypto_Bublle()

