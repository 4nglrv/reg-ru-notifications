import threading
import schedule
import time

from actions import reg_notification_msg_action
from bot import bot, state
from enviroments import SCHEDULE_TIME, REGION


def schedule_request_handler():
    print('Schedule is started')
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    # Create the job in schedule
    schedule.every().day.at(SCHEDULE_TIME, REGION).do(lambda: reg_notification_msg_action(state, bot))
    # schedule.every(5).seconds.do(start_actions_handler)
    # Thread
    threading.Thread(target=schedule_request_handler).start()
    # Bot polling
    bot.polling()
