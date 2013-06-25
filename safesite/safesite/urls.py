from django.conf.urls import patterns, include, url
from accounts import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'safesite.views.home', name='home'),
    # url(r'^safesite/', include('safesite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^home/',views.home ),
     url(r'^login/',views.login),
      url(r'^register/',views.register),
      url(r'auth/',views.auth),
      url(r'^account/',views.user_manage),
       url(r'^delete/',views.delete_user),
)
