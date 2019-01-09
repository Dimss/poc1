#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq.check-sites.svc.cluster.local'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body="https://www.gov.il")
channel.basic_publish(exchange='', routing_key='hello', body="https://www.pmo.gov.il")
channel.basic_publish(exchange='', routing_key='hello', body="https://www.police.gov.il")
channel.basic_publish(exchange='', routing_key='hello', body="https://www.president.gov.il")
channel.basic_publish(exchange='', routing_key='hello', body="https://www.shabak.gov.il")
channel.basic_publish(exchange='', routing_key='hello', body="https://www.mossad.gov.il")

print(" [x] Queue initialized")
connection.close()