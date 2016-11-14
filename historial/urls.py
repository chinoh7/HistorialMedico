from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.post_list),
        url(r'^consulta/nueva/$', views.consulta_nueva, name='consulta_nueva'),
    ]
