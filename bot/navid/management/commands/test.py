import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
from asgiref.sync import sync_to_async

from django.utils import timezone
from django.core.management.base import BaseCommand
from telethon import TelegramClient, events, sync

from ...models import Broker

class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Bot started....')
        api_id = 1472324
        api_hash = 'afb6585ab2cc8d7fc34a0687c5c14f18'

        client = TelegramClient('navid', api_id, api_hash)

        @sync_to_async
        def get_all_users():
            bot = Broker.objects.first()
            return bot.source_channels.all()


        brokers = Broker.objects.all()
        @client.on(events.NewMessage(incoming=True))
        async def my_event_handler(event):
            chat = await event.get_chat()
            sender = await event.get_sender()
            for broker in brokers:
                for source in broker.source_channels.all():
                    if source.username == sender.username:
                        print('')
                        print('broker name is: {}'.format(broker.name))
                        print('source cahnnel name is: {}'.format(source.username))
                        for dest in broker.destination_channels.all():
                            if source.username == dest.username:
                                continue
                            try:
                                print('msg forw to dest cahnnel: {} at time: {}'.format(dest.username, timezone.now()))
                                await event.forward_to(dest.username)
                            except:
                                print('error, dest channel is: {}'.format(dest.username))
                                pass

        client.start()
        client.run_until_disconnected()

