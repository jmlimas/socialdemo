from django.conf.urls import patterns, include, url
from principal.views import IndexAboutView, Privado, Cerrar
from django.contrib import admin
from django.contrib.auth.decorators import login_required

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexAboutView.as_view()),
    url('',include('social.apps.django_app.urls', namespace='social')),
    url(r'^privado/$',login_required(Privado.as_view()),name='privado'),
    url(r'^cerrar/$', login_required(Cerrar.as_view()),name='cerrar'),
)