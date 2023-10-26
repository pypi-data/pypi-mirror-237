from event_people.config import Config

class Listener:
    @staticmethod
    def on(event_name, callback = None):
        broker_callback = callback if callback else Listener.basic_callback
        queue_names = [event_name]
        broker = Config.get_broker()
        channel = broker.get_connection()

        if len(event_name.split('.')) == 3:
            queue_names = [f'{event_name}.all', f'{event_name}.{Config.APP_NAME}']

        for queue_name in queue_names:
            broker.consume(queue_name, broker_callback, False)

        try:
            channel.start_consuming()
        except KeyboardInterrupt:#pragma: no cover
            channel.stop_consuming()#pragma: no cover

    def basic_callback(event, context):
        print(event.name)#pragma: no cover
        print(event.header)#pragma: no cover
        print(event.body)#pragma: no cover
        context.success()#pragma: no cover

