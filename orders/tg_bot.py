from decouple import config

TOKEN_API = config('API_TG_BOT')
chat_id = config('chat_id')
# Нужно добавить текст
urls_request = f'https://api.telegram.org/bot{TOKEN_API}/sendMessage?chat_id={chat_id}&text='


