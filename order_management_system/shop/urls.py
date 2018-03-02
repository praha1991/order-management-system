from . import views
from django.conf.urls import url

app_name = 'shop'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /item/4/
    url(r'^item/$', views.ItemView.as_view(), name='item'),
    # ex: /cart/5/
    url(r'^cart/$', views.CartView.as_view(), name='cart')
]