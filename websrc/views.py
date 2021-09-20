import sys

from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings as django_settings
from django import forms
from django.urls import reverse

from . import api
from .forms import RuleForm, IPAddrRuleForm, SimplifiedRuleForm, flowForm
from .rules import ALLOW_RULES, DENY_RULES
from . import utils


# index page

def index(request):
    return render(request, 'index.html', {})



#  status and settings

def status(request):
    """
    show status of all SWs
    """
    status = api.get_fw_status()
    return render(request, 'status.html', {'status': status})

def statusdpid(request):
    """
    show status of all SWs
    """
    statusdpid = api.get_fw_statusdpid()
    return render(request, 'alldpidlist.html', {'statusdpid': statusdpid})

def statusdpid2(request):
    """
    show status of all SWs
    """
    statusdpid = api.get_fw_statusdpid()
    sorteddpid= statusdpid.order_by('dpid') 
    return render(request, 'status.html', {'sorteddpid': sorteddpid})

def status_enable(request, sw='all'):
    """
    enable fw on SWs
    """
    api.enable_fw(sw=sw)
    return HttpResponseRedirect(reverse('status'))


def status_disable(request, sw='all'):
    """
    disable fw on SWs
    """
    api.disable_fw(sw=sw)
    return HttpResponseRedirect(reverse('status'))


# detailed rules

def rules(request, sw_id='all'):
    """
    show all rules in a table
    provide form to add rule
    """
    rules = utils.flatten_rules(api.get_rules(sw=sw_id))
    form = RuleForm()
    return render(request, 'rules.html', {'rules': rules, 'form': form})


def rules_add(request):
    """
    add detailed rule
    """
    if request.method == 'POST':
        form = RuleForm(request.POST)
        if form.is_valid():
            rule_data = { k: v for k, v in form.cleaned_data.items() if v }
            api.add_rule(**rule_data)
            return HttpResponseRedirect(reverse('rules'))
    else:
        form = RuleForm()
    return render(request, 'add_rule.html', {'form': form})


def rules_delete(request, rule_id='all'):
    """
    delete a rule
    """
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            api.delete_rule(rule_id=rule_id)
            return HttpResponseRedirect(reverse('rules'))
    else:
        return HttpResponseRedirect(reverse('rules'))

# shortcut for global rules

def rules_allow_all(request):
    """
    Remove all current rules,
    and add a rule that allow all traffics with priority = 0
    """
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            api.delete_rule()
            for rule in ALLOW_RULES:
                api.add_rule(**rule)
            return HttpResponseRedirect(reverse('rules'))
    else:
        return HttpResponseRedirect(reverse('rules'))
        

def rules_deny_all(request):
    """
    Remove all current rules,
    and add a rule that deny all traffics with priority = 0
    """
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            api.delete_rule()
            for rule in DENY_RULES:
                api.add_rule(**rule)
            return HttpResponseRedirect(reverse('rules'))
    else:
        return HttpResponseRedirect(reverse('rules'))


# quick entry for IP based rules

def ip_rules(request):
    """
    (maybe) show rules in a table
    provide form to add IP based rule
    """
    rules = api.get_rules()
    rules = utils.flatten_rules(rules)
    rules = utils.filter_pure_ip_rules(rules)
    form = IPAddrRuleForm()
    return render(request, 'ip_rules.html', {'rules': rules, 'form': form})


def ip_rules_add(request):
    """
    add IP based rule
    """
    if request.method == 'POST':
        form = IPAddrRuleForm(request.POST)
        if form.is_valid():
            rule_data = { k: v for k, v in form.cleaned_data.items() if v }
            api.add_rule(**rule_data)
            return HttpResponseRedirect(reverse('ip_rules'))
    else:
        return HttpResponseRedirect(reverse('ip_rules'))

def ip_rules_delete(request, rule_id):
    """
    delete a rule and redirect to 'ip_rules'
    """
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            api.delete_rule(rule_id=rule_id)
            return HttpResponseRedirect(reverse('rules'))
    else:
        return HttpResponseRedirect(reverse('ip_rules'))

# def swstatus(request):
#     """
#     show status of all SWs
#     """
#     status = api.get_fw_status()
#     return render(request, 'getswitch.html', {'status': status})


# def rules(request, sw_id='all'):
#     """
#     show all rules in a table
#     provide form to add rule
#     """
#     rules = utils.flatten_rules(api.get_rules(sw=sw_id))
#     form = RuleForm()
#     return render(request, 'rules.html', {'rules': rules, 'form': form})



