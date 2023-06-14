# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
sbis_site = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/'
sbis_title = 'Вход в личный кабинет'

try:
    driver.get(sbis_site)
    print('Проверить адрес сайта и заголовок страницы')
    assert driver.current_url == sbis_site, 'Неверный адрес сайта'
    assert driver.title == sbis_title, 'Неверный заголовок сайта'

    print('Авторизоваться')
    sleep(1)
    user_login, user_password = 'bigshak', 'bigshak123'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)

    print('Проверить адрес сайта и заголовок страницы')
    sleep(2)
    assert 'fix-online.sbis.ru' in driver.current_url
    assert driver.title == 'СБИС'

    print('Проверить отображение аккордеона')
    accordion = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-Accordion__container')
    assert accordion.is_displayed(), 'Аккордеон не отображается'

    print('Проверить текст, атрибут и видимость кнопки "Контакты"')
    contacts_txt = 'Контакты'
    contacts = driver.find_element(By.CSS_SELECTOR,
                                   '[data-qa="Контакты"] [data-qa="NavigationPanels-Accordion__title"]')
    assert contacts.text == contacts_txt
    assert contacts.get_attribute("innerText") == contacts_txt

    print('Перейти в реестр "Контакты"')
    contact = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    sleep(5)
    contact.click()
finally:
    driver.quit()
