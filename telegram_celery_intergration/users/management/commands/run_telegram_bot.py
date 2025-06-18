import os
from django.core.management.base import BaseCommand
from users.telegram_bot import run_bot

class Command(BaseCommand):
    help = 'Runs the Telegram bot'

    def handle(self, *args, **options):
        # Set the bot token directly
        os.environ['TELEGRAM_BOT_TOKEN'] = '8118996850:AAG3A1DCwSL3bMZIRsN716j8Es_XMpOrXZM'
        
        self.stdout.write(self.style.SUCCESS('Starting Telegram bot...'))
        try:
            run_bot()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error running bot: {str(e)}')) 