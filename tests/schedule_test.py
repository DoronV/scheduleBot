import datetime
from unittest import TestCase
from scheduleBot import schedule, connect
from time import sleep

class ScheduleTest(TestCase):

    def test_navigate_to_schedule(self):
        connector = connect.Connector()
        sportjaDriver = connector.connect_to_sportja()
        connector.login_to_sportja(sportjaDriver)
        sleep(1)

        sportjaScheduler = schedule.Scheduler()
        testDriver = sportjaScheduler.navigate_to_schedule(sportjaDriver)

        sportjaXPath = testDriver.find_element_by_xpath("/html/body/div[7]/div[2]/div[2]/div[3]/div/div[3]/div[6]/div[3]/div[1]/span[1]") 
        self.assertTrue(sportjaXPath)
        testDriver.close()
    
    def test_check_if_current_week(self):
        connector = connect.Connector()
        sportjaDriver = connector.connect_to_sportja()
        connector.login_to_sportja(sportjaDriver)
        sleep(1)

        sportjaScheduler = schedule.Scheduler()
        testDriver = sportjaScheduler.navigate_to_schedule(sportjaDriver)

        sleep(1)
        weekNumber = str(datetime.date.today().isocalendar()[1])
        weekNumberXPath = testDriver.find_element_by_xpath("/html/body/div[7]/div[2]/div[2]/div[3]/div/div[1]/div[1]/span")
        text = weekNumberXPath.text
        self.assertRegex(text, weekNumber)
        testDriver.close()
    
    def test_check_if_next_week(self):
        connector = connect.Connector()
        sportjaDriver = connector.connect_to_sportja()
        connector.login_to_sportja(sportjaDriver)
        sleep(1)

        sportjaScheduler = schedule.Scheduler()
        sportjaScheduler.navigate_to_schedule(sportjaDriver)
        testDriver = sportjaScheduler.navigate_to_next_week(sportjaDriver)

        sleep(1)
        weekNumber = str(datetime.date.today().isocalendar()[1]+1)
        weekNumberXPath = testDriver.find_element_by_xpath("/html/body/div[7]/div[2]/div[2]/div[3]/div/div[1]/div[1]/span")
        text = weekNumberXPath.text
        self.assertRegex(text, weekNumber)
        testDriver.close()
    
    def test_make_reservation(self):
        connector = connect.Connector()
        sportjaDriver = connector.connect_to_sportja()
        connector.login_to_sportja(sportjaDriver)
        sleep(1)

        sportjaScheduler = schedule.Scheduler()
        sportjaScheduler.navigate_to_schedule(sportjaDriver)
        sleep(1) 

        sportjaScheduler.make_reservation(sportjaDriver)
