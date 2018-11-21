import pika
import json
from threading import Thread, Event, Lock
import compartilhados


class SAcomTX(Thread):

    def __init__(self, host):
        super(SAcomTX, self).__init__()

        credentials = pika.PlainCredentials('robot1', 'robot1')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host, 5672, '/', credentials))
        self.channel = conexao.channel()
        self.channel.queue_declare(queue='SS_to_SA')

    def run(self):
        while True:
            # Espera ate ter uma mensagem a transmitir
            compartilhados.enviar_sa_event.wait()

            # Bloqueia enquanto a mensagem e enviada
            with compartilhados.sa_lock:
                msg = compartilhados.transmitir_msg

                if '_dir' in msg: msg.pop('_dir')

                if '_sa' in msg:
                    routing_key = msg['_sa']
                    msg.pop('_sa')

                    try:
                        msg = json.dumps(msg)
                        self.channel.basic_publish(exchange='',
                                                   routing_key='SS_to_SA',
                                                   body=msg,
                                                   properties=msg_prop)
                    except:
                        pass

                compartilhados.enviar_sa_event.clear()

            self.connection.close()