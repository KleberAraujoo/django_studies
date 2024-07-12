from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list' ),
    path('porta',views.porta), # Com aspas vazia '' entramos na parte inicial do site
    path('sala', views.sala), # Com aspas preenchida entramos no site juntamente com a /sala
    path('quarto', views.quarto) # Mesma coisa nesta linha
]