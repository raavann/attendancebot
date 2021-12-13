from dhooks import Webhook
from dhooks import Embed

from os import getenv
from dotenv import load_dotenv
load_dotenv()

hook = Webhook(getenv('DISCORD'))

colors =  {
    'teal' : 0x1abc9c,
    'green' :0x2ecc71,
    'blue' : 0x3498db,
    'purple' : 0x9b59b6,
    'red' : 0xe74c3c
}

# when bot starts functioning
def start():
    embed = Embed(
        title='All is Ready!',
        color=colors['teal'],
        description='Congratulations!\nAll is ready and set!'
    )
    embed.set_footer('~ AutoAttendance bot')

    hook.send(embed=embed)

# when while(True) fails in main.py
def something_wrong():
    embed = Embed(
        title='Hmm.. Something went terrible..',
        color=colors['red'],
        description='''It looks like the bot ran into an error!
        You can try checking the steps again by visiting https://www.autoattendance.ml/about#users
        Or you can try contacting our team at https://www.autoattendance.ml/about#contact'''
    )
    embed.set_footer('~ AutoAttendance bot')

    hook.send(embed=embed)

# incorrect information in .env file
def class_year_error():
    embed = Embed(
        title='Incorrect input!',
        color=colors['red'],
        description='''It looks like you've entered incorrect information in the `.env` file!
        The bot will stop here!
        Make sure you restart the bot after entering correct information in `.env` file!
        You can try checking the steps again by visiting https://www.autoattendance.ml/about#users
        Or you can try contacting our team at https://www.autoattendance.ml/about#contact'''
    )
    embed.set_footer('~ AutoAttendance bot')

    hook.send(embed=embed)

# incorrect information in .env file
def email_pass_error():
    embed = Embed(
        title='Email/ Pass not provided',
        color=colors['red'],
        description='''It looks like you've not provided Email and Password in the `.env` file!
        The bot will stop here!
        Make sure you restart the bot after entering correct information in `.env` file!
        You can try checking the steps again by visiting https://www.autoattendance.ml/about#users
        Or you can try contacting our team at https://www.autoattendance.ml/about#contact'''
    )
    embed.set_footer('~ AutoAttendance bot')

    hook.send(embed=embed)


# joined class
def joined_class(sub, time):
    embed = Embed(
        title='Successfully joined the class!',
        color=colors['purple'],
        description=f'''Successfully joined {sub} class, at {time}'''
    )
    embed.set_footer('~ AutoAttendance bot')

    hook.send(embed=embed)

# left class
def leave_class(sub, time):
    embed = Embed(
        title='Successfully left the class!',
        color=colors['blue'],
        description=f'''Successfully left {sub} class, at {time}'''
    )
    embed.set_footer('~ AutoAttendance bot')

    hook.send(embed=embed)
