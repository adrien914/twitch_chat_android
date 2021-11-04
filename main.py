from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import StringProperty
from twitch_chat import TwitchChat
from dotenv import load_dotenv
from functools import partial
from kivy.clock import Clock
from kivy.app import App
import plyer
import os

def listen_to_chat_process(my_chat, dt):
    user, message = my_chat.listen_to_chat()   
    print(f'{user}: {message}')
    plyer.notification.notify(title=user, message=message)

class Container(AnchorLayout):
    label_string = StringProperty("Enter the name of your channel here")

class TwitchChatApp(App):
    quit = False
    event = None

    def build(self):
        self.container = Container()
        return self.container

    def start_listener(self, channel_name):
        self.container.label_string = "Script running ..."
        load_dotenv()
        my_chat = TwitchChat(oauth=os.environ.get('OAUTH'), channel_name=channel_name, bot_name='listen_bot')
        self.event = Clock.schedule_interval(partial(listen_to_chat_process, my_chat), .1)

    def stop_app(self):
        if self.event: self.event.cancel()
        exit()

if __name__ == '__main__':
    TwitchChatApp().run()