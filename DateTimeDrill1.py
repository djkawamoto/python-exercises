#!/usr/local/bin/python2
# The Tech Academy Python Course step 66 of 79
# datetime drill by Daniel Kawamoto

from datetime import datetime

class OfficeHours():

    def TimeCheck():
        now = datetime.now().time()
        nowHour = int(now.hour)
        nowMinute = list(now.strftime('%M'))
        ampm = 'AM'
        if nowHour == 24:
            ampm = 'AM.'
        elif nowHour > 24:
            ampm = 'AM.'
        elif nowHour > 12:
            ampm = 'PM.'
        print now.strftime('The time in PORTLAND(HQ) is %I:%M'), ampm

        def IsNYCOpen(): # Checks if New York office is open
            nycHour = nowHour + 3
            ampm = 'AM'
            nycMinute = nowMinute
            if nycHour == 24:
                nycHour = nycHour - 12
                ampm = 'AM'
            elif nycHour > 24:
                nycHour = nycHour - 24
                ampm = 'AM'
            elif nycHour > 12:
                nycHour = nycHour - 12
                ampm = 'PM'

            # Determines if the office is OPEN or CLOSED
            openClosed = 'TEST'
            if ampm == 'AM':
                if nycHour < 9 or nycHour == 12:
                    openClosed = 'CLOSED'
                else:
                    openClosed = 'OPEN'
            if ampm == 'PM':
                if nycHour < 9 or nycHour == 12:
                    openClosed = 'OPEN'
                else:
                    openClosed = 'CLOSED'
            nycMinute = "".join(nycMinute)
            print ('The time at the NEW YORK CITY office is %s:%s %s -- the office is %s.' % (nycHour, nycMinute, ampm, openClosed))


        def IsLDNOpen(): # Checks if London office is open
            ldnHour = nowHour + 8
            ampm = 'AM'
            ldnMinute = nowMinute

            # Determines AM or PM
            if ldnHour == 24:
                ldnHour = ldnHour - 12
                ampm = 'AM'
            elif ldnHour > 24:
                ldnHour = ldnHour - 24
                ampm = 'AM'
            elif ldnHour > 12:
                ldnHour = ldnHour - 12
                ampm = 'PM'

            # Determines if the office is OPEN or CLOSED
            openClosed = ''
            if ampm == 'AM':
                if ldnHour < 9 or ldnHour == 12:
                    openClosed = 'CLOSED'
                else:
                    openClosed = 'OPEN'
            if ampm == 'PM':
                if ldnHour < 9 or ldnHour == 12:
                    openClosed = 'OPEN'
                else:
                    openClosed = 'CLOSED'
            ldnMinute = "".join(ldnMinute)
            print ('The time at the LONDON office is %s:%s %s -- the office is %s.' % (ldnHour, ldnMinute, ampm, openClosed))

        IsNYCOpen()
        IsLDNOpen()

    TimeCheck()


if __name__ == "__main__":
    OfficeHours()
