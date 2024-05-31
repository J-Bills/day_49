from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import credential_dict, query_dict

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
    username_field.send_keys(credential_dict.get('username'))
    password_field.send_keys(credential_dict.get('password'))
    
    sign_in_button = driver.find_element(By.CLASS_NAME, value="btn__primary--large")
    print(sign_in_button.text)
    sign_in_button.click()
    
def jobSearch(driver):
    driver.get('https://www.linkedin.com/jobs')
    
    if len(query_dict) == 0:
        job_title_input = input("Enter the job title that you want")
        location_input = input("Enter the location")
        query_dict['job_title'] = job_title_input
        query_dict['location'] = location_input

    driver.implicity_wait(5)
    job_text = driver.find_element(By.CLASS_NAME, value="jobs-search-box__text-input")
    job_text.send_keys(query_dict['job_title'])
    

if __name__ == "__main__":
    browser = main()
    login(browser)
    jobSearch(browser)