from django.core.management.base import BaseCommand

from pretalx.submission.models import Submission
from pretalx.event.models import Event
from django_scopes import scope, scopes_disabled
from django.utils.timezone import now
from datetime import datetime, timezone, timedelta
import pytz

class Command(BaseCommand):
    help = "Set all time zones to Eastern"


    def handle(self, *args, **options):
        for event in Event.objects.all():        
            with scope(event=event):
                for talk in Submission.objects.all():
                    if talk.slots:
                        slot = talk.slots.last()
                        localtz=pytz.timezone('US/Eastern')
                        

                        if  slot.start:
                            slot.start= slot.start+ timedelta(hours=4)

                        if slot.end:
                            slot.end= slot.end+ timedelta(hours=4)
                            slot.real_end= slot.real_end+ timedelta(hours=4)

                            

                        slot.save()
                        # talk.save()
                        print(talk)

                    
                    # datetime.timezone.tzname.
