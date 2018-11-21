from threading import Lock, Event


def init():
    global enviar_sa_event, sa_lock, sa_msg, switch_event, switch_lock, switch_msg, sr_event, sr_lock, sr_msg

    enviar_sa_event = Event()
    sa_lock = Lock()
    sa_msg = {}

    switch_event = Event()
    switch_lock = Lock()
    switch_msg = {}

    sr_event = Event()
    sr_lock = Lock()
    sr_msg = {}


