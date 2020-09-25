from selenium import webdriver

try:
    driver=webdriver.Chrome(executable_path='C:\\Users\\rubel\\Documents\\python-webui-testing\\chromedriver.exe')
except Exception as e:
    print(e)
driver.get('http://letslit123.com/')
titel=driver.title
driver.find_element_by_name('userid').send_keys('Admin')

print('titel of the page is : ', titel)