from src.modules.bot import Bot
from src.modules.capture import Capture
from src.modules.listener import Listener
from src.modules.notifier import Notifier
import time
from random import random
from src.common import config


bot = Bot()
capture = Capture() 
# listener = Listener()
notifier = Notifier()

bot.start()
while not bot.ready:
    time.sleep(0.01)

notifier.start()
while not notifier.ready:
    time.sleep(0.01)

capture.start()
while not capture.ready:
    time.sleep(0.01)



    
    
# listener.start()
# while listener.ready:
#     time.sleep(0.01)


