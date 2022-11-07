import logging, pytz, datetime

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)
from asgiref.sync import sync_to_async

from django.utils import timezone
from django.core.management.base import BaseCommand
from telethon import TelegramClient, events, sync

from ...models import Broker


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Bot started....")
        tz = pytz.timezone("Asia/Tehran")

        api_id = 1472324
        api_hash = "afb6585ab2cc8d7fc34a0687c5c14f18"
        client = TelegramClient("navid", api_id, api_hash)

        # api_id = 1446710
        # api_hash = '58a91c8d8d9704beb534a5327d0c25c8'
        # client = TelegramClient('mobina3', api_id, api_hash)
        # client.connect()
        # client.send_code_request('00989357518003')
        # client.sign_in('00989357518003', 19559)

        brokers = Broker.objects.all()
        sources = []
        for broker in brokers:
            for source in broker.source_channels.all():
                sources.append(source.username)
        print(sources)

        client.start()

        @client.on(events.NewMessage(incoming=True, chats=sources))
        async def my_event_handler(event):
            chat = await event.get_chat()
            sender = await event.get_sender()
            for broker in brokers:
                for source in broker.source_channels.all():
                    if source.username == sender.username:
                        print()
                        print("broker name is: {}".format(broker.name))
                        print("source cahnnel name is: {}".format(source.username))
                        for dest in broker.destination_channels.all():
                            if source.username == dest.username:
                                continue
                            try:
                                print(
                                    f"msg forw to dest cahnnel: {dest.username} at time: {datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')}"
                                )
                                await event.forward_to(dest.username)
                            except:
                                print(f"error, dest channel is: {dest.username}")
                                pass

        client.run_until_disconnected()
