from django import forms
from .models import OrderStates

class CreateOrderForm(forms.Form):
    target_address = forms.CharField()
    meeting_place = forms.CharField()
    meeting_time = forms.CharField()
    description = forms.CharField()
    weight = forms.FloatField
    length = forms.FloatField
    width = forms.FloatField
    height = forms.FloatField
    item_sender_fname = forms.CharField()
    item_sender_sname = forms.CharField()
    item_sender_lname = forms.CharField()
    item_receiver_fname = forms.CharField()
    item_receiver_sname = forms.CharField()
    item_receiver_lname = forms.CharField()

class EditOrderForm(forms.Form):
    target_address = forms.CharField()
    meeting_place = forms.CharField()
    meeting_time = forms.CharField()
    description = forms.CharField()
    weight = forms.FloatField
    length = forms.FloatField
    width = forms.FloatField
    height = forms.FloatField
    item_sender_fname = forms.CharField()
    item_sender_sname = forms.CharField()
    item_sender_lname = forms.CharField()
    courier_fname = forms.CharField()
    courier_sname = forms.CharField()
    courier_lname = forms.CharField()
    item_receiver_fname = forms.CharField()
    item_receiver_sname = forms.CharField()
    item_receiver_lname = forms.CharField()

class ChangeOrderStateForm(forms.Form):
    order_state = forms.ChoiceField(choices=OrderStates)
    # Исключить состояния inProcess и done в зав. от.
    cancellation_comment = forms.CharField()

class CourierForm(forms.Form):
    first_name = forms.CharField()
    second_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()