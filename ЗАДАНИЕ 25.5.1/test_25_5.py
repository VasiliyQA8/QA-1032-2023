from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Firefox(executable_path=r"/Users/User/skillfactory/geckodriver.exe")
    pytest.driver.implicitly_wait(10)
    pytest.driver.get('https://petfriends.skillfactory.ru/login')
    assert WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h1')))

    yield

    pytest.driver.quit()

def test_show_only_my_pets():
    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element(By.ID, 'email').send_keys('HVS8@yandex.ru')
    pytest.driver.find_element(By.ID, 'pass').send_keys('286143')

    WebDriverWait(pytest.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
    WebDriverWait(pytest.driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, 'Мои питомцы'))).click()
    pytest.driver.implicitly_wait(10)
    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == "Василий888"

    names = WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#all_my_pets>table>tbody>tr>td:nth-child(2)')))
    user_statistics = WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='.col-sm-4 left']")))
    stats = user_statistics[0].text.split()
    pets_num = int(stats[2])
    print(f'Количество карточек: {pets_num}')
    pytest.driver.implicitly_wait(10)
    assert pets_num == len(names)  # Если тест проходит, то "Присутствуют все питомцы"

    list_pets = []
    for i in range(len(names)):
        list_pets.append(names[i].text)
    print(list_pets)

    for i in range(len(list_pets)):
        for j in range(i + 1, len(list_pets)):
            assert list_pets[i] != list_pets[j]
    print("Все элементы уникальны")  # У всех питомцев разные имена.

    images = WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#all_my_pets>table>tbody>tr>th>img')))
    pet_photo = 0
    for p in range(len(images)):
        if images[p].get_attribute('src') != '':
            pet_photo += 1
    assert pets_num / 2 <= pet_photo  # Если тест проходит, то "Хотя бы у половины питомцев есть фото"

    age = WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#all_my_pets>table>tbody>tr>td:nth-child(4)')))
    breed = WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#all_my_pets>table>tbody>tr>td:nth-child(3)')))
    assert len(names) == len(age) == len(breed)  # Если тест проходит, то "У всех питомцев есть имя, возраст и порода."

    tabl1 = WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#all_my_pets>table>tbody:not(img and .smart_cell)')))
    table = tabl1[0].text.split()
    temp = []
    for i in table:
        if i != '×':
            temp.append(i)
    pets_5 = [temp[i:i + 3] for i in range(0, len(temp), 3)]
    print(pets_5)

    for i in range(len(pets_5)):
        for j in range(i + 1, len(pets_5)):
            assert pets_5[i] != pets_5[j]
    print("Все элементы уникальны")            # В списке нет повторяющихся питомцев.
