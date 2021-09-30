import json
from django.conf import settings as config
import requests


def _req(method, url, timeout=2.0, *args, **kwargs):
    f = getattr(requests, method)
    _url = "http://{}{}".format(config.CONTROLLER, url)
    response = f(_url, timeout=timeout, *args, **kwargs)
    response.raise_for_status()
    return response.json()

def _get(url, *args, **kwargs):
    return _req('get', url, *args, **kwargs)

def _post(url, *args, **kwargs):
    return _req('post', url, *args, **kwargs)

def _put(url, *args, **kwargs):
    return _req('put', url, *args, **kwargs)

def _delete(url, *args, **kwargs):
    return _req('delete', url, *args, **kwargs)


# firewall status

def get_fw_status():
    """
    get firewall status
    GET /firewall/module/status
    """
    return _get('/firewall/module/status')

def get_fw_statusdpid():
    """
    get firewall status
    GET /firewall/module/status
    """
    return _get('/stats/switches')

def enable_fw(sw='all'):
    """
    start firewall
    PUT /firewall/module/enable/{switch-id}
    """
    return _put('/firewall/module/enable/{}'.format(sw))

def disable_fw(sw='all'):
    """
    disable firewall
    PUT /firewall/module/disable/{switch-id}
    """
    return _put('/firewall/module/disable/{}'.format(sw))


# firewall logs

def get_log_status():
    """
    get log status of all FW SWs
    GET /firewall/log/status
    """
    return _get('/firewall/log/status')

def enable_log(sw='all'):
    """
    set log enable the FW SWs
    PUT /firewall/log/enable/{switch-id}
    """
    return _put('/firewall/log/enable/{}'.format(sw))

def disable_log(sw='all'):
    """
    set log disable the FW SWs
    PUT /firewall/log/disable/{switch-id}
    """
    return _put('/firewall/log/disable/{}'.format(sw))


# firewall rules

def get_rules(sw='all'):
    """
    GET /firewall/rules/{switch-id}
    GET /firewall/rules/{switch-id}/{vlan-id}
    """
    return _get('/firewall/rules/{}'.format(sw))

def add_rule(sw='all', **kwargs):
    """
    POST /firewall/rules/{switch-id}
    POST /firewall/rules/{switch-id}/{vlan-id}
    """
    payload = kwargs
    return _post('/firewall/rules/{}'.format(sw), json=payload)

def delete_rule(sw='all', rule_id='all'):
    """
    DELETE /firewall/rules/{switch-id}
    DELETE /firewall/rules/{switch-id}/{vlan-id}
    """
    payload = { 'rule_id': rule_id }
    return _delete('/firewall/rules/{}'.format(sw), json=payload)

# #def get_switch():
# def get_switch(sw='all'):
#     # return _get('/stats/desc/1')
#     return _get('/stats/desc/{}'.format(sw))

def get_switch():
    # return _get('/stats/desc/1')
    return _get('/stats/desc/1')

def get_switch2():
    # return _get('/stats/desc/1')
    return _get('/stats/desc/2')

def get_switch3():
    # return _get('/stats/desc/1')
    return _get('/stats/desc/3')

def get_switch4():
    # return _get('/stats/desc/1')
    return _get('/stats/desc/4')
def get_switch5():
    # return _get('/stats/desc/1')
    return _get('/stats/desc/5')
def get_switch6():
    # return _get('/stats/desc/1')
    return _get('/stats/desc/6')


def addflow(sw='all', **kwargs):
    """
    POST /firewall/rules/{switch-id}
    POST /firewall/rules/{switch-id}/{vlan-id}
    """
    payload = kwargs
    return _post('/stats/flowentry/add'.format(sw), json=payload)
    
def allflowstats1():
    return _get('/stats/flow/1')
def allflowstats2():
    return _get('/stats/flow/2')
def allflowstats3():
    return _get('/stats/flow/3')
def allflowstats4():
    return _get('/stats/flow/4')

def allflowstats5():
    return _get('/stats/flow/5')

def allflowstats6():
    return _get('/stats/flow/6')
def clearflowentry(sw='all'):
    """
    disable firewall
    PUT /firewall/module/disable/{switch-id}
    """
    return _put('/stats/flowentry/clear/1'.format(sw))



def getportdesc1():

    return _get('/stats/portdesc/1')

def getportdesc2():

    return _get('/stats/portdesc/2')

def getportdesc3():

    return _get('/stats/portdesc/3')

def getportdesc4():

    return _get('/stats/portdesc/4')

def getportdesc5():

    return _get('/stats/portdesc/5')

def getportdesc6():

    return _get('/stats/portdesc/6')


def getportstats1():

    return _get('/stats/port/1')



def allaggregatestats():

    return _get('/stats/aggregateflow/1')

def allaggregatestats2():

    return _get('/stats/aggregateflow/2')

def allaggregatestats3():

    return _get('/stats/aggregateflow/3')
def allaggregatestats4():

    return _get('/stats/aggregateflow/4')
def allaggregatestats5():

    return _get('/stats/aggregateflow/5')
def allaggregatestats6():

    return _get('/stats/aggregateflow/6')

