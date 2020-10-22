import datetime
from scheduleBot import connect
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class Scheduler():

    def navigate_to_schedule(self, sportjaDriver: webdriver):
        self.sportjaDriver = sportjaDriver
        sportjaXPath = self.sportjaDriver.find_element_by_xpath(
            "/html/body/nav/ul[1]/li[7]/a/span"
            )
        sportjaXPath.click()
        sleep(1)

        return sportjaDriver
    
    def navigate_to_next_week(self, sportjaDriver: webdriver):
        sportjaDriver.find_element_by_css_selector(
            "#head > a:nth-child(5)"
        ).click()
        sleep(1)

        return sportjaDriver

    def make_reservation(self, sportjaDriver: webdriver):
        self.sportjaDriver = sportjaDriver
        _check_if_next_week(self)
        classnames = sportjaDriver.find_elements_by_class_name("classname")
        weightList = []
        for classname in classnames:
            if classname.text == "Weightlifting":
                weightList.append(classname)

        for elem in weightList[1:]:
            elem.click()

        sleep(1)
        reserveButton = None 
        waitingListButton = None
        cancelButton = None

        try:
            cancelButton = sportjaDriver.find_element_by_css_selector("a.grey_btn_small:nth-child(2) > span:nth-child(1)")
        except NoSuchElementException:
            print("No cancelButton found.")

        try:
            reserveButton = sportjaDriver.find_element_by_css_selector("#book_btn > span:nth-child(1)")
        except NoSuchElementException:
            print("No reserveButton found.")

        try:
            waitingListButton = sportjaDriver.find_element_by_css_selector("#join_waiting_list_btn")
        except NoSuchElementException:
            print("No waitingListButton found.")
        
        if reserveButton:
            reserveButton.click()
            sportjaDriver.close()
            print('Class reserved for next Saturday!')
            return 0
        elif waitingListButton:
            waitingListButton.click()
            sportjaDriver.close()
            print('Put on waiting list, check your mailbox')
            return 0
        elif cancelButton:
            sportjaDriver.close()
            print('Already reserved')
            return 0
        else:
            print('Can\'t reserve or put on waiting list')
            sportjaDriver.close()
            return 1

def _check_if_next_week(self):
    weekNumber = str(datetime.date.today().isocalendar()[1]+1)
    weekNumberXPath = self.sportjaDriver.find_element_by_xpath(
        "/html/body/div[7]/div[2]/div[2]/div[3]/div/div[1]/div[1]/span"
        ).text

    if weekNumber in weekNumberXPath:
        return 0
    else:
        print('Not the correct week')
        return 1