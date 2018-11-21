import pika
import json
from threading import Thread
import compartilhados
from copy import deepcopy
import time


class SAcomRX(Thread):

    def __init__(self, host):
        super(SAcomRX, self).__init__()

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=str(host)))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='SA_to_SS')
        self.channel.basic_consume(self.trata_msg_recebida, queue='SS_to_SA', no_ack=True)

    def trata_msg_recebida(self, ch, method, properties, body):
        try:
            msg = json.loads(body)
        except:
            return

        # Identificador (indica que a msg veio do SS)
        msg['_dir'] = 'sa'

        with compartilhados.gerente_msg_lock:
            # Copia a mensagem para o buffer de transmissao
            compartilhados.gerente_msg = deepcopy(msg)

            # Chama o gerente
            compartilhados.solicita_gerente.set()

            # Tempo de seguranca para o gerente pegar a msg
            time.sleep(0.2)


    def run(self):
        self.channel.start_consuming()