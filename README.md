# OpenAI-Omegle
is a bot for educational purposes
this script has many bugs

1- first you have to set the path to chromedriver.exe here is an example:
    
    driver = webdriver.Chrome(executable_path='E:\chromedriver\chromedriver.exe')
    driver.get("https://www.omegle.com/") 

2- second you have to set the topic (if you don't put anything it's default) here is:

    driver.find_element(By.CSS_SELECTOR, ".topicplaceholder").click()
    driver.find_element(By.CSS_SELECTOR, ".newtopicinput").send_keys("tiktok")
    driver.find_element(By.CSS_SELECTOR, ".newtopicinput").send_keys(Keys.ENTER)

3- third you have to put api keys (the key is in "https://beta.openai.com/account/api-keys" where you have to login) 

4- with that it should work, but as I said before it has many bugs and it was done in one night because I had insomnia, do not judge me.

