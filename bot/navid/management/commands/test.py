import logging, pytz, datetime

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)
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

        brokers = Broker.objects.all()
        sources = []
        for broker in brokers:
            for source in broker.source_channels.all():
                sources.append(source.username)

        client.start()

        @client.on(events.NewMessage(incoming=True, chats=sources))
        async def my_event_handler(event):
            chat = await event.get_chat()
            sender = await event.get_sender()
            for broker in brokers:
                for source in broker.source_channels.all():
                    if source.username == sender.username:
                        print(f"broker name is: {broker.name}")
                        print(f"source channel name is: {source.username}")
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
