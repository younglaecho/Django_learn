"""fc_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from fcuser.views import index, RegisterView, LoginView, logout
from product.views import (
    ProductList, ProductCreate, ProductDetail,
    ProductListAPI
)
from order.views import OrderCreate, OrderList # OrderFail
from imageUp.views import PostView
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('summernote/', include('django_summernote.urls')),
    path('register/', RegisterView.as_view()), # class를 사용하여 뷰를 만든 경우 as_view 메소드를 사용해야한다.
    path('login/', LoginView.as_view()),
    path('logout/', logout),
    path('product/', ProductList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('product/create/', ProductCreate.as_view()),
    path('order/',OrderList.as_view()),
    path('order/create/',OrderCreate.as_view()),
    # path('order/fail/', OrderFail.as_view()),
    path('imageUp/', PostView.as_view() ),

    path('api/product/',ProductListAPI.as_view() )
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

