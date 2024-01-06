from .models import Order, Courier, OrderStates

class OrdersService:
    order_not_found = "Order not found in base."
    incorrect_data = "Incorrect data"

    @staticmethod
    def get_all_orders():
        orders = Order.objects.all()
        return orders

    @staticmethod
    def create(new_order):
        if new_order != None:
            order = Order()
            order.state = OrderStates.new.value
            order.target_address = new_order.target_address
            order.meeting_place = new_order.meeting_place
            order.meeting_time = new_order.meeting_time
            order.item = new_order.item
            order.item_sender = new_order.item_sender
            order.courier = new_order.courier
            order.item_receiver = new_order.item_receiver
            order.save()
            return "Successfully created new order!"
        return OrdersService.incorrect_data
    
    @staticmethod
    def get_order_by_id(id):
        try:
            order = Order.objects.get(id=id)
            if (order.state is OrderStates.new.value):
                return order
        except Order.DoesNotExist:
            return OrdersService.order_not_found
        
    @staticmethod
    def edit_post_async(updated_order):
        try:
            Order.objects.filter(id=updated_order.id).aupdate(target_address = updated_order.target_address,
                                                              meeting_place = updated_order.meeting_place,
                                                              meeting_time = updated_order.meeting_time,
                                                              item = updated_order.item,
                                                              item_sender = updated_order.item_sender,
                                                              courier = updated_order.courier,
                                                              item_receiver = updated_order.item_receiver)
        except Order.DoesNotExist:
            return OrdersService.order_not_found
        
    @staticmethod
    def delete_async(id):
        try:
            Order.objects.filter(id=id).adelete()
            return f"Successfully deleted order N{id}"
        except Order.DoesNotExist:
            return OrdersService.order_not_found

class CouriersService:
    courier_not_found = "Courier not found in base."

    @staticmethod
    def get_all_couriers():
        couriers = Courier.objects.all()
        return couriers

    @staticmethod
    def create(new_courier):
        if new_courier != None:
            courier = new_courier
            courier.first_name = new_courier.first_name
            courier.second_name = new_courier.second_name
            courier.last_name = new_courier.last_name
            courier.phone_number = new_courier.phone_number
            courier.save()
            return "Successfully added new courier!"
        return CouriersService.incorrect_data
            
    @staticmethod
    def get_courier_by_id(id):
        try:
            courier = Courier.objects.get(id=id)
            return courier
        except Courier.DoesNotExist:
            return CouriersService.courier_not_found
    
    @staticmethod
    def edit_post_async(updated_courier):
        try:
            Courier.objects.filter(id=updated_courier.id).aupdate(first_name = updated_courier.first_name, 
                                                                 second_name = updated_courier.second_name,
                                                                 last_name = updated_courier.last_name,
                                                                 phone_number = updated_courier.phone_number)
        except Courier.DoesNotExist:
            return CouriersService.courier_not_found
        
    @staticmethod
    def delete_async(id):
        try:
            Courier.objects.filter(id=id).adelete()
            return f"Successfully deleted courier N{id}"
        except Courier.DoesNotExist:
            return CouriersService.courier_not_found
