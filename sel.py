from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://dzen.ru/news/story/ad1d0484-edcb-572f-9c96-b5905959bfbf?lang=ru&\
           opertop=1&persistent_id=3427005603&rubric=personal_feed&story=b229580a-23fa-51be\
           -8b6a-9e744cf86049&t=7508254372204122112&rid=1407953924.1322.1790110226613.56331')
first_type = driver.find_element(By.CLASS_NAME, 'news-link-new')
print(first_type.get_attribute('href'))