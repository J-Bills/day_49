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
        job_title_input = input("Enter the job title that you want")
        location_input = input("Enter the location")
        config.query_dict['job_title'] = job_title_input
        config.query_dict['location'] = location_input

    driver.implicitly_wait(5)
    
    job_text = driver.find_element(By.CLASS_NAME, value="jobs-search-box__text-input")
    job_text.send_keys(config.query_dict['job_title'])
    job_text.click()
    job_id = str(job_text.get_attribute('id'))
    sesh_id = job_id.split(sep='-')[5]
    
    location_text = driver.find_element(By.ID, value=f"jobs-search-box-location-id-{sesh_id}")
    location_text.send_keys(config.query_dict['location'])
    job_text.send_keys(Keys.ENTER)
    

def jobFilter(driver):
    driver.implicitly_wait(10)
    
    easy_apply_button = driver.find_element(By.CSS_SELECTOR, value='.search-reusables__filter-binary-toggle .artdeco-pill')
    easy_apply_button.click()
    
    data_posted_button = driver.find_element(By.ID, value='searchFilter_timePostedRange')
    data_posted_button.click()
    values = driver.find_elements(By.NAME, value='date-posted-filter-value')
    value = values[3]
    value.click()
    


def nextPage(driver):
    next_page_button = driver.find_element(By.CSS_SELECTOR, value='.jobs-search-pagination .artdeco-button')


if __name__ == "__main__":
    browser = main()
    login(browser)
    jobSearch(browser)
    jobFilter(browser)