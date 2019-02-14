import unittest
import json
import app
import requests
import HtmlTestRunner


class TestSendReceiveQueueMessages(unittest.TestCase):

    def test_fetch_sites_list(self):
        try:
            data = requests.get(app.conf.SITES_LIST).json()
        except Exception as ex:
            self.fail(ex)
        self.assertIsInstance(data, list)
        self.assertIsNot(0, len(data))

    def test_sent_receive_message_to_queue(self):
        data = requests.get(app.conf.SITES_LIST).json()
        test_message = data[0]
        app.publish_message(json.dumps(test_message))
        app.channel.basic_consume(self._msg_receive_callback, queue=app.conf.RABBITMQ_QUEUE, no_ack=True)
        app.channel.start_consuming()

    def test_failure_example(self):
        self.assertEqual(0, 1)

    def _msg_receive_callback(self, ch, method, properties, body):
        app.channel.stop_consuming()
        data = requests.get(app.conf.SITES_LIST).json()
        test_message = data[0]
        body = json.loads(body.decode())
        self.assertEqual(body, test_message)


if __name__ == '__main__':
    print("This is main")
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=''))
