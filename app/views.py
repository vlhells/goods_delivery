from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from .models import Order, Item, ItemSender, Courier, ItemReceiver
from django.views import View
from .services import OrdersService, CouriersService
from .forms import *

class OrdersView(View):
    # template_name = 'author_list.html'

    @staticmethod
    def check_answer_type(server_answer):
        if 'not' in server_answer:
            return HttpResponseNotFound(server_answer)
        return HttpResponse(server_answer)
    
    @staticmethod
    def return_invalid_data_answer():
        return HttpResponseBadRequest("Invalid data")

    def index(self, request):
        orders = OrdersService.get_all_orders()
        return render(request, self.template_name, {'orders': orders})
    
    def create_get(self, request):
        create_order_form = CreateOrderForm()
        return render(request, "create.html", {"form": create_order_form})
    
    @staticmethod
    def create_post(request):
        create_order_form = CreateOrderForm(request.POST)
        if create_order_form.is_valid():
            new_order = Order(
                state = OrderStates.new.value,
                meeting_time=create_order_form.cleaned_data['meeting_time'],
                meeting_place=create_order_form.cleaned_data['meeting_place'],
                target_address=create_order_form.cleaned_data['target_address'],
                item=Item(description = create_order_form.cleaned_data['item_description'],
                          weight = create_order_form.cleaned_data['item_weight'],
                          length = create_order_form.cleaned_data['length'],
                          width= create_order_form.cleaned_data['item_width'],
                          height = create_order_form.cleaned_data['item_height']
                          ),
                item_sender = ItemSender(first_name = create_order_form.cleaned_data['item_sender_fname'],
                                         second_name = create_order_form.cleaned_data['item_sender_sname'],
                                         last_name = create_order_form.cleaned_data['item_sender_lname'],
                                         phone_number = create_order_form.cleaned_data['item_sender_phone_number']),
                item_receiver = ItemReceiver(first_name = create_order_form.cleaned_data['item_receiver_fname'],
                                             second_name = create_order_form.cleaned_data['item_receiver_sname'],
                                             last_name = create_order_form.cleaned_data['item_receiver_lname'],
                                             phone_number = create_order_form.cleaned_data['item_receiver_phone_number'])
            )

            server_answer = OrdersService.create(new_order)
            return OrdersView.check_answer_type(server_answer)
        else:
            return OrdersView.return_invalid_data_answer()
    
    @staticmethod
    def edit_get(request, order_id):
        edit_order_form = EditOrderForm()
        target_order = OrdersService.get_order_by_id(order_id)
        return render(request, "edit.html", {"form": edit_order_form, "order_data": target_order})
    
    @staticmethod
    def edit_post(request):
        edit_order_form = EditOrderForm(request.POST)
        if edit_order_form.is_valid():
            updated_order = Order(
                meeting_time=edit_order_form.cleaned_data['meeting_time'],
                meeting_place=edit_order_form.cleaned_data['meeting_place'],
                target_address=edit_order_form.cleaned_data['target_address'],
                item=Item(description = edit_order_form.cleaned_data['item_description'],
                          weight = edit_order_form.cleaned_data['item_weight'],
                          length = edit_order_form.cleaned_data['length'],
                          width= edit_order_form.cleaned_data['item_width'],
                          height = edit_order_form.cleaned_data['item_height']
                          ),
                item_sender = ItemSender(first_name = edit_order_form.cleaned_data['item_sender_fname'],
                                         second_name = edit_order_form.cleaned_data['item_sender_sname'],
                                         last_name = edit_order_form.cleaned_data['item_sender_lname'],
                                         phone_number = edit_order_form.cleaned_data['item_sender_phone_number']),
                item_receiver = ItemReceiver(first_name = edit_order_form.cleaned_data['item_receiver_fname'],
                                             second_name = edit_order_form.cleaned_data['item_receiver_sname'],
                                             last_name = edit_order_form.cleaned_data['item_receiver_lname'],
                                             phone_number = edit_order_form.cleaned_data['item_receiver_phone_number'])
            )

            server_answer = OrdersService.edit_post_async(updated_order)
            return OrdersView.check_answer_type(server_answer)
        else:
            return OrdersView.return_invalid_data_answer()
    
    @staticmethod
    def delete_async(order_id):
        server_answer = OrdersService.delete_async(order_id)
        return OrdersView.check_answer_type(server_answer)

class CouriersView(View):
    def index(self, request):
        couriers = CouriersService.get_all_couriers()
        return render(request, self.template_name, {'couriers': couriers})
    
    def create_get(self, request):
        courier_form = CourierForm()
        return render(request, "create.html", {"form": courier_form})
    
    @staticmethod
    def create_post(request):
        courier_form = CourierForm(request.POST)
        if courier_form.is_valid():
            new_courier = Courier(
                first_name = courier_form.cleaned_data['first_name'],
                second_name = courier_form.cleaned_data['second_name'],
                last_name = courier_form.cleaned_data['last_name'],
                phone_number = courier_form.cleaned_data['phone_number']
            )

            server_answer = CouriersService.create(new_courier)
            return OrdersView.check_answer_type(server_answer)
        else:
            return OrdersView.return_invalid_data_answer()
    
    @staticmethod
    def edit_get(request, courier_id):
        courier_form = CourierForm()
        target_courier = CouriersService.get_courier_by_id(courier_id)
        return render(request, "edit.html", {"form": courier_form, "courier_data": target_courier})
    
    @staticmethod
    def edit_post(request):
        courier_form = CourierForm(request.POST)
        if courier_form.is_valid():
            updated_courier = Courier(
                first_name = courier_form.cleaned_data['first_name'],
                second_name = courier_form.cleaned_data['second_name'],
                last_name = courier_form.cleaned_data['last_name'],
                phone_number = courier_form.cleaned_data['phone_number']
            )

            server_answer = CouriersService.edit_post_async(updated_courier)
            return OrdersView.check_answer_type(server_answer)
        else:
            return OrdersView.return_invalid_data_answer()
    
    @staticmethod
    def delete_async(courier_id):
        server_answer = CouriersService.delete_async(courier_id)
        return OrdersView.check_answer_type(server_answer)
