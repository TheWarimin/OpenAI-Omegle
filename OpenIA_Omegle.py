from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import openai
import time

try:
    # Selenium setup here you put the path to chromedriver.exe
    driver = webdriver.Chrome(executable_path='E:\chromedriver\chromedriver.exe')
    driver.get("https://www.omegle.com/") 

    # Open omegle and put the topic
    driver.find_element(By.CSS_SELECTOR, ".topicplaceholder").click()
    driver.find_element(By.CSS_SELECTOR, ".newtopicinput").send_keys("HERE YOU PUT THE TOPIC")
    driver.find_element(By.CSS_SELECTOR, ".newtopicinput").send_keys(Keys.ENTER)
       
    # Agree with the terms of service and continue
    driver.find_element(By.ID, "textbtn").click()
    driver.find_element(By.CSS_SELECTOR, "p:nth-child(2) input").click() 
    driver.find_element(By.CSS_SELECTOR, "p:nth-child(3) input").click() 
    driver.find_element(By.CSS_SELECTOR, "p > input").click()

    # Now we gonna put time (because the page needs time to charge)
    time.sleep(6) 

    # Now you make click box chat and you write and send them
    driver.find_element(By.CSS_SELECTOR, ".chatmsg").click()

    # Now we gonna put time again (because the page needs time to charge)
    #time.sleep(2) 

    #driver.find_element(By.CSS_SELECTOR, ".chatmsg").send_keys("hola")
    #driver.find_element(By.CSS_SELECTOR, ".sendbtn").click()

    def continue_conversation(driver):

        # OpenAI API key setup
        openai.api_key = "HERE YOU PUT THE API KEYS"
        previous_response = None
        while True:
            # Wait for the other person's response
            try:
                wait = WebDriverWait(driver, 10)
                response = wait.until(EC.presence_of_element_located((By.XPATH,"(//*[@class='strangermsg'])[last()]")))
            except TimeoutException:
                time.sleep(2) 
                driver.find_element(By.CSS_SELECTOR, ".disconnectbtn").click()
                time.sleep(1) 
                driver.find_element(By.CSS_SELECTOR, ".disconnectbtn").click()

            response_text = response.text
            if response_text.startswith("Stranger:"):
                response_text = response_text[9:]
                print(response.text)
                if previous_response != response_text:
                    previous_response = response_text
                    

                    # Use OpenAI to generate a response             
                    response_text = openai.Completion.create(
                        engine="text-davinci-002",
                        prompt=f"{response.text}\n",
                        max_tokens=2048,
                        n = 1,
                        stop=None,
                        temperature=0.7
                        )
                    
                    # Send the response
                    driver.find_element(By.CSS_SELECTOR, ".chatmsg").send_keys(response_text.choices[0].text.replace("you:","").replace("User:","").replace("You:","").replace("Stranger:","").replace("Person:","").replace("Me:","").replace("Friend:",""))
                    driver.find_element(By.CSS_SELECTOR, ".sendbtn").click()
                    
            try:
                if not driver.find_element(By.CSS_SELECTOR, ".chatmsg").is_enabled():
                    time.sleep(2) 
                    driver.find_element(By.CSS_SELECTOR, ".disconnectbtn").click()
                    time.sleep(1) 
                    driver.find_element(By.CSS_SELECTOR, ".disconnectbtn").click()                   
                    #driver.find_element(By.CSS_SELECTOR, ".disconnectbtn").click()
                    #break
            except NoSuchElementException:
                pass    


    continue_conversation(driver)

except Exception as e:
    with open("error_log_prueba.txt", "w") as f:
        f.write(str(e))
