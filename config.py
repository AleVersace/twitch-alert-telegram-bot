# Deploy
HEROKU_URL = 'https://*******.herokuapp.com/'   # Your Heroku App URL (or others)


# Twitch
TWITCH_URL = 'https://twitch.tv/******'     # Your twitch channel url
TWITCH_CLIENT_ID = ''   # Your twitch dev app client ID
TW_CH = '' # Your twitch channel name


# Telegram & Bot
TOKEN = ''  # Your telegram bot token (Generated by BotFather)
CHAT_ID = '@******'   # Channel tag
BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)
LOCAL_WEBHOOK_ENDPOINT = '{}/{}'.format(HEROKU_URL, TOKEN)
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_URL, LOCAL_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessagie?chat_id={}&text={}'


# Twitch API
TWITCH_API = 'https://api.twitch.tv/helix/webhooks/hub'
USR_ID = 1234   # Your twitch channel usr id
TOPIC = 'https://api.twitch.tv/helix/streams?user_id={}'.format(USR_ID)
JSON_TWITCH_REQ = {
    'hub.callback': HEROKU_URL + TW_CH,
    'hub.mode': 'subscribe',
    'hub.topic': TOPIC,
    'hub.lease_seconds': 864000,
    'hub.secret': ''
}
APP_ACCESS_TOKEN = ''   # Twitch App access token - Expires every 60days
