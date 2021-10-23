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
from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    path('status/', views.status),
    path('getswitch/', views.get_switch),
    path('iprules/', views.ip_rules),
    path('detailedrules/', views.rules),
    path('dpid/', views.statusdpid),
    path('allflowstats/', views.getflow),
    path('aboutus', views.aboutus_view),
    # path('allflow1', views.getflow),
    # path('allflow2', views.getflow2),
    # path('allflow3', views.getflow3),
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

    url(r'^allflowstats1/$', views.getflow, name='allflowstats1'),
    url(r'^allflowstats2/$', views.getflow2, name='allflowstats2'),
    url(r'^allflowstats3/$', views.getflow3, name='allflowstats3'),
    url(r'^allflowstats4/$', views.getflow4, name='allflowstats4'),
    url(r'^allflowstats5/$', views.getflow5, name='allflowstats5'),
    url(r'^allflowstats6/$', views.getflow6, name='allflowstats6'),
    url(r'^allflowstats7/$', views.getflow7, name='allflowstats7'),
    url(r'^allflowstats8/$', views.getflow8, name='allflowstats8'),
    url(r'^allflowstats9/$', views.getflow9, name='allflowstats9'),
    url(r'^stats/flowentry/clear/$', views.flowentryclear, name='flowentryclear'),
    
    url(r'^allaggregate1/$', views.getaggregate1, name='allaggregate1'),
    
    url(r'^getportdesc1/$', views.getportdesc1, name='getportdesc1'),
    url(r'^getportdesc2/$', views.getportdesc2, name='getportdesc2'),
    url(r'^getportdesc3/$', views.getportdesc3, name='getportdesc3'),
    url(r'^getportdesc4/$', views.getportdesc4, name='getportdesc4'),
    url(r'^getportdesc5/$', views.getportdesc5, name='getportdesc5'),
    url(r'^getportdesc6/$', views.getportdesc6, name='getportdesc6'),
    url(r'^getportdesc7/$', views.getportdesc7, name='getportdesc7'),
    url(r'^getportdesc8/$', views.getportdesc8, name='getportdesc8'),
    url(r'^getportdesc9/$', views.getportdesc9, name='getportdesc9'),

    url(r'^getportstats1/$', views.getportstats1, name='getportstats1'),
    url(r'^getportstats2/$', views.getportstats2, name='getportstats2'),
    url(r'^getportstats3/$', views.getportstats3, name='getportstats3'),
    url(r'^getportstats4/$', views.getportstats4, name='getportstats4'),
    url(r'^getportstats5/$', views.getportstats5, name='getportstats5'),
    url(r'^getportstats6/$', views.getportstats6, name='getportstats6'),
    url(r'^getportstats7/$', views.getportstats7, name='getportstats7'),
    url(r'^getportstats8/$', views.getportstats8, name='getportstats8'),
    url(r'^getportstats9/$', views.getportstats9, name='getportstats9'),

    url(r'^guitopo/$', views.guitopo, name='guitopo'),
    url(r'^qosrules/$', views.qosrules, name='qosrules'),
    url(r'^qosrules/add/$', views.rules_add, name='qosrules_add'),
    url(r'^qosrules/delete/(?P<rule_id>[0-9]+)/$', views.rules_delete, name='qosrules_delete'),
    url(r'^qosrules/delete/$', views.rules_delete, name='qosrules_delete_all'),

   url(r'^flowgraph1/$', views.testgraph, name='testgraph'),
   url(r'^flowgraph2/$', views.testgraph2, name='testgraph2'),
   url(r'^flowgraph3/$', views.testgraph3, name='testgraph3'),
   url(r'^flowgraph4/$', views.testgraph4, name='testgraph4'),
   url(r'^flowgraph5/$', views.testgraph5, name='testgraph5'),
   url(r'^flowgraph6/$', views.testgraph6, name='testgraph6'),
   url(r'^flowgraph7/$', views.testgraph7, name='testgraph7'),
   url(r'^flowgraph8/$', views.testgraph8, name='testgraph8'),
   url(r'^flowgraph9/$', views.testgraph9, name='testgraph9'),

     path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),

]   
