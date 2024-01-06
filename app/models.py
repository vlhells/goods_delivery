from django.db import models
import enum
from abc import ABC

class Item(models.Model):
    description = models.CharField(max_length=256, null=False)
    weight = models.FloatField(null=False)
    length = models.FloatField(null=False)
    width = models.FloatField(null=False)
    height = models.FloatField(null=False)

class Human(models.Model, ABC):
    first_name = models.CharField(max_length=25, null=False)
    second_name = models.CharField(max_length=60, null=True)
    last_name = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=16, null=False)

class ItemSender(Human):
    pass

class Courier(Human):
    pass

class ItemReceiver(Human):
    pass

class Order(models.Model):
    state = models.CharField(max_length=25, null=False)
    meeting_time = models.DateTimeField(null=False)
    meeting_place = models.CharField(max_length=85, null=False)
    target_address = models.CharField(max_length=85, null=False)
    cancellation_comment = models.CharField(max_length=256, null=True)
    item = models.ForeignKey(Item, on_delete = models.CASCADE, null=False)
    item_sender = models.ForeignKey(ItemSender, on_delete = models.DO_NOTHING, null=False)
    courier = models.ForeignKey(Courier, on_delete = models.DO_NOTHING, null=True)
    item_receiver = models.ForeignKey(ItemReceiver, on_delete = models.DO_NOTHING, null=False)

class OrderStates(enum.Enum):
    new = 'Новая'
    in_process = 'Передана на выполнение'
    cancelled = 'Отменена'
    done = 'Выполнена'
