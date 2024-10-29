from django.urls import path

from base import views

urlpatterns = [
    path('login/',views.LoginView.as_view(),name='login'),
    path('data/',views.DataView.as_view(),name='data'),
    path('dataInfo/',views.DataInfoView.as_view(),name='dataInfo'),
    path('img/',views.ImgView.as_view(),name='img'),
]