"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('home/',views.home,name="home"),
    path('main/',views.main,name="main"),
    path('login/', views.login_call,name="login_call"),
    path('logout/', views.logout_call,name="logout_call"),
    path('signup/', views.signup,name="signup"),
    path('productdetail/<id>', views.productdetail,name="productdetail"),
    path('testimonial/', views.testimonial,name="testimonial"),
    path('about/', views.about,name="about"),
    path('add_to_cart/<pid>', views.add_to_cart,name="add_to_cart"),
    path('checkout/', views.checkout,name="checkout"),
    path('viewcart/',views.viewcart,name="viewcart"),
    path('blog_list/', views.blog_list,name="blog_list"),
    path('contact/', views.contact,name="contact"),
    path('products/', views.products,name="products"),
    path('placeorder/', views.placeorder,name="placeorder"),
    
    path('editcart/<id>', views.editcart,name="products"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



