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


#QoS rules
def qosrules(request, sw_id='all'):
    """
    show all rules in a table
    provide form to add rule
    """
    rules = utils.flatten_rules(api.get_rules(sw=sw_id))
    form = RuleForm()
    return render(request, 'qosrule.html', {'rules': rules, 'form': form})

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
    rules7 = api.get_switch7()
    rules8 = api.get_switch8()
    rules9 = api.get_switch9()
    statusdpid = api.get_fw_statusdpid()
    print(statusdpid) 
    br = "1"
    br2 ="2"
    br3 ="3"
    br4 ="4"
    br5 ="5"
    br6 ="6"
    br7 ="7"
    br8 ="8"
    br9 ="9"
    print(rules) 
    # rules = utils.flatten_sw(api.get_switch())
    return render(request, 'getswitch.html', {'rules': rules, 'statusdpid' :statusdpid, 'br':br, 'rules2' :rules2, 'br2':br2, 'rules3' :rules3, 'br3':br3, 'rules4' :rules4, 'br4':br4, 'rules5' :rules5, 'br5':br5, 'rules6' :rules6, 'br6':br6, 'rules7' :rules7, 'br7':br7,'rules8' :rules8, 'br8':br8, 'rules9' :rules9, 'br9':br9})

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


def getflow2(request):
    rules = utils.flatten_flows2(api.allflowstats2())
    return render(request, 'allflow2.html', {'rules': rules})

def getflow3(request):
    rules = utils.flatten_flows3(api.allflowstats3())
    return render(request, 'allflow3.html', {'rules': rules})


def getflow4(request):
    rules = utils.flatten_flows4(api.allflowstats4())
    return render(request, 'allflow4.html', {'rules': rules})

def getflow5(request):
    rules = utils.flatten_flows5(api.allflowstats5())
    return render(request, 'allflow5.html', {'rules': rules})

def getflow6(request):
    rules = utils.flatten_flows6(api.allflowstats6())
    return render(request, 'allflow6.html', {'rules': rules})

def getflow7(request):
    rules = utils.flatten_flows7(api.allflowstats7())
    return render(request, 'allflow7.html', {'rules': rules})

def getflow8(request):
    rules = utils.flatten_flows8(api.allflowstats8())
    return render(request, 'allflow8.html', {'rules': rules})

def getflow9(request):
    rules = utils.flatten_flows9(api.allflowstats9())
    print(api.allflowstats9())
    return render(request, 'allflow9.html', {'rules': rules})

def testgraph(request):
    rules = utils.flatten_flows9(api.allflowstats9())
    print(api.allflowstats9())
    return render(request, 'flowgraph1.html', {'rules': rules})

def testgraph2(request):
    rules = utils.flatten_flows9(api.allflowstats9())
    print(api.allflowstats9())
    return render(request, 'flowgraph2.html', {'rules': rules})
def testgraph3(request):
    rules = utils.flatten_flows9(api.allflowstats9())
    print(api.allflowstats9())
    return render(request, 'flowgraph3.html', {'rules': rules})
def testgraph4(request):
    rules = utils.flatten_flows9(api.allflowstats9())
    print(api.allflowstats9())
    return render(request, 'flowgraph4.html', {'rules': rules})
def testgraph5(request):
    rules = utils.flatten_flows9(api.allflowstats9())
    print(api.allflowstats9())
    return render(request, 'flowgraph5.html', {'rules': rules})
def testgraph6(request):
    rules = utils.flatten_flows9(api.allflowstats9())
    print(api.allflowstats9())
    return render(request, 'flowgraph6.html', {'rules': rules})
def testgraph7(request):
    rules = utils.flatten_flows9(api.allflowstats9())
    print(api.allflowstats9())
    return render(request, 'flowgraph7.html', {'rules': rules})
def testgraph8(request):
    rules = utils.flatten_flows9(api.allflowstats9())
    print(api.allflowstats9())
    return render(request, 'flowgraph8.html', {'rules': rules})
def testgraph9(request):
    rules = utils.flatten_flows9(api.allflowstats9())
    print(api.allflowstats9())
    return render(request, 'flowgraph9.html', {'rules': rules})

