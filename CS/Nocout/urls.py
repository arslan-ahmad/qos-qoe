from django.conf.urls import patterns, url, include
from Nocout import views


urlpatterns = patterns('',
	url(r'^Nocout/$', views.index, name='index'),
	url(r'^Nocout/probe',views.probes, name='probes'),
	url(r'^Nocout/Probes_details',views.Probe_details,name='Probe_details'),
	url(r'^Nocout/Inventory',views.Inventory,name='Inventory'),
	url(r'^Nocout/registration',views.registration,name='registration'),
	url(r'^Nocout/Probe_services_details',views.Probe_services_details,name='Probe_services_details'))
