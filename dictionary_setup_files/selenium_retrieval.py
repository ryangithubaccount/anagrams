from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import os

DRIVER_PATH = '../../chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
website_name = 'https://scrabble.merriam.com/words/start-with/'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
sum = 0

for letter in alphabet:
    letter_dictionary = []
    driver.get(website_name + letter)
    #expands "closed" word lists
    list_buttons = driver.find_elements_by_xpath("//div[@class=\'sbl_word_group closed\']/div[@class=\'wres_t\']")
    for button in list_buttons:
        driver.execute_script("arguments[0].click();", button)

    for i in range(13):
    #no 2 letter words should need to expand (I think)
        try:
            element = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@class=\'sbl_load_all\'][@data-letterc=\'" + str(i + 3) +"\']")))
            driver.execute_script("arguments[0].click();", element)
        except:
            continue
    #wait for everything to load
    time.sleep(10)
    lists = driver.find_elements_by_xpath("//ul")
    for list in lists:
        letter_dictionary.append(list.text)
    print("writing to files: " + letter)

    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "../dictionaries/" + letter + ".txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    f = open(abs_file_path, 'w')
    for word in letter_dictionary:
        f.write(word + '\n')
    f.close()
driver.close()