def getaggregate1(request):
    rules =  utils.flatten_flows1(api.allaggregatestats1())
    rules2 = utils.flatten_flows2(api.allaggregatestats2())
    rules3 = utils.flatten_flows3(api.allaggregatestats3())
    rules4 = utils.flatten_flows4(api.allaggregatestats4())
    rules5 = utils.flatten_flows5(api.allaggregatestats5())
    rules6 = utils.flatten_flows6(api.allaggregatestats6())
    rules7 = utils.flatten_flows7(api.allaggregatestats7())
    rules8 = utils.flatten_flows8(api.allaggregatestats8())
    rules9 = utils.flatten_flows9(api.allaggregatestats9())
    # statusdpid = api.get_fw_statusdpid()
    print(api.allaggregatestats1()) 
    br = "1"
    br2 ="2"
    br3 ="3"
    br4 ="4"
    br5 ="5"
    br6 ="6"
    br7 ="7"
    br8 ="8"
    br9 ="9"
    print(rules) 
    # rules = utils.flatten_sw(api.get_switch())
    return render(request, 'allaggregate1.html', {'rules': rules, 'br' : br, 'rules2' :rules2, 'br2':br2, 'rules3' :rules3, 'br3':br3, 'rules4' :rules4, 'br4':br4, 'rules5' :rules5, 'br5':br5, 'rules6' :rules6, 'br6':br6, 'rules7' :rules7, 'br7':br7, 'rules8' :rules8, 'br8':br8, 'rules9' :rules9, 'br9':br9})


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
def getportdesc2(request):
    rules = utils.flatten_flows2(api.getportdesc2())
    return render(request, 'getportdesc2.html', {'rules': rules})
def getportdesc3(request):
    rules = utils.flatten_flows3(api.getportdesc2())
    return render(request, 'getportdesc3.html', {'rules': rules})
def getportdesc4(request):
    rules = utils.flatten_flows4(api.getportdesc4())
    return render(request, 'getportdesc4.html', {'rules': rules})

def getportdesc5(request):
    rules = utils.flatten_flows5(api.getportdesc5())
    return render(request, 'getportdesc5.html', {'rules': rules})

def getportdesc6(request):
    rules = utils.flatten_flows6(api.getportdesc6())
    return render(request, 'getportdesc6.html', {'rules': rules})

def getportdesc7(request):
    rules = utils.flatten_flows7(api.getportdesc7())
    return render(request, 'getportdesc7.html', {'rules': rules})

def getportdesc8(request):
    rules = utils.flatten_flows8(api.getportdesc8())
    return render(request, 'getportdesc8.html', {'rules': rules})
def getportdesc9(request):
    rules = utils.flatten_flows9(api.getportdesc9())
    return render(request, 'getportdesc9.html', {'rules': rules})



def getportstats1(request):
    # rules = api.allflowstats()
    #print(rules) 
    # increment = int(request.GET['append_increment'])
    # increment_to = increment + 10
    rules = utils.flatten_flows1(api.getportstats1())
    #rules = utils.flatten_flows1(api.allflowstats())[increment:increment_to]
    return render(request, 'getportstats1.html', {'rules': rules})

def getportstats2(request):
    rules = utils.flatten_flows2(api.getportstats2())
    return render(request, 'getportstats2.html', {'rules': rules})

def getportstats3(request):
    rules = utils.flatten_flows3(api.getportstats3())
    return render(request, 'getportstats3.html', {'rules': rules})

def getportstats4(request):
    rules = utils.flatten_flows4(api.getportstats4())
    return render(request, 'getportstats4.html', {'rules': rules})

def getportstats5(request):
    rules = utils.flatten_flows5(api.getportstats5())
    return render(request, 'getportstats5.html', {'rules': rules})

def getportstats6(request):
    rules = utils.flatten_flows6(api.getportstats6())
    return render(request, 'getportstats6.html', {'rules': rules})

def getportstats7(request):
    rules = utils.flatten_flows7(api.getportstats7())
    return render(request, 'getportstats7.html', {'rules': rules})

def getportstats8(request):
    rules = utils.flatten_flows8(api.getportstats8())
    return render(request, 'getportstats8.html', {'rules': rules})

def getportstats9(request):
    rules = utils.flatten_flows9(api.getportstats9())
    return render(request, 'getportstats9.html', {'rules': rules})

# def get_more_tables(request):
#     increment = int(request.GET['append_increment'])
#     increment_to = increment + 10
#     order = Order.objects.filter(owner=request.user).order_by('-id')[increment:increment_to]
#     return render(request, 'get_more_tables.html', {'order': order})

def aboutus_view(request):
    return render(request,'aboutus.html')

def guitopo(request):
    return render(request,'guitopo.html')