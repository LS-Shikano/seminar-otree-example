# Imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  # For using Chrome as your browser

import time  # so that we can tell the program to wait

import random  # so that we can randomize our inputs


# FUNCTIONS
def build_driver():
    # Set up the driver
    return webdriver.Chrome(ChromeDriverManager().install())


def pass_first_page(driver):
    # Click through first page
    # Give input to the entry question - find the element by its id
    entry_question_id = 'id_entry_question'
    entry_question_input = 'Testing Input for Entry Question'
    driver.find_element_by_id(entry_question_id).send_keys(entry_question_input)

    # Give input to the eligibility question - find the element by xpath
    eligibility_xpath = '//*[@id="form"]/div/input[5]'
    driver.find_element_by_xpath(eligibility_xpath).click()

    # Click the next button
    # Find the element by its tag
    driver.find_element_by_tag_name('button').click()


def pass_second_page(driver):
    # First, check that we've actually passed to the second page, and have not been redirected
    current_url = driver.current_url  # one way to do this is to check the url of the current page
    print(f"Current Url: {current_url}")
    if 'mingle' not in current_url:
        # Find and answer the age question
        age_question_name = 'age_question'
        driver.find_element_by_name(age_question_name).send_keys('20')

        # Find the gender question by identify all element with the same name
        gender_question_name = 'gender'
        gender_options = driver.find_elements_by_name(gender_question_name)
        # Randomly select the input
        gender_choice = random.randint(0, len(gender_options) - 1)
        gender_options[gender_choice].click()

        # Click the next button
        driver.find_element_by_tag_name('button').click()
    else:
        print("You've been redirected")


def pass_third_page(driver):
    # Again, check which page you're on first. Here's another way to do that

    # Another way to do this is to search for any elements matching a certain identification
    popout_questions = driver.find_elements_by_name("popout_question")

    if len(popout_questions) > 0:  # if an element is found, then you're on the right page
        yes_xpath = '//*[@id="merkelYes"]'
        driver.find_element_by_xpath(yes_xpath).click()

        driver.find_element_by_name('popout_yes').send_keys("In a vision")
        driver.find_element_by_tag_name('button').click()

    else:
        # So we're not on the popout question page - verify that we're on the HTML-Overview page
        h3_heading = driver.find_elements_by_tag_name('h3')
        if len(h3_heading) > 0:
            print("We're on the HTML-Overview page")
            # Use JavaScript to scroll to the end of the page
            # This doesn't have any functionality here, it's just to demonstrate how using JavaScript works
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)


def pass_final_page(driver):
    # Here's another way to investigate what's happening on the page- you can take a screenshot for manual verification
    driver.save_screenshot('FinalPageSreenshot.png')

    # Now we can computationally check by looking for text that we're expecting to see
    headings = driver.find_elements_by_tag_name('h2')
    final_text = False
    for heading in headings:
        if "End" in heading.text:
            final_text = True
    if final_text == True:
        driver.find_element_by_tag_name('button').click()
    else:
        print("You are not on the final page")


# ACTION
driver = build_driver()  # initialize the driver

session_wide_link = 'http://localhost:8000/join/mamidejo'
driver.get(session_wide_link)  # open the browser to the url of your survey

pass_first_page(driver)  # run the function for the first page
time.sleep(2)  # wait for 2 seconds before proceeding to the next page
# ^ this is sometimes necessary if it takes longer for the page to load than for the script to run
pass_second_page(driver)  # run the function for the second page

time.sleep(2)
pass_third_page(driver)

time.sleep(2)
pass_final_page(driver)
print('Success! Closing the driver now...')

driver.quit()
