import pika
import json
from threading import Thread
import compartilhados
from copy import deepcopy
import time


class SAcomRX(Thread):

    def __init__(self, host):
        Thread.__init__(self)

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=str(host)))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='SA_to_SS')
        self.channel.basic_consume(self.trata_msg_recebida, queue='SA_to_SS', no_ack=True)

    def trata_msg_recebida(self, ch, method, properties, body):
        try:
            msg = json.loads(body)
        except:
            return

        # Identificador (indica que a msg veio do SS)
        msg['_dir'] = 'sa'

        print("sadTry")
        with compartilhados.switch_lock:
            print("sadLock")
            # Copia a mensagem para o buffer de transmissao
            compartilhados.switch_msg = deepcopy(msg)
            print("sadcopy")
            # Chama o gerente
            compartilhados.switch_event.set()
            print("sadset")
            # Tempo de seguranca para o gerente pegar a msg
            time.sleep(0.2)

            compartilhados.switch_event.clear()
            print("sad")


    def run(self):
        self.channel.start_consuming()