from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.example_view, name='example'),
    path('variable/', views.variable_view, name='variable'),
]

handler404 = 'jose_site.views.my_custom_page_not_found_view'
