import requests
import urllib
import json

class TelegramBot(object):

    def __init__(self, token, url):
        self.token = token
        self.url = url

    def get_url(self, url):
        response = requests.get(url).content.decode('utf8')
        return json.loads(response)

    #timeout=100 makes so that connection is kept open to wait for new messages long polling
    #? is start of argument list in URL, & is for each additional argument
    def get_updates(self, offset=None):
        url = self.url + 'getUpdates?timeout=100'
        if offset:
            url += '&offset={}'.format(offset)
        return get_url(url)

    def get_last_chat_id_and_text(self, updates):
        num_updates = len(updates['result'])
        last_update = num_updates-1
        text = updates['result'][last_update]['message']['text']
        chat_id = updates['result'][last_update]['message']['chat']['id']
        return (text, chat_id)

    def get_last_update_id(self, updates):
        update_ids = []
        for update in updates['result']:
            update_ids.append(int(update['update_id']))
        return max(update_ids)


    def send_message(self, text, chat_id):
        text = urllib.parse.qoute_plus(text) #avoids conflicts with special characters in text
        url = self.url + 'sendMessage?text={}&chat_id={}'.format(text, chat_id)
        get_url(url)

    #gets all new updates and send replies
    def main():
        last_update_id = None
        while True:
            updates = get_updates(last_update_id)
            if len(updates["result"]) > 0:
                last_update_id = get_last_update_id(updates) + 1
                echo_all(updates)
            time.sleep(0.5)
