from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Order, Courier
from django.views import View
from .services import OrdersService, CouriersService

class OrdersView(View):
    # template_name = 'author_list.html'

    def index(self, request):
        orders = OrdersService.get_all_orders()
        return render(request, self.template_name, {'orders': orders})
    
    def create_get(self, request):
        return render(request, self.template_name)
    
    def create_post(self, request):
        pass