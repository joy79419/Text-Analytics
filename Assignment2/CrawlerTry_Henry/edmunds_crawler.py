# Import webdriver from selenium
import pandas as pd
from selenium import webdriver
chrome_path = r'/Users/chunhsiangchang/Desktop/software/selenium/chromedriver'
# prepend it with r because of the backslash characters

driver = webdriver.Chrome(chrome_path)  # This will open up a chrome window

# Take a website that you want to scrape
driver.get("https://forums.edmunds.com/discussion/18576/general/x/edmunds-members-cars-conversations")

tt = 0
ff = []
while True:
    
    posts = driver.find_elements_by_class_name('Message')
    posts1 = driver.find_elements_by_class_name('UserQuote')


        # This is the list of the blockquotes that you don't want
        
    l1 = []     
    for post in posts1:
        l1.append(post.text)


        # This is the list of all the original comments

    l2 = []
    for post in posts:
        l2.append(post.text)

        
    # Now you have to delete l1 from l2

    for j in range(0,len(l1)):
        for i in range(0,len(l2)):
            if (l1[j] in l2[i]):
                l2[i]=l2[i].replace(l1[j],'')              
        
    ff.append(l2)
    tt += 1
        
    if tt%100 == 0:
        print(tt)
        
    try:
        driver.find_element_by_link_text("»").click()

    except:
        print("stoped at:",tt)
        break


pd.DataFrame(ff).to_csv("Edmunds_General_Car_conversation.csv")