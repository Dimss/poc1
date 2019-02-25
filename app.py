#!/usr/bin/env python
import pika
import json
import requests
import logging
import sys
import conf
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host=conf.RABBITMQ_IP))
channel = connection.channel()
channel.queue_declare(queue=conf.RABBITMQ_QUEUE)


def publish_message(message):
    channel.basic_publish(exchange='', routing_key=conf.RABBITMQ_QUEUE, body=message)
    logging.info("published row = {0}".format(message))


def main():
    data = requests.get(conf.SITES_LIST).json()
    for row in data:
        serialized = json.dumps(row)
        publish_message(serialized)

    logging.info(" [x] Queue initialized")
    connection.close()
    while True:
        logging.info(" [x] Gonna sleep forever cuz I don't know what to do now")
        time.sleep(10)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s %(levelname)s] %(message)s',
        stream=sys.stdout
    )
    main()
