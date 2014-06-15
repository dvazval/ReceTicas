from django.conf.urls import patterns, include, url

from django.contrib import admin
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
   
)
