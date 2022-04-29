from selenium import webdriver
import time


def wait(x):
    time.sleep(x)

def aria_search(label):
    return 


if __name__ == "__main__":

    connection_requests_sent = 0

    enter_driver_loc = input('Enter the file path of your webdriver: ')

    driver = webdriver.Chrome(enter_driver_loc)
    driver.get('https://www.linkedin.com')
    wait(2)



    #Login
    username = driver.find_element_by_xpath("//input[@name ='session_key']")
    password = driver.find_element_by_xpath("//input[@name ='session_password']")

    enter_user = input("Enter your LinkedIn Username: ")
    enter_pass = input("Enter your LinkedIn Password: ")

    username.send_keys(enter_user)
    password.send_keys(enter_pass)
    wait(2)

    driver.find_element_by_xpath("//button[@type='submit']").click()
    wait(2)



    #Navigation to Connections Page

    search = driver.find_element_by_xpath("//input[@aria-label ='Search']")
    search.send_keys("keysToSend")
    search.submit()
    wait(2)

    driver.find_element_by_xpath("//button[@aria-label='People']").click()
    wait(2)

    driver.find_element_by_xpath("//button[@aria-label='Connections filter. Clicking this button displays all Connections filter options.']").click()
    wait(2)

    search = driver.find_element_by_xpath("//input[@value ='S']").click()
    wait(2)

    driver.find_element_by_xpath("//button[@aria-label='Apply current filter to show results']").click()



    #Sending Connect Requests

    connection_requests_sent = 0
    

    while connection_requests_sent <=80:

        #Finding all potential Connections

        total_buttons = driver.find_elements_by_tag_name('button')

        connect_buttons = [button for button in total_buttons if button.text == 'Connect']

        connection_requests_sent = 0




        #Sending the Connection Requests

        for button in connect_buttons:

            driver.execute_script("arguments[0].click();", button)

            wait(2)


            send = driver.find_element_by_xpath("//button[@aria-label='Send now']")

            driver.execute_script("arguments[0].click();", send)

            wait(2)


            close_privacy_restrictions = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")

            driver.execute_script("arguments[0].click();", close_privacy_restrictions)

            wait(2)




        #Going to the Next Page of Connections

        next_page = driver.find_element_by_xpath("//button[@aria-label='Next']")

        driver.execute_script("arguments[0].click();", next_page)

        # Improvement: Do not limit connections to certain amount and let program work until daily connection request
        # limit reached



    #Success Message

    print("You've sent approximately 80 Connection Requests!")

    






