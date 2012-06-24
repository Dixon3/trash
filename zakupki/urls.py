from django.conf.urls.defaults import patterns, include, url
from zakupki.contracts.models import *
from zakupki.contracts.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^contracts/$', ContractsListView.as_view()),
    (r'^contracts/(?P<pk>\w+)$', ContractsDetailView.as_view()),
    (r'^contracts/(?P<order_uid>\w+)/contractssuppliers$',ContractsSuppliersDetailView.as_view()),
    # Examples:
    # url(r'^$', 'zakupki.views.home', name='home'),
    # url(r'^zakupki/', include('zakupki.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
