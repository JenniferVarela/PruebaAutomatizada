# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()


driver.get("http://localhost:4200")  

def test_empty_fields():
    driver.find_element(By.ID, "registrar").click() 
    time.sleep(1)
    error_nombre = driver.find_element(By.CSS_SELECTOR, "small.error").text
    assert "El nombre es obligatorio." in error_nombre

def test_email_invalid():
    driver.find_element(By.ID, "nombre").send_keys("Usuario Test")
    driver.find_element(By.ID, "email").send_keys("correo.invalido")
    driver.find_element(By.ID, "contrasenia").send_keys("ContraseñaSegura123")
    driver.find_element(By.ID, "confirmarContrasenia").send_keys("ContraseñaSegura123")
    driver.find_element(By.ID, "registrar").click()
    time.sleep(1)
    error_email = driver.find_element(By.CSS_SELECTOR, "small.error").text
    assert "Ingrese un correo válido." in error_email

def test_password_mismatch():
    driver.find_element(By.ID, "nombre").clear()
    driver.find_element(By.ID, "nombre").send_keys("Usuario Test")
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "email").send_keys("usuario@test.com")
    driver.find_element(By.ID, "contrasenia").clear()
    driver.find_element(By.ID, "contrasenia").send_keys("ContraseñaSegura123")
    driver.find_element(By.ID, "confirmarContrasenia").clear()
    driver.find_element(By.ID, "confirmarContrasenia").send_keys("ContraseñaIncorrecta")
    driver.find_element(By.ID, "registrar").click()
    time.sleep(1)
    error_mismatch = driver.find_element(By.CSS_SELECTOR, "small.error").text
    assert "Las contraseñas no coinciden." in error_mismatch

def test_valid_submission():
    driver.find_element(By.ID, "nombre").clear()
    driver.find_element(By.ID, "nombre").send_keys("Usuario Test")
    driver.find_element(By.ID, "email").clear()
    driver.find_element(By.ID, "email").send_keys("usuario@test.com")
    driver.find_element(By.ID, "contrasenia").clear()
    driver.find_element(By.ID, "contrasenia").send_keys("ContraseñaSegura123")
    driver.find_element(By.ID, "confirmarContrasenia").clear()
    driver.find_element(By.ID, "confirmarContrasenia").send_keys("ContraseñaSegura123")
    driver.find_element(By.ID, "registrar").click()
    time.sleep(1)

    # Verificar que se haya enviado el formulario (ajusta según tu HTML)
    success_message = driver.find_element(By.TAG_NAME, "h1").text  # Ajusta según tu HTML
    assert "Validar" in success_message

if __name__ == "__main__":
    test_empty_fields()
    test_email_invalid()
    test_password_mismatch()
    test_valid_submission()
    driver.quit()
