from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import config

def main():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    #chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    
    return driver

def login(driver):
    driver.get('https://www.linkedin.com/login')
    username_field = driver.find_element(By.ID,value='username')
    password_field = driver.find_element(By.ID,value='password')
    username_field.send_keys(config.credential_dict.get('username'))
    password_field.send_keys(config.credential_dict.get('password'))
    
    sign_in_button = driver.find_element(By.CLASS_NAME, value="btn__primary--large")
    print(sign_in_button.text)
    sign_in_button.click()
    
def jobSearch(driver):
    driver.get('https://www.linkedin.com/jobs')
    
    if len(config.query_dict) == 0:
        job_title_input = input("Enter the job title that you want:\n")
        location_input = input("Enter the location:\n")
        config.query_dict['job_title'] = job_title_input
        config.query_dict['location'] = location_input

    driver.implicitly_wait(5)
    
    ember = driver.find_element(By.CLASS_NAME, value="ember-view")
    ember_value = ember.get_attribute('id')
    
    job_text = driver.find_element(By.CLASS_NAME, value="jobs-search-box__text-input")
    job_text.send_keys(config.query_dict['job_title'])
    job_text.click()
        
    location_text = driver.find_element(By.ID, value=f"jobs-search-box-location-id-{ember_value}")
    location_text.send_keys(config.query_dict['location'])
    location_text.send_keys(Keys.ENTER)

def jobApply(driver):
    # easy_apply_button = driver.find_element(By.XPATH, value='//*[@id="ember380"]')
    pass


if __name__ == "__main__":
    browser = main()
    login(browser)
    jobSearch(browser)
    jobApply(browser)