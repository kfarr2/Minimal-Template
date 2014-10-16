from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from mintemplate.home import views as home

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mintemplate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home.home, name='home'),
)
