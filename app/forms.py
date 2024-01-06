from django import forms
from .models import OrderStates

class CreateOrderForm(forms.Form):
    target_address = forms.CharField(required=True, label="Целевой адрес доставки:")
    meeting_place = forms.CharField(required=True, label="Место встречи с курьером:")
    meeting_time = forms.CharField(required=True, label="Время встречи с курьером:")
    item_description = forms.CharField(required=True, label="Описание груза:")
    item_weight = forms.FloatField(required=True, label="Вес груза:")
    item_length = forms.FloatField(required=True, label="Длина груза:")
    item_width = forms.FloatField(required=True, label="Ширина груза:")
    item_height = forms.FloatField(required=True, label="Высота груза:")
    item_sender_fname = forms.CharField(required=True, label="Имя отправителя:")
    item_sender_sname = forms.CharField(label="Отчество отправителя:")
    item_sender_lname = forms.CharField(required=True, label="Фамилия отправителя:")
    item_sender_phone_number = forms.CharField(required=True, label="Контактный номер отправителя:")
    item_receiver_fname = forms.CharField(required=True, label="Имя получателя:")
    item_receiver_sname = forms.CharField(label="Отчество получателя:")
    item_receiver_lname = forms.CharField(required=True, label="Фамилия получателя:")
    item_receiver_phone_number = forms.CharField(required=True, label="Контактный номер получателя:")

class EditOrderForm(forms.Form):
    target_address = forms.CharField(required=True, label="Целевой адрес доставки:")
    meeting_place = forms.CharField(required=True, label="Место встречи с курьером:")
    meeting_time = forms.CharField(required=True, label="Время встречи с курьером:")
    item_description = forms.CharField(required=True, label="Описание груза:")
    item_weight = forms.FloatField(required=True, label="Вес груза:")
    item_length = forms.FloatField(required=True, label="Длина груза:")
    item_width = forms.FloatField(required=True, label="Ширина груза:")
    item_height = forms.FloatField(required=True, label="Высота груза:")
    item_sender_fname = forms.CharField(required=True, label="Имя отправителя:")
    item_sender_sname = forms.CharField(label="Отчество отправителя:")
    item_sender_lname = forms.CharField(required=True, label="Фамилия отправителя:")
    item_sender_phone_number = forms.CharField(required=True, label="Контактный номер отправителя:")
    item_receiver_fname = forms.CharField(required=True, label="Имя получателя:")
    item_receiver_sname = forms.CharField(label="Отчество получателя:")
    item_receiver_lname = forms.CharField(required=True, label="Фамилия получателя:")
    item_receiver_phone_number = forms.CharField(required=True, label="Контактный номер получателя:")

class ChangeOrderStateForm(forms.Form):
    def __init__(self, available_order_states):
        self.available_order_states = available_order_states

    order_states = forms.ChoiceField(self.available_order_states, required=True)
    # TODO: Исключить состояния inProcess и done в зав. от того, выбран ли курьер.
    # filter(lambda s: s.value != OrderStates.in_process.value, OrderStates)
    cancellation_comment = forms.CharField()

class CourierForm(forms.Form):
    first_name = forms.CharField(required=True, label="Имя курьера:")
    second_name = forms.CharField(label="Отчество курьера:")
    last_name = forms.CharField(required=True, label="Фамилия курьера:")
    phone_number = forms.CharField(required=True, label="Контактный номер курьера:")