from django.conf.urls import url
from . import views

app_name = 'pictures'

urlpatterns = [
    url(r'^pictures/', views.index, name='index')
]

