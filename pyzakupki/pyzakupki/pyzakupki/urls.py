from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'customers.views.index', name='home'),
    url(r'^customers/(?P<customer_id>\d+)/$','customers.views.customer',name='customers'),
    url(r'^customers/(?P<customer_id>\d+)/contracts/$','customers.views.customer_contracts',name='customers_contracts'),
    url(r'^budget/(?P<budget_id>\d+)/$','customers.views.customers_bybudget',name='customers_bybudget'),
    url(r'^contr/(?P<contr_id>\d+)/$','contr.views.contr',name='customers.views.contr'),
    url(r'^obj/(?P<obj_type>\w+)/(?P<obj_id>\d+)/$','contr.views.object',name='obj_type_id'),
    url(r'^obj/(?P<obj_type>\w+)/(?P<column>\w+)/$','contr.views.search',name='search_obj_column'),
    url(r'^obj/(?P<obj_type>\w+)/(?P<column>\w+)/sear/$','contr.views.search_obj_by_child',name='search_obj_column_subobject')        
    #url(r'^pyzakupki/', include('customers.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
