from django.shortcuts import render,redirect
from django.views.generic import FormView, TemplateView, ListView
from django.utils.decorators import method_decorator

from fcuser.decorator import login_required
from .forms import OrderForm
from .models import Order
from fcuser.models import Fcuser
from product.models import Product
from django.db import transaction


# Create your views here.

@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    form_class = OrderForm
    success_url = '/product/'

    def form_valid(self, form):
      with transaction.atomic():
        order = Order(
            quantity = form.data.get('quantity'),
            product = Product.objects.get(pk=form.data.get('product')),
            fcuser = Fcuser.objects.get(email=self.request.session.get('user')),
        )
        order.save()
        prod = Product.objects.get(pk=form.data.get('product'))
        prod.stock -= int(form.data.get('quantity'))
        prod.save()
      return super().form_valid(form)
    def form_invalid(self, form):
      return redirect('/product/' + str(form.data.get('product')))
      
    def get_form_kwargs(self, **kwargs): # 폼을 생성할 때 어떤 인자값을 전달할지 결정하는 함수
      kw = super().get_form_kwargs(**kwargs)
      kw.update({
        'request': self.request
      })
      return kw


@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order_list'
    
    def get_queryset(self):
      queryset = Order.objects.filter(fcuser__email=self.request.session.get('user'))
      return queryset

