#!/usr/bin/env python
import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq.check-sites.svc.cluster.local'))
channel = connection.channel()

channel.queue_declare(queue='hello')

with open('SiteList.json') as f:
    data = json.load(f)

for i in range(10):
    channel.basic_publish(exchange='', routing_key='hello', body=data[i])
    print("published data[{0}] = {1}".format(i, data[i]))

channel.basic_publish(exchange='', routing_key='hello', body="https://www.google.com")
channel.basic_publish(exchange='', routing_key='hello', body="https://www.cnn.com")
channel.basic_publish(exchange='', routing_key='hello', body="https://www.ynet.co.il")

channel.basic_publish(exchange='', routing_key='hello', body="https://www.gov.il")
channel.basic_publish(exchange='', routing_key='hello', body="https://www.pmo.gov.il")
channel.basic_publish(exchange='', routing_key='hello', body="https://www.police.gov.il")
channel.basic_publish(exchange='', routing_key='hello', body="https://www.president.gov.il")
channel.basic_publish(exchange='', routing_key='hello', body="https://www.shabak.gov.il")
channel.basic_publish(exchange='', routing_key='hello', body="https://www.mossad.gov.il")

print(" [x] Queue initialized")
connection.close()
