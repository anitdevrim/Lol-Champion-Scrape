import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()

champion_input = input("Enter the champion you want to fetch:\n")
champion_input.lower()


url = f"https://mobalytics.gg/lol/champions/{champion_input}/build"

options = webdriver.ChromeOptions()
driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=options)
driver.get(url)

def scrape_data():
    # Winrate
    winrate = driver.find_element(By.XPATH, os.getenv("WINRATE"))  # web element
    # Current Patch
    patch = driver.find_element(By.XPATH, os.getenv("PATCH"))  # web element
    # Name of the Main Rune
    main_rune_name = driver.find_element(By.XPATH, os.getenv("MAIN_RUNE_NAME"))  # web element
    # Name of the Secondary Rune
    secondary_rune_name = driver.find_element(By.XPATH, os.getenv("SECONDARY_RUNE_NAME"))  # web element

    # First Rune Page
    key_runes = driver.find_elements(By.XPATH, os.getenv("KEY_RUNE"))
    for rune in key_runes:
        key_rune = rune.find_element(By.CLASS_NAME, 'm-1iebrlh')  # key_rune is web element

    first_runes = driver.find_elements(By.XPATH, os.getenv("FIRST_RUNE"))
    for rune in first_runes:
        first_rune = rune.find_elements(By.CLASS_NAME, 'm-1nx2cdb')  # first_rune is a web element list

    # Secondary Rune Page
    secondary_runes = driver.find_elements(By.XPATH, os.getenv("SECONDARY_RUNE"))
    for rune in secondary_runes:
        secondary_rune = rune.find_elements(By.CLASS_NAME, 'm-1nx2cdb')  # secondary_rune is a web element list

    # Additional Choices
    additional_choices = driver.find_elements(By.XPATH, os.getenv("ADDITIONALS"))
    for element in additional_choices:
        choices = element.find_elements(By.CLASS_NAME, 'm-1dj96r2')
    
    # Items
    item_list = []  # Item names are stored inside
    for i in range(7):
        if(i == 0):
            continue
        else:
            xpath = f'//*[@id="container"]/div/main/div[3]/div[2]/div/div[3]/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div/div[{i}]/div/img'
            item = driver.find_element(By.XPATH, xpath)
            item_list.append(item.accessible_name)

    # Ability Orders
    ability_divs = driver.find_elements(By.XPATH, os.getenv("ABILITIES"))
    for i in ability_divs:
        abilities = i.find_elements(By.CLASS_NAME, 'm-af8mp8')
    
    # Output
    print("Current Patch:", patch.text)
    print("Win Rate:", winrate.text)
    print("\n\n--- RUNES ---")
    print("#",main_rune_name.text.upper(),"#")
    print(key_rune.accessible_name)
    for i in first_rune:
        print(i.accessible_name)
    print("#",secondary_rune_name.text.upper(),"#")
    for i in secondary_rune:
        print(i.accessible_name)
    for i in choices:
        print(i.text)
    print("\n\n--- BUILD ---")
    for i in item_list:
        print(i)
    print("\n\n--- ABILITY ORDER ---")
    for i,j in enumerate(abilities, start = 1):
        print(i, j.text)

scrape_data()
