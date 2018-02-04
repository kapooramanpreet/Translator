from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^x1', hello.views.x1, name='x1'),
    url(r'^x2', hello.views.x2, name='x2'),
    url(r'^x', hello.views.x, name='x'),
    path('admin/', admin.site.urls),
]
