from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import random
import string


def build_driver():
    # Set up the driver
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def check_exists_by_xpath(driver, xpath):
    try:
        x = driver.find_element(By.XPATH, xpath)
        if x.is_displayed():
            return 1
    except NoSuchElementException:
        return 0


def welcome_page(driver):
    # Give input to the entry question - find the element by its id
    entry_question_id = 'id_entry_question'
    entry_question_input = 'Testing Input for Entry Question'
    driver.find_element(By.ID, entry_question_id).send_keys(entry_question_input)

    # eligible
    eligible = driver.find_elements(By.NAME, 'eligible_question')
    rand_selection = random.randint(0, len(eligible) - 1)
    eligible[rand_selection].click()

    # next button
    driver.find_element(By.XPATH, '//*[@id ="form"]/div/button').click()
    return rand_selection


def demo_page(driver):
    xpath = "//*[@id='id_entry_question']"
    age = random.randint(1, 30)
    driver.find_element(By.XPATH, xpath).send_keys(str(age))

    # gender field
    gender = driver.find_elements(By.NAME, 'gender')
    rand_selection = random.randint(0, len(gender) - 1)
    gender[rand_selection].click()

    # next
    driver.find_element(By.XPATH, '//*[@id ="form"]/div/button').click()


def only_one_group(driver):
    # Find the element by its tag
    driver.find_element(By.TAG_NAME, 'button').click()


def cat_pets(driver):
    # two radio buttons
    yes = '//*[@id="petYes"]'
    no = '//*[@id="petNo"]'
    select = random.randint(0, 1)
    input_text = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(1, 10)))
    if select == 0:
        driver.find_element(By.XPATH, yes).click()
        # how did you find out
        driver.find_element(By.XPATH, '//*[@id="divYes"]/input').send_keys(input_text)
    else:
        driver.find_element(By.XPATH, no).click()
        # do you not read the news
        driver.find_element(By.XPATH, '//*[@id="divNo"]/input').send_keys(input_text)
    # next button
    driver.find_element(By.XPATH, '//*[@id = "form"]/div/button').click()


def end_of_survey(driver):
    # submit button
    driver.find_element(By.XPATH, '//*[@id = "form"]/div/button').click()


def run_bots(no_times, link_name):
    driver = build_driver()  # initialize the driver
    for i in range(no_times):  # go through the survey several times
        driver.get(link_name)  # open the browser to the url of your survey
        # check if one can do th survey(e.g. if quota is full start page is not shown(in our case 20 participants)
        if check_exists_by_xpath(driver, "//*[@id='id_entry_question']") == 1:
            x = welcome_page(driver)  # check whether they are eligible
            if x == 1:  # then they are not eligible, otherwise no next page
                continue
        demo_page(driver)  # demo-page(age, gender etc)
        #       # check if extra site is shown to you shown
        if check_exists_by_xpath(driver, '//*[@id="form"]/div/h3') == 1:
            only_one_group(driver)
        cat_pets(driver)
        end_of_survey(driver)
    print("Success!")


# this is the session wide link
link = 'http://localhost:8000/join/sedukeha'
run_bots(no_times=20, link_name=link)
