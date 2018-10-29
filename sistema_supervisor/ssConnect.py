import pika

class SSconnect():

    def __init__(self, fila_sr, fila_sa):
        self.fila_sr = fila_sr
        self.fila_sa = fila_sa
        self.connection_sr = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel_sr = self.connection_sr.channel()
        self.channel_sr.queue_declare(queue=fila_sr)

        self.connection_sa = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel_sa = self.connection_sr.channel()
        self.channel_sa.queue_declare(queue=fila_sa)



    def callback(ch, method, properties, body):
        body.decode()

    def callback_sa(ch, method, properties, body):
        return body.decode()

    def fila(self):
        self.channel_sr.basic_consume(self.callback,
                                      queue=self.fila_sr,
                                      no_ack=True)
        self.channel_sa.basic_consume(self.callback,
                                      queue=self.fila_sa,
                                      no_ack=True)

    def consuming_sr(self):
        self.channel_sr.start_consuming()

    def consuming_sa(self):
        self.channel_sa.start_consuming()
