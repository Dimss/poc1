#!/usr/bin/env python
import pika
import json
import requests

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq.check-sites.svc.cluster.local'))
channel = connection.channel()

print("NEW VERSION!!! serialized the json payload")

channel.queue_declare(queue='hello')

data = json.loads(requests.get('https://raw.githubusercontent.com/abarlev/poc1/master/SiteList.json').text)

for i in range(100):
    print("published data[{0}] = {1}".format(i, data[i]))
    serialized=json.dumps(data[i])
    channel.basic_publish(exchange='', routing_key='hello', body=serialized))
    print("published data[{0}] = {1}".format(i, body))

#channel.basic_publish(exchange='', routing_key='hello', body="https://www.google.com")
#channel.basic_publish(exchange='', routing_key='hello', body="https://www.cnn.com")
#channel.basic_publish(exchange='', routing_key='hello', body="https://www.ynet.co.il")

#channel.basic_publish(exchange='', routing_key='hello', body="https://www.gov.il")
#channel.basic_publish(exchange='', routing_key='hello', body="https://www.pmo.gov.il")
#channel.basic_publish(exchange='', routing_key='hello', body="https://www.police.gov.il")
#channel.basic_publish(exchange='', routing_key='hello', body="https://www.president.gov.il")
#channel.basic_publish(exchange='', routing_key='hello', body="https://www.shabak.gov.il")
#channel.basic_publish(exchange='', routing_key='hello', body="https://www.mossad.gov.il")

print(" [x] Queue initialized")
connection.close()
