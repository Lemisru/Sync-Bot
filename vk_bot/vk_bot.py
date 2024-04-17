from vkbottle.bot import Bot

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import API, state_dispenser, labeler
from handlers import reactions_labeler

labeler.load(reactions_labeler)

bot = Bot(api=API, 
          labeler=labeler, 
          state_dispenser=state_dispenser)

if __name__ == "__main__":
    bot.run_forever()