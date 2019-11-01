from django.contrib.postgres.fields import JSONField

from django.db import models


class Event(models.Model):
    ACTION_EVENT_TYPE= "action_event"
    INCIDENT_EVENT_TYPE = "incident_event"

    timestamp = models.DateTimeField()
    event_type = models.CharField(max_length=50)
    payload = JSONField()
