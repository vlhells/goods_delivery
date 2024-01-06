from django.db import models
import enum
from abc import ABC

class Item(models.Model):
    description = models.CharField(max_length=256)
    weight = models.FloatField
    length = models.FloatField
    width = models.FloatField
    height = models.FloatField

class Human(models.Model, ABC):
    first_name = models.CharField(max_length=25)
    second_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=16)

class ItemSender(Human):
    pass

class Courier(Human):
    pass

class ItemReceiver(Human):
    pass

class Order(models.Model):
    state = models.CharField(max_length=25)
    meeting_time = models.DateTimeField
    meeting_place = models.CharField(max_length=85)
    target_address = models.CharField(max_length=85)
    cancellation_comment = models.CharField(max_length=256)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    item_sender = models.ForeignKey(ItemSender, on_delete = models.DO_NOTHING)
    courier = models.ForeignKey(Courier, on_delete = models.DO_NOTHING)
    item_receiver = models.ForeignKey(ItemReceiver, on_delete = models.DO_NOTHING)

class OrderStates(enum.Enum):
    new = 'Новая'
    in_process = 'Передана на выполнение'
    cancelled = 'Отменена'
    done = 'Выполнена'
