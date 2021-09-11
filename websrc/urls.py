"""websrc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),

    # index page
    url(r'^$', views.index, name='index'),

    # settings and status
    url(r'^status/$', views.status, name='status'),
    url(r'^status/enable/$', views.status_enable, name='status_enable_all'),
    url(r'^status/enable/(?P<sw>[0-9]+)/$', views.status_enable, name='status_enable'),
    url(r'^status/disable/$', views.status_disable, name='status_disable_all'),
    url(r'^status/disable/(?P<sw>[0-9]+)/$', views.status_disable, name='status_disable'),
    
    # all -- show all detailed rules
    url(r'^rules/$', views.rules, name='rules'),
    url(r'^rules/add/$', views.rules_add, name='rules_add'),
    url(r'^rules/delete/(?P<rule_id>[0-9]+)/$', views.rules_delete, name='rules_delete'),
    url(r'^rules/delete/$', views.rules_delete, name='rules_delete_all'),

    # shortcut for global rules
    url(r'^rules/allow_all/$', views.rules_allow_all, name='rules_allow_all'),
    url(r'^rules/deny_all/$', views.rules_deny_all, name='rules_deny_all'),
    
    # IP / IP range -- a quick entry for check / set rules based on IP / IP range
    url(r'^ip-rules/$', views.ip_rules, name='ip_rules'),
    url(r'^ip-rules/add/$', views.ip_rules_add, name='ip_rules_add'),
    url(r'^ip-rules/delete/(?P<rule_id>[0-9]+)/$', views.ip_rules_delete, name='ip_rules_delete'),
    url(r'^ip-rules/delete/$', views.ip_rules_delete, name='ip_rules_delete_all'),


    #get switch
    url(r'^get-switch/$', views.get_switch, name='get_switch'),
    
    #add flow
    url(r'^addflow/$', views.addflow, name='addflow'),

    url(r'^statusdpid/$', views.statusdpid, name='statusdpid'),

    url(r'^allflowstats/$', views.getflow, name='allflowstats'),
]   
