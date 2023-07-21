import threading
import schedule
import time

from actions import reg_notification_msg_action
from bot import bot, state
from enviroments import SCHEDULE_TIME, REGION


def start_actions_handler():
    reg_notification_msg_action(state=state, bot=bot)


def schedule_request_handler():
    print('Schedule is started')
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    # Create the job in schedule.
    schedule.every().day.at(SCHEDULE_TIME, REGION).do(reg_notification_msg_action)
    # schedule.every(60).seconds.do(start_actions_handler)
    # Thread
    threading.Thread(target=schedule_request_handler).start()
    # Bot polling
    bot.polling()
