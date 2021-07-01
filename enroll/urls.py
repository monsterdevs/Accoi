from django.urls import path
from . import views

urlpatterns = [
    # path('showformdata/',views.showformdata),
    path('showformdetails/',views.showformdetails),
    # path('showlogs/',viewa.showlogs)
    path('analyze',views.analyze,name='analyze'),
    path('progress/',views.analyze)
]y