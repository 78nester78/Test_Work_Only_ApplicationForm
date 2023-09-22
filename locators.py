from selenium.webdriver.common.by import By

NAME_FIELD = (By.NAME, 'name')
EMAIL_FIELD = (By.NAME, 'email')
PHONE_FIELD = (By.NAME, 'phone')
COMPANY_FIELD = (By.NAME, 'company')


START_PAGE = (By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/h2')
COMP_OF_WORKS = (By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/form/div[2]/div[1]/label[1]/span')
ABOUT_PROJECT = (By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[2]/form/div[2]/div[2]/textarea')
BUDGET = (By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[2]/form/div[3]/div/label[6]/span')
SURVEY = (By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[2]/form/div[4]/div/label[3]/span')
CAPTCHA_MOVE = (By.XPATH, '//*[@id="recaptcha-anchor"]')
CAPTCHA_MOVE_1 = (By.XPATH, '//*[@id="rc-anchor-container"]/div[3]/div[1]/div/div')
CAPTCHA = (By.CLASS_NAME, 'recaptcha-checkbox-border')
WRONG_NAME = (By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div[2]/form/div[1]/div/div[1]/p')

