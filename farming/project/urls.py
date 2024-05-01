from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name= 'home' ),
    path('ask', views.bot_reply, name= 'ask' ),
    path('reg', views.register, name= 'reg' ),
    path('log', views.log, name= 'log' ),
    path('out', views.user_logout, name= 'out' ),
]