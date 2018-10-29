import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='saTOss')

channel.basic_publish(exchange='', routing_key='saTOss', body="SA")