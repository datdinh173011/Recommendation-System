import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

# RabbitMQ not to give more than one message to a worker at a time. 
# Instead, it will dispatch it to the next worker that is not still busy
channel.basic_qos(prefetch_count=1) 
# the task_queue won't be lost even if RabbitMQ restarts
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()