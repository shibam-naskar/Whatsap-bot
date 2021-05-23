from selenium import webdriver
import pyautogui as pt
import selenium
import random
import requests
import urllib
from youtubesearchpython import VideosSearch
from time import sleep
from time import sleep
from prsaw import RandomStuff
from googlesearch import search
from gtts import gTTS
from config import CHROME_OROFILE_PATH

options = webdriver.ChromeOptions()
options.add_argument(CHROME_OROFILE_PATH)
driver = webdriver.Chrome("/usr/bin/chromedriver",options=options)
driver.get("https://web.whatsapp.com/")


#covid 19 api
url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

headers = {
    'x-rapidapi-key': "<APIKEY>",
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)
response1 = response.json()

# covid 19 api end




print("Login")

name = input("Enter name")
msg = " "
loopCode1 = "!loopspam".lower()



nameReply = ['hi i am wall-e','ooh my name is wall-e','oh there you can call me wall-e','shibam calls me walle so you can also','wall-e is here','hey there wall-e is here','wall-e','hellow there i am walle a inteligent bot','no fikar jab walle is here','humko sab wall-e kehte hai']
shibamReply = ['shibam is a verry humble man','shibam is a verry good boy','oh my owner shibam is verry kindman','shibam is verry good boy']

user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

while True:
    try:
        message = driver.find_elements_by_class_name("_3-8er")[-1]
    
        if(message.text != msg):
            whatsapp_messege = str(message.text).lower()
            if("bot" in whatsapp_messege):
                if("hi" in whatsapp_messege):
                    finalReply = "hlw buddy"
                    msg = finalReply
                    msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                    msgBox.send_keys(finalReply)
                    sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                    sendButton.click()
                elif("are you" in whatsapp_messege):
                    finalReply = "i know i am a bot but shibam trained me like a human"
                    msg = finalReply
                    msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                    msgBox.send_keys(finalReply)
                    sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                    sendButton.click()
            

            
            # elif(loopCode1 in whatsapp_messege):
            #     smsg = whatsapp_messege.split()
            #     try:
            #         number = int(smsg[2])
            #         msg1 = smsg[1]
            #         finalReply = msg1
            #         msg = finalReply
            #         for i in range(number):
            #             msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            #             msgBox.send_keys(finalReply)
            #             sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
            #             sendButton.click()
            #     except ValueError:
            #         finalReply = "The number is not defined please try again"
            #         msg = finalReply
            #         msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            #         msgBox.send_keys(finalReply)
            #         sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
            #         sendButton.click()
            elif("your name" in whatsapp_messege or "who are you" in whatsapp_messege or "your name?" in whatsapp_messege):
                indexNo = random.randint(0,9)
                finalReply = nameReply[indexNo]
                msg = finalReply
                msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                msgBox.send_keys(finalReply)
                sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                sendButton.click()

            elif("!play" in whatsapp_messege):
                whatsapp_messege = whatsapp_messege.replace("!play", "")
                videosSearch = VideosSearch(whatsapp_messege, limit = 2)
                result1 = videosSearch.result()
                input1 = result1['result'][0]['link']
                finalReply = input1
                msg = finalReply
                msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                msgBox.send_keys(finalReply)
                sleep(5)
                sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                sendButton.click()

            elif("!say" in whatsapp_messege and whatsapp_messege != msg):
                msg= whatsapp_messege
                whatsapp_messege = whatsapp_messege.replace("!say","")
                tts = gTTS(whatsapp_messege)
                tts.save('response.mp4')
                filepath = "/home/shibam/shibam-codes/python/gabriel-whatsap-bot/response.mp4"
                attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
                attachment_box.click()
                            
                image_box = driver.find_element_by_xpath(
                                '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                image_box.send_keys(filepath)

                sleep(2)

                send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
                send_button.click() 


            elif("!search" in whatsapp_messege):
                whatsapp_messege = whatsapp_messege.replace("!search ", "")
                for i in search(whatsapp_messege, tld="com", num=5, stop=5,pause=2):
                    finalReply = str(i)
                    msg = finalReply
                    msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                    msgBox.send_keys(finalReply)
                    sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                    sendButton.click()


            elif("joke" in whatsapp_messege or "jokes" in whatsapp_messege):
                    r = requests.get('https://icanhazdadjoke.com/slack')
                    joke = r.json()['attachments'][0]['text']
                    finalReply = joke
                    msg = finalReply
                    msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                    msgBox.send_keys(finalReply)
                    sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                    sendButton.click()
            elif("meme"in whatsapp_messege and whatsapp_messege != msg):
                msg = whatsapp_messege

                r = requests.get('https://meme-api.herokuapp.com/gimme/wholesomememes')
                pic_url = r.json()['preview'][2]

                urllib.request.urlretrieve(str(pic_url), "meme.jpg")
                filepath = "/home/shibam/shibam-codes/python/gabriel-whatsap-bot/meme.jpg"
                attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
                attachment_box.click()
                            
                image_box = driver.find_element_by_xpath(
                                '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
                image_box.send_keys(filepath)

                sleep(2)

                send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
                send_button.click() 
            elif("covid status of" in whatsapp_messege):
                whatsapp_messege = whatsapp_messege.replace("covid status of", "")
                string = whatsapp_messege.split()
                
                for i in range(len(string)):
                    string[i] = string[i].replace(string[i], string[i].capitalize())

                listToStr = ' '.join([str(elem) for elem in string])

            
                if(listToStr == "India"):
                    try:
                        for each in response1['total_values']:
                            finalReply = each + ' : '+ response1['total_values'][each]
                            msg = finalReply
                            msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                            msgBox.send_keys(finalReply)
                            sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                            sendButton.click()
                    except KeyError:
                            finalReply = "i have not found any data of this country " + str(listToStr)
                            msg = finalReply
                            msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                            msgBox.send_keys(finalReply)
                            sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                            sendButton.click()
                        
                else:
                    try:
                        for each in response1['state_wise'][str(listToStr)]:
                            finalReply = each + ' : ' + response1['state_wise'][str(listToStr)][each]
                            msg = finalReply
                            msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                            msgBox.send_keys(finalReply)
                            sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                            sendButton.click()
                            if(each == 'statenotes'):
                                break
                    except KeyError:
                        finalReply = "i have not found any state with the name of " + str(listToStr)
                        msg = finalReply
                        msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                        msgBox.send_keys(finalReply)
                        sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                        sendButton.click()

            elif("who is your dad" in whatsapp_messege or "what is your fathers name" in whatsapp_messege or "who is your father" in whatsapp_messege or "who have created you" in whatsapp_messege or "who is your creator" in whatsapp_messege):
                finalReply = "i was created by shibam i know him as my father"
                msg = finalReply

                msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                msgBox.send_keys(finalReply)
                sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                sendButton.click()
            
            elif("!weather of" in whatsapp_messege):
                whatsapp_messege = whatsapp_messege.replace("!weather of", "")
                response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={whatsapp_messege}&appid=6fed6f20c4335444cc1258a52b955765').json()
                try:
                    wind = "wind speed:s "+ str(response['wind']['speed']) + " km/h"
                    temprature = "temp: "+ str(response['main']['temp'])+" F"
                    description = "it might be "+str(response['weather'][0]['description'])+" outside"
                    humidity = "humidity is "+ str(response['main']['humidity'])+"%"
                    atm = "atm pressure "+str(response['main']['pressure'])
                    finalReply = str(temprature)+"\n"+str(wind)+"\n"+str(humidity)+"\n"+str(atm)+"\n"+str(description)
                    msg = str(description)
                except:
                    finalReply = "i cant find the data of" + whatsapp_messege
                    msg = finalReply
                    msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                    msgBox.send_keys(finalReply)
                    sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                    sendButton.click()
                    msg = finalReply


                msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                msgBox.send_keys(finalReply)
                sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                sendButton.click()


            else:
                api_key = "jYLk9BFC0WEO"
                rs = RandomStuff(api_key = api_key)

                response =  rs.get_ai_response(whatsapp_messege)
                if(response == "Error: Incorrect Usage!"):
                    print("error in api")
                elif("support@affiliateplus.xyz?" in str(response)):
                    print("address")
                elif("support@affiliateplus.xyz." in str(response)):
                    print("address")
                elif("RSA." in str(response)):
                    finalReply = "who is that shibam calls me wall-e"
                    msg = finalReply
                    msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                    msgBox.send_keys(finalReply)
                    sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                    sendButton.click()
                elif("PGamerX" in str(response)):
                    indexNo = random.randint(0,3)
                    finalReply = shibamReply[indexNo]
                    msg = finalReply
                    msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                    msgBox.send_keys(finalReply)
                    sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                    sendButton.click()
                else:
                    finalReply = response
                    msg = finalReply
                    msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                    msgBox.send_keys(finalReply)
                    sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
                    sendButton.click()


    except:
        print("reloading")



                    




 




