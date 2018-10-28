import pika


class SSbind():

    def __init__(self, fila_sr, fila_sa):
        self.fila_sr = fila_sr
        self.fila_sa = fila_sa
        self.connection_sr = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel_sr = self.connection._srchannel()
        self.channel_sr.queue_declare(queue=fila_sr)

        self.fila_sa = fila_sa
        self.connection_sa = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel_sa = self.connection_sa.channel()
        self.channel_sa.queue_declare(queue=fila_sa)

    def enviarTosr(self, msg):
        self.channel_sr.basic_publish(exchange='',
                                   routing_key=self.fila_sr,
                                   body=msg)

    def enviarTosa(self, msg):
        self.channel_sa.basic_publish(exchange='',
                                   routing_key=self.fila_sa,
                                   body=msg)

    def encerraSr(self):
        self.connection_sr.close()

    def encerraSa(self):
        self.connection_sa.close()