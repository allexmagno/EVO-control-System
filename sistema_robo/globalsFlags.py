from threading import Lock, Event


def init():
    global com_lock, com_event, com_msg, robo_event, robo_lock, robo_msg

    com_event = Event()
    com_lock = Lock()
    com_msg = {}

    robo_event = Event()
    robo_lock = Lock()
    robo_msg = {}