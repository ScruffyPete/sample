from django.conf.urls import url, include
from django.contrib import admin

from sample import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^clients/', include('clients.urls'))
]

if 'debug_toolbar' in settings.INSTALLED_APPS and settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
