#!/usr/bin/env python
import pika
import json
import requests

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq.check-sites.svc.cluster.local'))
channel = connection.channel()

channel.queue_declare(queue='sites')

data = json.loads(requests.get('https://raw.githubusercontent.com/abarlev/poc1/master/SiteList.json').text)

for row in data:
    serialized = json.dumps(row)
    channel.basic_publish(exchange='', routing_key='sites', body=serialized)
    print("published row = {0}".format(serialized))

print(" [x] Queue initialized")
connection.close()
