import Pyro4
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare('start')

def callback(ch, method, properties, body):
    srcom = Pyro4.Proxy(body.decode())

    print(srcom.getPosInicial())

    k = input("atualiza coord")

    print(srcom.getPosInicial())

channel.basic_consume(callback,
                      queue='start',
                      no_ack=True)

channel.start_consuming()

