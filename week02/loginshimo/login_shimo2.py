from selenium import webdriver
import time

def login():        
    try:
        browser = webdriver.Chrome()
        browser.get('https://shimo.im/login?from=home')
        time.sleep(1)

        account_input = browser.find_element_by_name('mobileOrEmail') # browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/input')
        account_input.send_keys('+8613866666666')

        password_input = browser.find_element_by_name('password') # browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input')
        password_input.send_keys('shimopassword')
        time.sleep(1)
        
        btn_login = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button')
        btn_login.click()

        cookies = browser.get_cookies() # 获取cookies
        print(cookies)
        time.sleep(3)

    except Exception as e:
        print(e)
    finally:
        browser.close()

if __name__ == "__main__":
    login()