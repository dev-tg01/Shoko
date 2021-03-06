if __name__.endswith("sample_config"):
    import sys

    print(
        "The README is there to be read. Extend this sample config to a config file, don't just rename and change "
        "values here. Doing that WILL backfire on you.\nBot quitting.",
        file=sys.stderr,
    )
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    BOT_TOKEN = "1357282823:AAGxAGEcpLnMKr5Kat-gFJF3l1Knc7os8f0"
    OWNER_ID = (
        "1306543333"  # If you dont know, run the bot and do /id in your private chat with it
    )
    OWNER_USERNAME = "gojou_sensei_01"
    TELETHON_HASH =  '354ab50d5c0d499c04aebef8d7c61951' 
    TELETHON_ID = 1960206

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://mnfmghbg:0lDI1A0JOLAPpwUHD8cRRax35d1pQNUe@lallah.db.elephantsql.com"  # needed for any database modules
    REDIS_URI = "redis://Divu:Divyesh9990@@redis-18455.c238.us-central1-2.gce.cloud.redislabs.com:18455"
    MESSAGE_DUMP = -100  # needed to make sure 'save from' messages persist
    GBAN_DUMP = -100
    ERROR_DUMP = -100
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = (
        [1313665327, 1258544708, 1111332827, 1349105330, 680240877, 696086626, 604968079, 840545787, 1353333753, 239508098, 712008424]
    )  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = (
        [1222035687, 1100420431]
    )  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = (
        [1372739207]
    )  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WHITELIST_CHATS = []
    BLACKLIST_CHATS = []
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = None  
    ALLOW_EXCL = False  # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /
    CUSTOM_CMD = ('/', '!')   # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with more custom handler!
    API_OPENWEATHER = None  # OpenWeather API
    SPAMWATCH_API = 'trkjw7HsaVfkj7e0aQJoamHQ1VftxMI9SNZ0UBC_Z5Nfq~Vv9hYN9CkIVnPwM_ti' # Your SpamWatch token
    
    
class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True


