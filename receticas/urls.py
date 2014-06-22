from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView, DetailView

from views import RecetaListView
from views import RecetaDisplayView
from views import RecetaCreate, RecetaUpdate, RecetaDelete

from models import Receta

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'receticas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/rece/'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'auth.views.login_user'),
    url(r'^home/$', 'receticas.views.home'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^rece/', 'receticas.views.index'),
    url(r'^recetas/(?P<pk>\d+)/$', DetailView.as_view(#-(?P<slug>[-\w]+)
	context_object_name="receta",
	model=Receta,
	#paginate_by = '5',
	template_name= "recetas/receta.html",
	), name="receta"),
    url(r'^recetas/', RecetaListView.as_view(
	context_object_name="receta",
	model=Receta,
	template_name= "recetas/lista-recetas.html",
	), name="recetas"),
    url(r'recet/add/$', RecetaCreate.as_view(), name='receta_add'),
    url(r'recet/(?P<pk>\d+)/$', RecetaUpdate.as_view(), name='receta_update'),
    url(r'recet/(?P<pk>\d+)/delete/$', RecetaDelete.as_view(), name='receta_delete'),



)
