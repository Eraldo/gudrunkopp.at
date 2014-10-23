from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gudrunkoppat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^backend/', include(admin.site.urls)),
    url(r'^goddess/', include(admin.site.urls)),
    url(r'', include('pages.urls', namespace="pages")),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
