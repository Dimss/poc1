#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq.check-sites.svc.cluster.local'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body="https://www.gov.il,10")
channel.basic_publish(exchange='', routing_key='hello', body="https://www.pmo.gov.il,10]")
channel.basic_publish(exchange='', routing_key='hello', body="https://www.police.gov.il,10]")
channel.basic_publish(exchange='', routing_key='hello', body="https://www.president.gov.il,10]")
channel.basic_publish(exchange='', routing_key='hello', body="https://www.shabak.gov.il,10]")
channel.basic_publish(exchange='', routing_key='hello', body="https://www.mossad.gov.il,10]")

print(" [x] Queue initialized")
connection.close()
