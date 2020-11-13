from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
#from returnPassword import getPassword

# for removing error chrome is not reachable

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
#chrome = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")

def login():



    #y = input("fffff : ")
    time.sleep(5)

    username = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    username.send_keys("username")
    time.sleep(5)


    password = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    password.send_keys("password")
    time.sleep(5)

    password.send_keys(Keys.ENTER)
    time.sleep(30)
    #x=input("xxxx: ")

    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()#not now

    time.sleep(30)
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()# notification turn on
    

def search():
    time.sleep(20)
    item = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
    time.sleep(5)
    item.send_keys("dushyant__brahman")
    time.sleep(5)
    item.send_keys(Keys.ENTER)
    driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div/div[2]/div/span").click()

def likeandcomment():
    time.sleep(30)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]").click()
    #driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[4]/article/div[1]/div/div[1]/div[1]/a/div/div[2]").click()# firstpic
    for i in range(10):
        time.sleep(5)
        #like image
        post = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[2]/div/div/div[2]")
        ac = ActionChains(driver)
        ac.double_click(post).perform()
        
        #comments
        time.sleep(5)
        po=driver.find_element_by_css_selector(".Ypffh")
        po.send_keys("Nice pic")
        po.send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element_by_css_selector("._65Bje").click()#forwarding images
def message():
    


    
   


login();
search();
likeandcomment();
