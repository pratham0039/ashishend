from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('add_product/', views.add_product, name='add_product'),
    path('product_list/', views.product_list, name='product_list'),
    path('pay_option/<int:record_id>/', views.pay_option, name='pay_option'),
    path('pay_option2/<int:record_id>/', views.pay_option2, name='pay_option2'),
    path('udhaar/', views.udhaar, name='udhaar'),
    path('labs/', views.labs_list, name='labs_list'),
    path('search/', views.search_records, name='search_records'),
    path('lab/<str:lab>/', views.lab_records, name='lab_records'),
    path('generate_pdf/<str:month>/<str:lab>/', views.generate_pdf, name='generate_pdf'),
    path('add_deposit/<str:lab>', views.add_deposit, name = 'add_deposit')

]