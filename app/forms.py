from django import forms
from .models import OrderStates

class CreateOrderForm(forms.Form):
    target_address = forms.CharField(required=True)
    meeting_place = forms.CharField(required=True)
    meeting_time = forms.CharField(required=True)
    description = forms.CharField(required=True)
    weight = forms.FloatField(required=True)
    length = forms.FloatField(required=True)
    width = forms.FloatField(required=True)
    height = forms.FloatField(required=True)
    item_sender_fname = forms.CharField(required=True)
    item_sender_sname = forms.CharField()
    item_sender_lname = forms.CharField(required=True)
    item_receiver_fname = forms.CharField(required=True)
    item_receiver_sname = forms.CharField()
    item_receiver_lname = forms.CharField(required=True)

class EditOrderForm(forms.Form):
    target_address = forms.CharField(required=True)
    meeting_place = forms.CharField(required=True)
    meeting_time = forms.CharField(required=True)
    description = forms.CharField(required=True)
    weight = forms.FloatField(required=True)
    length = forms.FloatField(required=True)
    width = forms.FloatField(required=True)
    height = forms.FloatField(required=True)
    item_sender_fname = forms.CharField(required=True)
    item_sender_sname = forms.CharField()
    item_sender_lname = forms.CharField(required=True)
    courier_fname = forms.CharField(required=True)
    courier_sname = forms.CharField()
    courier_lname = forms.CharField(required=True)
    item_receiver_fname = forms.CharField(required=True)
    item_receiver_sname = forms.CharField()
    item_receiver_lname = forms.CharField(required=True)

class ChangeOrderStateForm(forms.Form):
    order_state = forms.ChoiceField(choices=OrderStates, required=True)
    # Исключить состояния inProcess и done в зав. от.
    cancellation_comment = forms.CharField()

class CourierForm(forms.Form):
    first_name = forms.CharField(required=True)
    second_name = forms.CharField()
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)