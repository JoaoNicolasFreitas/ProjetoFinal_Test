import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:5173")
    yield driver
    driver.quit()

class TestRegistration:
    def test_min_password_length(self, driver):
       
        driver.find_element(By.CSS_SELECTOR, '[data-testid="senha-input"]').send_keys("12345678")
        driver.find_element(By.CSS_SELECTOR, '[data-testid="confirmar-senha-input"]').send_keys("12345678")
        assert not driver.find_elements(By.CSS_SELECTOR, '[data-testid="senha-error"]')

        
        driver.find_element(By.CSS_SELECTOR, '[data-testid="senha-input"]').clear()
        driver.find_element(By.CSS_SELECTOR, '[data-testid="senha-input"]').send_keys("1234567")
        error = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="senha-error"]'))
        )
        assert "Senha deve ter no mínimo 8 caracteres" in error.text

    def test_phone_validation(self, driver):
        
        driver.find_element(By.CSS_SELECTOR, '[data-testid="telefone-input"]').send_keys("(11) 91234-5678")
        assert not driver.find_elements(By.CSS_SELECTOR, '[data-testid="telefone-error"]')

        
        driver.find_element(By.CSS_SELECTOR, '[data-testid="telefone-input"]').clear()
        driver.find_element(By.CSS_SELECTOR, '[data-testid="telefone-input"]').send_keys("(11) 1234-5678")
        error = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="telefone-error"]'))
        )
        assert "Formato inválido" in error.text

    def test_cpf_validation(self, driver):
       
        driver.find_element(By.CSS_SELECTOR, '[data-testid="cpf-input"]').send_keys("123.456.789-09")
        assert not driver.find_elements(By.CSS_SELECTOR, '[data-testid="cpf-error"]')

       
        driver.find_element(By.CSS_SELECTOR, '[data-testid="cpf-input"]').clear()
        driver.find_element(By.CSS_SELECTOR, '[data-testid="cpf-input"]').send_keys("123.456.789-00")
        error = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="cpf-error"]'))
        )
        assert "CPF inválido" in error.text

    def test_email_validation(self, driver):
        
        driver.find_element(By.CSS_SELECTOR, '[data-testid="email-input"]').send_keys("teste@teste.com")
        driver.find_element(By.CSS_SELECTOR, '[data-testid="confirmar-email-input"]').send_keys("teste@teste.com")
        assert not driver.find_elements(By.CSS_SELECTOR, '[data-testid="email-error"]')

       
        driver.find_element(By.CSS_SELECTOR, '[data-testid="email-input"]').clear()
        driver.find_element(By.CSS_SELECTOR, '[data-testid="email-input"]').send_keys("teste@")
        error = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="email-error"]'))
        )
        assert "Email inválido" in error.text

    def test_email_password_match(self, driver):
       
        driver.find_element(By.CSS_SELECTOR, '[data-testid="senha-input"]').send_keys("12345678")
        driver.find_element(By.CSS_SELECTOR, '[data-testid="confirmar-senha-input"]').send_keys("12345678")
        assert not driver.find_elements(By.CSS_SELECTOR, '[data-testid="confirmar-senha-error"]')

       
        driver.find_element(By.CSS_SELECTOR, '[data-testid="confirmar-senha-input"]').clear()
        driver.find_element(By.CSS_SELECTOR, '[data-testid="confirmar-senha-input"]').send_keys("87654321")
        error = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="confirmar-senha-error"]'))
        )
        assert "Senhas não conferem" in error.text

    def test_successful_registration(self, driver):
        
        driver.find_element(By.CSS_SELECTOR, '[data-testid="nome-input"]').send_keys("João Silva")
        driver.find_element(By.CSS_SELECTOR, '[data-testid="telefone-input"]').send_keys("(11) 91234-5678")
        driver.find_element(By.CSS_SELECTOR, '[data-testid="cpf-input"]').send_keys("123.456.789-09")
        driver.find_element(By.CSS_SELECTOR, '[data-testid="email-input"]').send_keys("teste@teste.com")
        driver.find_element(By.CSS_SELECTOR, '[data-testid="confirmar-email-input"]').send_keys("teste@teste.com")
        driver.find_element(By.CSS_SELECTOR, '[data-testid="senha-input"]').send_keys("12345678")
        driver.find_element(By.CSS_SELECTOR, '[data-testid="confirmar-senha-input"]').send_keys("12345678")

       
        driver.find_element(By.CSS_SELECTOR, '[data-testid="submit-button"]').click()

        
        success = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.alert-success'))
        )
        assert "Cadastro realizado com sucesso!" in success.text 