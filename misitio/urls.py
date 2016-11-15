from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

#from historial.views import RegistroUsuario
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    # Examples:
    # url(r'^$', 'misitio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('historial.urls')),

]+ static(settings.MEDIA_URL, docment_root=settings.MEDIA_ROOT) #comentar esto cuando Debug=False
