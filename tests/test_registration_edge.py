import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import sys
import os

def clear_screen():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(seconds, message=""):
    
    for i in range(seconds, 0, -1):
        clear_screen()
        print("\n" + "="*50)
        print(f"\n{message}")
        print(f"\nAguardando {i} segundos...")
        print("\n" + "="*50)
        sys.stdout.flush()
        time.sleep(1)

class TestRegistrationEdge:
    @pytest.fixture
    def driver(self):
        clear_screen()
        print("\n" + "="*50)
        print("\nIniciando testes de registro...")
        print("\n" + "="*50)
        time.sleep(2)
        
       
        edge_options = Options()
        
        edge_options.add_argument('--start-maximized')
        
        
        driver = webdriver.Edge(options=edge_options)
        driver.get("http://localhost:5173")
        
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "nome"))
        )
        
        countdown(3, "Formulário carregado! Iniciando testes...")
        
        yield driver
        
        
        driver.quit()
        print("\n" + "="*50)
        print("\nTestes finalizados!")
        print("\n" + "="*50)

    def test_min_password_length(self, driver):
        
        clear_screen()
        print("\n" + "="*50)
        print("\nTestando tamanho mínimo da senha...")
        print("\n" + "="*50)
        time.sleep(2)
        
       
        driver.find_element(By.ID, "nome").send_keys("Teste Usuario")
        countdown(2, "Preenchendo nome...")
        
        
        driver.find_element(By.ID, "telefone").send_keys("(11) 91234-5678")
        countdown(2, "Preenchendo telefone...")
        
        
        driver.find_element(By.ID, "cpf").send_keys("123.456.789-09")
        countdown(2, "Preenchendo CPF...")
        
        
        driver.find_element(By.ID, "email").send_keys("teste@exemplo.com")
        countdown(2, "Preenchendo email...")
        
        
        driver.find_element(By.ID, "confirmarEmail").send_keys("teste@exemplo.com")
        countdown(2, "Preenchendo confirmação de email...")
        
       
        print("\nTestando senha válida (8 caracteres)...")
        driver.find_element(By.ID, "senha").send_keys("12345678")
        countdown(2, "Preenchendo senha válida...")
        
        driver.find_element(By.ID, "confirmarSenha").send_keys("12345678")
        countdown(2, "Preenchendo confirmação de senha válida...")
        
        
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        countdown(3, "Enviando formulário com senha válida...")
        
        
        error_messages = driver.find_elements(By.CLASS_NAME, "invalid-feedback")
        assert len(error_messages) == 0, "Não deveria haver mensagens de erro"
        
       
        driver.find_element(By.ID, "senha").clear()
        driver.find_element(By.ID, "confirmarSenha").clear()
        countdown(2, "Limpando campos de senha...")
        
        
        print("\nTestando senha inválida (7 caracteres)...")
        driver.find_element(By.ID, "senha").send_keys("1234567")
        countdown(2, "Preenchendo senha inválida...")
        
        driver.find_element(By.ID, "confirmarSenha").send_keys("1234567")
        countdown(2, "Preenchendo confirmação de senha inválida...")
        
        
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        countdown(3, "Enviando formulário com senha inválida...")
        
        
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-testid='senha-error']")
        assert "Senha deve ter no mínimo 8 caracteres" in error_message.text

    def test_phone_validation(self, driver):
        
        clear_screen()
        print("\n" + "="*50)
        print("\nTestando validação de telefone...")
        print("\n" + "="*50)
        time.sleep(2)
        
       
        driver.find_element(By.ID, "nome").send_keys("Teste Usuario")
        countdown(2, "Preenchendo nome...")
        
        driver.find_element(By.ID, "cpf").send_keys("123.456.789-09")
        countdown(2, "Preenchendo CPF...")
        
        driver.find_element(By.ID, "email").send_keys("teste@exemplo.com")
        countdown(2, "Preenchendo email...")
        
        driver.find_element(By.ID, "confirmarEmail").send_keys("teste@exemplo.com")
        countdown(2, "Preenchendo confirmação de email...")
        
        driver.find_element(By.ID, "senha").send_keys("12345678")
        countdown(2, "Preenchendo senha...")
        
        driver.find_element(By.ID, "confirmarSenha").send_keys("12345678")
        countdown(2, "Preenchendo confirmação de senha...")
        
        
        print("\nTestando telefone válido...")
        driver.find_element(By.ID, "telefone").send_keys("(11) 91234-5678")
        countdown(2, "Preenchendo telefone válido...")
        
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        countdown(3, "Enviando formulário com telefone válido...")
        
        
        error_messages = driver.find_elements(By.CLASS_NAME, "invalid-feedback")
        assert len(error_messages) == 0, "Não deveria haver mensagens de erro"
        
      
        driver.find_element(By.ID, "telefone").clear()
        countdown(2, "Limpando campo de telefone...")
        
       
        print("\nTestando telefone inválido...")
        driver.find_element(By.ID, "telefone").send_keys("(11) 1234-5678")
        countdown(2, "Preenchendo telefone inválido...")
        
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        countdown(3, "Enviando formulário com telefone inválido...")
        
        
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-testid='telefone-error']")
        assert "Formato inválido" in error_message.text

    def test_cpf_validation(self, driver):
       
        clear_screen()
        print("\n" + "="*50)
        print("\nTestando validação de CPF...")
        print("\n" + "="*50)
        time.sleep(2)
        
        
        driver.find_element(By.ID, "nome").send_keys("Teste Usuario")
        countdown(2, "Preenchendo nome...")
        
        driver.find_element(By.ID, "telefone").send_keys("(11) 91234-5678")
        countdown(2, "Preenchendo telefone...")
        
        driver.find_element(By.ID, "email").send_keys("teste@exemplo.com")
        countdown(2, "Preenchendo email...")
        
        driver.find_element(By.ID, "confirmarEmail").send_keys("teste@exemplo.com")
        countdown(2, "Preenchendo confirmação de email...")
        
        driver.find_element(By.ID, "senha").send_keys("12345678")
        countdown(2, "Preenchendo senha...")
        
        driver.find_element(By.ID, "confirmarSenha").send_keys("12345678")
        countdown(2, "Preenchendo confirmação de senha...")
        
       
        print("\nTestando CPF válido...")
        driver.find_element(By.ID, "cpf").send_keys("123.456.789-09")
        countdown(2, "Preenchendo CPF válido...")
        
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        countdown(3, "Enviando formulário com CPF válido...")
        
        
        error_messages = driver.find_elements(By.CLASS_NAME, "invalid-feedback")
        assert len(error_messages) == 0, "Não deveria haver mensagens de erro"
        
       
        driver.find_element(By.ID, "cpf").clear()
        countdown(2, "Limpando campo de CPF...")
        
        
        print("\nTestando CPF inválido...")
        driver.find_element(By.ID, "cpf").send_keys("123.456.789-00")
        countdown(2, "Preenchendo CPF inválido...")
        
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        countdown(3, "Enviando formulário com CPF inválido...")
        
        
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-testid='cpf-error']")
        assert "CPF inválido" in error_message.text

    def test_email_validation(self, driver):
        
        clear_screen()
        print("\n" + "="*50)
        print("\nTestando validação de email...")
        print("\n" + "="*50)
        time.sleep(2)
        
        
        driver.find_element(By.ID, "nome").send_keys("Teste Usuario")
        countdown(2, "Preenchendo nome...")
        
        driver.find_element(By.ID, "telefone").send_keys("(11) 91234-5678")
        countdown(2, "Preenchendo telefone...")
        
        driver.find_element(By.ID, "cpf").send_keys("123.456.789-09")
        countdown(2, "Preenchendo CPF...")
        
        driver.find_element(By.ID, "senha").send_keys("12345678")
        countdown(2, "Preenchendo senha...")
        
        driver.find_element(By.ID, "confirmarSenha").send_keys("12345678")
        countdown(2, "Preenchendo confirmação de senha...")
        
        
        print("\nTestando email válido...")
        driver.find_element(By.ID, "email").send_keys("teste@exemplo.com")
        countdown(2, "Preenchendo email válido...")
        
        driver.find_element(By.ID, "confirmarEmail").send_keys("teste@exemplo.com")
        countdown(2, "Preenchendo confirmação de email válido...")
        
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        countdown(3, "Enviando formulário com email válido...")
        
        
        error_messages = driver.find_elements(By.CLASS_NAME, "invalid-feedback")
        assert len(error_messages) == 0, "Não deveria haver mensagens de erro"
        
        
        driver.find_element(By.ID, "email").clear()
        driver.find_element(By.ID, "confirmarEmail").clear()
        countdown(2, "Limpando campos de email...")
        
        
        print("\nTestando email inválido...")
        driver.find_element(By.ID, "email").send_keys("teste@exemplo@com")
        countdown(2, "Preenchendo email inválido...")
        
        driver.find_element(By.ID, "confirmarEmail").send_keys("teste@exemplo@com")
        countdown(2, "Preenchendo confirmação de email inválido...")
        
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        countdown(3, "Enviando formulário com email inválido...")
        
       
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-testid='email-error']")
        assert "Email inválido" in error_message.text

    def test_email_password_match(self, driver):
       
        clear_screen()
        print("\n" + "="*50)
        print("\nTestando confirmação de email e senha...")
        print("\n" + "="*50)
        time.sleep(2)
        
        
        driver.find_element(By.ID, "nome").send_keys("Teste Usuario")
        countdown(2, "Preenchendo nome...")
        
        driver.find_element(By.ID, "telefone").send_keys("(11) 91234-5678")
        countdown(2, "Preenchendo telefone...")
        
        driver.find_element(By.ID, "cpf").send_keys("123.456.789-09")
        countdown(2, "Preenchendo CPF...")
        
        
        print("\nTestando email e senha coincidentes...")
        driver.find_element(By.ID, "email").send_keys("teste@exemplo.com")
        countdown(2, "Preenchendo email...")
        
        driver.find_element(By.ID, "confirmarEmail").send_keys("teste@exemplo.com")
        countdown(2, "Preenchendo confirmação de email...")
        
        driver.find_element(By.ID, "senha").send_keys("Senha123")
        countdown(2, "Preenchendo senha...")
        
        driver.find_element(By.ID, "confirmarSenha").send_keys("Senha123")
        countdown(2, "Preenchendo confirmação de senha...")
        
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        countdown(3, "Enviando formulário com dados coincidentes...")
        
       
        error_messages = driver.find_elements(By.CLASS_NAME, "invalid-feedback")
        assert len(error_messages) == 0, "Não deveria haver mensagens de erro"
        
        
        driver.find_element(By.ID, "senha").clear()
        driver.find_element(By.ID, "confirmarSenha").clear()
        countdown(2, "Limpando campos de senha...")
        
        
        print("\nTestando email e senha não coincidentes...")
        driver.find_element(By.ID, "senha").send_keys("Senha123")
        countdown(2, "Preenchendo senha...")
        
        driver.find_element(By.ID, "confirmarSenha").send_keys("Senha456")
        countdown(2, "Preenchendo confirmação de senha diferente...")
        
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        countdown(3, "Enviando formulário com senhas diferentes...")
        
       
        error_message = driver.find_element(By.CSS_SELECTOR, "[data-testid='confirmar-senha-error']")
        assert "Senhas não conferem" in error_message.text

    def test_successful_registration(self, driver):
        
        clear_screen()
        print("\n" + "="*50)
        print("\nTestando cadastro bem-sucedido...")
        print("\n" + "="*50)
        time.sleep(2)
        
        
        driver.find_element(By.ID, "nome").send_keys("Teste Usuario")
        countdown(2, "Preenchendo nome...")
        
        driver.find_element(By.ID, "telefone").send_keys("(75) 55544-4444")
        countdown(2, "Preenchendo telefone...")
        
        driver.find_element(By.ID, "cpf").send_keys("210.830.180-19")
        countdown(2, "Preenchendo CPF...")
        
        driver.find_element(By.ID, "email").send_keys("teste@teste.com.br")
        countdown(2, "Preenchendo email...")
        
        driver.find_element(By.ID, "confirmarEmail").send_keys("teste@teste.com.br")
        countdown(2, "Preenchendo confirmação de email...")
        
        driver.find_element(By.ID, "senha").send_keys("12345678")
        countdown(2, "Preenchendo senha...")
        
        driver.find_element(By.ID, "confirmarSenha").send_keys("12345678")
        countdown(2, "Preenchendo confirmação de senha...")
        
       
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        countdown(3, "Enviando formulário completo...")
        
        
        success_message = driver.find_element(By.CLASS_NAME, "alert-success")
        assert "Cadastro realizado com sucesso" in success_message.text 