import pika
import json
from threading import Thread
import compartilhados
from copy import deepcopy
import time


class SAcomRX(Thread):

    def __init__(self, host, robo):
        Thread.__init__(self)
        self.robo = robo
        credentials = pika.PlainCredentials('robot1', 'robot1')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host, 5672, '/', credentials))
        #self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=str(host)))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='SA_to_SS',
                                      exchange_type='fanout')

        self.channel.queue_declare(queue=self.robo)
        self.channel.basic_consume(self.trata_msg_recebida,
                                   queue=self.robo,
                                   no_ack=True)
        self.channel.queue_bind(exchange='SA_to_SS', queue=self.robo)
        self.jogador = ''

    def trata_msg_recebida(self, ch, method, properties, body):
        try:
            msg = json.loads(body)
        except:
            return

        print("RECEBENDO DO SA")
        # Identificador (indica que a msg veio do SS)
        msg['_dir'] = 'sa'

        with compartilhados.sw_lock:
            # Copia a mensagem para o buffer de transmissao
            foo = deepcopy(msg)
            if 'jogadorA' in msg:

                if msg['jogadorA'] == self.robo:
                    foo = {'_dir': 'sa', 'cmd': 1100, 'modo_jogo': msg['modo_jogo'],
                           'cacas': msg['cacas'], 'x': msg['xA'], 'y': msg['yA']}

                elif msg['jogadorB'] == self.robo:
                    foo = {'_dir': 'sa', 'cmd': 1100, 'modo_jogo': msg['modo_jogo'],
                           'cacas': msg['cacas'], 'x': msg['xB'], 'y': msg['yB']}

                with compartilhados.sacomrx:
                    compartilhados.sw_msg = deepcopy(foo)
                    # Chama o gerente
                    compartilhados.sw_event.set()
                    # Tempo de seguranca para o gerente pegar a msg
                    time.sleep(0.2)

            elif msg['robo'] == self.jogador:

                with compartilhados.sacomrx:
                    compartilhados.sw_msg = deepcopy(msg)
                    # Chama o gerente
                    compartilhados.sw_event.set()
                    # Tempo de seguranca para o gerente pegar a msg
                    time.sleep(0.2)

            compartilhados.sw_event.clear()

    def run(self):
        self.channel.start_consuming()
