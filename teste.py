from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurar o ChromeDriver com o webdriver_manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Abrir o WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Aguarde até o usuário escanear o código QR e logar no WhatsApp
input("Escaneie o QR Code e pressione Enter para continuar...")

# Defina o nome do contato ou número (no formato internacional)
contato = "+55XXXXXXX"  # Substitua com o número do contato (ex: +55 11 91234-5678)
mensagem = "Mensagem de teste"

# Enviar a mensagem 10 vezes
for i in range(100):
    # Buscar o campo de pesquisa e localizar o contato
    pesquisa = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    pesquisa.click()
    pesquisa.send_keys(contato)  # Pesquisar pelo nome ou número do contato
    pesquisa.send_keys(Keys.ENTER)
    
    # Aguardar o carregamento da conversa
    time.sleep(2)
    
    # Localizar o campo de entrada de mensagem e enviar a mensagem
    caixa_mensagem = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]/p')
    caixa_mensagem.send_keys(mensagem)
    caixa_mensagem.send_keys(Keys.ENTER)  # Enviar a mensagem
    
    # Aguardar um tempo para evitar comportamento de spam

# Fechar o navegador após o envio
driver.quit()
