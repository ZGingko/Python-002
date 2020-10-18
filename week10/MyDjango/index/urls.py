from django.urls import path, re_path, register_converter
from . import views, converters
import time

register_converter(converters.IntConverter, 'myint')
register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.index),
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),

    path('<int:year>', views.year),
    path('<int:year>/<str:name>', views.name),

    path('books', views.books),
    path('test1', views.test1),
    path('test2', views.test2)
]