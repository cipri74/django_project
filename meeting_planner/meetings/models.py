from datetime import time
from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    floor_nr = models.IntegerField()
    room_nr = models.IntegerField()

    def __str__(self):
        return f"{self.name} at floor: {self.floor_nr} in room: {self.room_nr}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        # nr_hours =
        return f"<{self.title}> at {self.start_time} on {self.date}, " \
               f"duration: {self.duration} {'hours' if int(self.duration) > 1 else 'hour'}, " \
               f"in {self.room}."
