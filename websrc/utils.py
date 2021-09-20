def flatten_rules(rules):
    """
    convert rules from api to a flat list
    """
    rtn = []
    for switch in rules:
        switch_id = switch['switch_id']
        for ac_list in switch['access_control_list']:
            for rule in ac_list['rules']:
                rule['switch_id'] = switch_id
                rtn.append(rule)
    return rtn


def is_pure_ip_rule(rule):
    if set(['in_port', 'dl_src', 'dl_dst', 'nw_proto']) & set(rule.keys()):
        return False
    if not set(['nw_src', 'nw_dst', 'ipv6_src', 'ipv6_src']) & set(rule.keys()):
        return False
    return True


def filter_pure_ip_rules(rules):
    """
    filter out the pure IP rules
    """
    return filter(is_pure_ip_rule, rules)


def is_global_rule(rule):
    """
    rules that have field: dl_type
    do NOT have field: nw_src nw_dst ipv6_src ipv6_dst nw_proto tp_src tp_dst
    """
    unset = set(['nw_src', 'nw_dst', 'ipv6_src', 'ipv6_dst', 'nw_proto', 'tp_src', 'tp_dst'])
    if unset & set(rule.keys()):
        return False
    return True


def filter_global_rules(rules):
    return filter(is_global_rule, rules)


# def flatten_sw(testswitches):
#     """
#     convert rules from api to a flat list
#     """
#     rtn = []
#     for switch in testswitches:
#         no1 = switch['1']
#         for rule in switch['1']:
#                 rule['1'] = no1
#                 rtn.append(rule)
#     return rtn

# def flatten_rules(rules):
#     """
#     convert rules from api to a flat list
#     """
#     rtn = []
#     for switch in rules:
#         switch_id = switch['switch_id']
#         for ac_list in switch['access_control_list']:
#             for rule in ac_list['rules']:
#                 rule['switch_id'] = switch_id
#                 rtn.append(rule)
#     return rtn

def flatten_sw(rules):
    """
    convert rules from api to a flat list
    """
    rtn = []
    for switch in rules:
        no1 = switch['1']
        for a in no1:
            rtn.append(a)
    return rtn

def flatten_flows1(rules):
    """
    convert rules from api to a flat list
    """
    rtn = []
    # for switch in rules:
    for a in rules['1']:
            rtn.append(a)
    return rtn
def flatten_flows2(rules):
    """
    convert rules from api to a flat list
    """
    rtn = []
    # for switch in rules:
    for a in rules['2']:
            rtn.append(a)
    return rtn
def flatten_flows3(rules):
    """
    convert rules from api to a flat list
    """
    rtn = []
    # for switch in rules:
    for a in rules['3']:
            rtn.append(a)
    return rtn
def flatten_flows4(rules):
    """
    convert rules from api to a flat list
    """
    rtn = []
    # for switch in rules:
    for a in rules['4']:
            rtn.append(a)
    return rtn
def flatten_flows5(rules):
    """
    convert rules from api to a flat list
    """
    rtn = []
    # for switch in rules:
    for a in rules['5']:
            rtn.append(a)
    return rtn
def flatten_flows6(rules):
    """
    convert rules from api to a flat list
    """
    rtn = []
    # for switch in rules:
    for a in rules['6']:
            rtn.append(a)
    return rtn
# def flatten_sw():
#     """
#     convert rules from api to a flat list
#     """
#     rtn = []
#     no1 = ['1']
#     for a in ['1']:
#         rtn.append(a)
#     return rtn

def flatten_flows(rules):
    """
    convert rules from api to a flat list
    """
    rtn = []
    for dpid in rules:
        dpid = dpid['1']
        for ac_list in switch['access_control_list']:
            for rule in ac_list['rules']:
                rule['switch_id'] = switch_id
                rtn.append(rule)
    return rtn