def get_switch(request):
    rules = api.get_switch()
    rules2 = api.get_switch2()
    rules3 = api.get_switch3()
    rules4 = api.get_switch4()
    rules5 = api.get_switch5()
    rules6 = api.get_switch6()
    statusdpid = api.get_fw_statusdpid()
    print(statusdpid) 
    br = "1"
    br2 ="2"
    br3 ="3"
    br4 ="4"
    br5 ="5"
    br6 ="6"
    print(rules) 
    # rules = utils.flatten_sw(api.get_switch())
    return render(request, 'getswitch.html', {'rules': rules, 'statusdpid' :statusdpid, 'br':br, 'rules2' :rules2, 'br2':br2, 'rules3' :rules3, 'br3':br3, 'rules4' :rules4, 'br4':br4, 'rules5' :rules5, 'br5':br5, 'rules6' :rules6, 'br6':br6})

# def get_switch(request, dpid='all'):
#     #rules = api.get_switch()
#     #statusdpid = api.get_fw_statusdpid()
#     #print(statusdpid) 
#     rules = utils.flatten_sw(api.get_switch(sw=dpid))
#     print(rules) 
#     return render(request, 'getswitch.html', {'rules': rules})

# def get_switch(request):
#     #rules = api.get_switch()
#     #statusdpid = api.get_fw_statusdpid()
#     #print(statusdpid) 
#     #rules = utils.flatten_sw(api.get_switch())
#     print(rules) 
#     return render(request, 'getswitch.html', {'rules': rules})



def addflow(request):
    """
    add flow
    """
    if request.method == 'POST':
        form = flowForm(request.POST)
        if form.is_valid():
            rule_data = { k: v for k, v in form.cleaned_data.items() if v }
            api.addflow(**rule_data)
            return HttpResponseRedirect(reverse('addflow'))
    else:
        return HttpResponseRedirect(reverse('addflow'))

def flowentryclear(request, sw='all'):
    """
    disable fw on SWs
    """
    api.clearflowentry(sw=sw)
    return render(request, 'allflows1.html')


def getflow(request):
    """
    (maybe) show rules in a table
    provide form to add IP based rule
    """
    # rules = api.allflowstats()
    #print(rules) 
    # increment = int(request.GET['append_increment'])
    # increment_to = increment + 10
    rules = utils.flatten_flows1(api.allflowstats1())
    #rules = utils.flatten_flows1(api.allflowstats())[increment:increment_to]
    return render(request, 'allflow1.html', {'rules': rules})

def getaggregate1(request):
    rules =  api.allaggregatestats()
    # rules2 = utils.flatten_flows2(api.allaggregatestats2())
    # rules3 = utils.flatten_flows3(api.allaggregatestats3())
    # rules4 = utils.flatten_flows4(api.allaggregatestats4())
    # rules5 = utils.flatten_flows5(api.allaggregatestats5())
    # rules6 = utils.flatten_flows6(api.allaggregatestats6())
    # statusdpid = api.get_fw_statusdpid()
    # print(statusdpid) 
    br = "1"
    # br2 ="2"
    # br3 ="3"
    # br4 ="4"
    # br5 ="5"
    # br6 ="6"
    print(rules) 
    # rules = utils.flatten_sw(api.get_switch())
    return render(request, 'allaggregate1.html', {'rules': rules, 'br' : br})


def getportdesc1(request):
    """
    (maybe) show rules in a table
    provide form to add IP based rule
    """
    # rules = api.allflowstats()
    #print(rules) 
    # increment = int(request.GET['append_increment'])
    # increment_to = increment + 10
    rules = utils.flatten_flows1(api.getportdesc1())
    #rules = utils.flatten_flows1(api.allflowstats())[increment:increment_to]
    return render(request, 'getportdesc1.html', {'rules': rules})

def getportstats1(request):
    # rules = api.allflowstats()
    #print(rules) 
    # increment = int(request.GET['append_increment'])
    # increment_to = increment + 10
    rules = utils.flatten_flows1(api.getportstats1())
    #rules = utils.flatten_flows1(api.allflowstats())[increment:increment_to]
    return render(request, 'getportstats1.html', {'rules': rules})


# def get_more_tables(request):
#     increment = int(request.GET['append_increment'])
#     increment_to = increment + 10
#     order = Order.objects.filter(owner=request.user).order_by('-id')[increment:increment_to]
#     return render(request, 'get_more_tables.html', {'order': order})

def aboutus_view(request):
    return render(request,'aboutus.html')