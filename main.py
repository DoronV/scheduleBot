from scheduleBot import connect, schedule

def main():
    sportjaConnector = connect.Connector()
    sportjaDriver = sportjaConnector.connect_to_sportja()

    sportjaConnector.login_to_sportja(sportjaDriver)

    sportjaScheduler = schedule.Scheduler()
    sportjaScheduler.navigate_to_schedule(sportjaDriver)
    sportjaScheduler.navigate_to_next_week(sportjaDriver)
    sportjaScheduler.make_reservation(sportjaDriver)

if __name__ == "__main__":
    main()