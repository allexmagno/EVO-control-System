import pika
from threading import Thread

class ssConnect(Thread):

    def __init__(self, fila_sr, fila_sa):
        Thread.__init__(self)
        self.fila_sr = fila_sr
        self.fila_sa = fila_sa
        self.connection_sr = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel_sr = self.connection_sr.channel()
        self.channel_sr.queue_declare(queue=fila_sr)

        self.connection_sa = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel_sa = self.connection_sr.channel()
        self.channel_sa.queue_declare(queue=fila_sa)


    def callback_sr(ch, method, properties, body):
        return body.decode()

    def callback_sa(ch, method, properties, body):
        return body.decode()

    def fila(self):
        self.channel_sr.basic_consume(self.callback_sr,
                                      queue=self.fila_sr,
                                      no_ack=True)
        self.channel_sa.basic_consume(self.callback_sa,
                                      queue=self.fila_sa,
                                      no_ack=True)

    def run(self):
        self.channel_sr.start_consuming()
        self.channel_sa.start_consuming()
