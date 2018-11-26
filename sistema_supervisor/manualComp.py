from threading import Event, Lock


def init():
    global lock_man, event_man, msg_man, main_lock, main_event, main_msg

    lock_man = Lock()
    event_man = Event()
    msg_man = {}

    main_lock = Lock()
    main_event = Event()
    main_msg = {}