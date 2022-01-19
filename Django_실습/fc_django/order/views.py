from django.shortcuts import render,redirect
from django.views.generic import FormView, TemplateView, ListView
from django.utils.decorators import method_decorator

from fcuser.decorator import login_required
from .forms import OrderForm
from .models import Order


# Create your views here.

@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    form_class = OrderForm
    success_url = '/product/'

    def form_invalid(self, form):
      return redirect('/product/' + str(form.product))
      
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

