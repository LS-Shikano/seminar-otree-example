# Imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager # For using Chrome as your browser

import time # so that we can tell the program to wait

import random # so that we can ranodmize our inputs

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
   # Find and answer the age question
   age_question_name = 'age_question'
   driver.find_element_by_name(age_question_name).send_keys('20')

   # Find the gender question by identify all element with the same name
   gender_question_name = 'gender'
   gender_options = driver.find_elements_by_name(gender_question_name)
   # Randomly select the input
   gender_choice = random.randint(0,len(gender_options)-1)
   gender_options[gender_choice].click()

   # Click the next button
   driver.find_element_by_tag_name('button').click()


# ACTION
driver = build_driver() # initialize the driver

session_wide_link= 'http://localhost:8000/join/rajofavu'
driver.get(session_wide_link) # open the browser to the url of your survey

pass_first_page(driver) # run the function for the first page
time.sleep(2) # wait for 2 seconds before proceeding to the next page
# ^ this is sometimes necessary if it takes longer for the page to load than for the script to run
pass_second_page(driver) # run the function for the second page
print('Success!')
