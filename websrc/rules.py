ALLOW_RULES = [
    {'dl_type': u'IPv4', 'actions': u'ALLOW'},
    {'dl_type': u'IPv6', 'actions': u'ALLOW'},
    {'dl_type': u'ARP', 'actions': u'ALLOW'},
]

DENY_RULES = [
    {'dl_type': u'IPv4', 'actions': u'DENY'},
    {'dl_type': u'IPv6', 'actions': u'DENY'},
    {'dl_type': u'ARP', 'actions': u'DENY'},
]
