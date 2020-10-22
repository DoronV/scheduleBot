from unittest import TestCase
from scheduleBot import connect
from time import sleep

class ConnectionTest(TestCase):

    def test_connect_to_sportja(self):
        testConnection = connect.Connector()
        testDriver = testConnection.connect_to_sportja()

        self.assertEqual(testDriver.title, "SPORTJA Online Fitness")
        testDriver.close()

    def test_login_to_sportja(self):
        testConnection = connect.Connector()
        testDriver = testConnection.connect_to_sportja()
        testConnection.login_to_sportja(testDriver)

        sleep(5)
        sportjaXPath = testDriver.find_element_by_xpath("/html/body/nav/ul[1]/li[7]/a/span")
        self.assertTrue(sportjaXPath)
        testDriver.close()