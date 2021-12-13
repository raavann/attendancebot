from os import getenv
from dotenv import load_dotenv
from dscrd.discord import class_year_error, something_wrong, start, email_pass_error, joined_class, leave_class

from data.data import update_table
from time import sleep, time
from datetime import datetime, timedelta
from bot.bot import meet_bot

# .env data validation and return table
def checkup():
    load_dotenv()
    CLASS = getenv('CLASS')
    YEAR = getenv('YEAR')
    SECTION = getenv('SECTION')

    EMAIL = getenv('EMAIL')
    PASSWORD = getenv('PASSWORD')

    if(SECTION == None):
        SECTION = ''

    classes = ['civil', 'mech', 'it', 'cse', 'etc', 'ei']
    year = ['1', '2', '3', '4']
    section = ['a','b','']

    if(CLASS not in classes or YEAR not in year or SECTION not in section):
        class_year_error()
        exit()

    if(EMAIL==None or PASSWORD==None):
        email_pass_error()
        quit()

    table = CLASS + SECTION + YEAR

    return table

def login_getlink(bot):
    login = True
    get_link = True

    # if either one is true run again!
    # Only close when both returns false
    while login or get_link:
        
        # if either one is still True, kill and restart
        if(login or get_link):
            bot.quit()

        sleep(5)
        EMAIL = getenv('EMAIL')
        PASSWORD = getenv('PASSWORD')
        login = bot.login(EMAIL, PASSWORD)

        sleep(5)
        get_link = bot.get_meet(period['link'])

def join_meeting(bot, period):
    st = datetime.fromisoformat(period['st'][:-1 ])
    if( st - timedelta(minutes=5) <  datetime.now() < st + timedelta(minutes=25)):
        login_getlink(bot)

        sleep(5)
        join_meet = bot.join()  # -2 = no join button exist
                                # -1 = no leave button but join exist and clicked
                                # 0 = everything nice
        while (join_meet != 0 and datetime.now() < datetime.fromisoformat(period['et'][:-1 ]) ):
            # close browser and do everything again
            login_getlink(bot)

            join_meet = join_meeting(bot, period)

        # if here then joined class successfully, send discord notification
        joined_class(period['sub'], datetime.now().strftime("%m/%d/%Y, %H:%M"))

        return join_meet
        

table = checkup()
start()

while(True):

    # it will be called atleast after 15minutes as while loop below runs for atleast 15minutes
    data = update_table(table)

    # data is now only those elements whose end time is more than current time
    # i.e classes which haven't completed
    data = [timetable for timetable in data if datetime.fromisoformat(timetable['et'][:-1 ]) > datetime.now()]

    if(len(data) == 0):
        # if data is none try after 15minutes
        sleep(900)
        break

    # attend classes in order, but step out every 15min to check for new period if no classes exist in these 15mins
    timestart = time()
    duration = 900
    bot = meet_bot()
    while(time() < timestart + duration):
        for period in data:
            join_meeting(bot, period)

            st = datetime.fromisoformat(period['st'][:-1 ])
            et = datetime.fromisoformat(period['et'][:-1 ])

            # sleep until class ends
            sleep( round((et-st).total_seconds()) )

            # quit class
            bot.quit()
            leave_class(period['sub'], datetime.now().strftime("%m/%d/%Y, %H:%M"))

something_wrong()