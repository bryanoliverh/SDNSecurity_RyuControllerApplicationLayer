from django import forms


# class ConfirmForm(forms.Form):
#     enabled = forms.BooleanField(label='Enabled')


# class SettingsForm(forms.Form):
#     ip = forms.GenericIPAddressField(label='IP address')


class RuleForm(forms.Form):

    DL_TYPE_CHOICES = (
        ('', '-'),
        ('ARP', 'ARP'),
        ('IPv4', 'IPv4'),
        ('IPv6', 'IPv6'),
    )

    NW_PROTO_CHOICES = (
        ('', '-'),
        ('TCP', 'TCP'),
        ('UDP', 'UDP'),
        ('ICMP', 'ICMP'),
        ('ICMPv6', 'ICMPv6'),
    )

    ACTION_CHOICES = (
        ('ALLOW', 'ALLOW'),
        ('DENY', 'DENY'),
    )

    priority = forms.IntegerField(
        label="Priority", required=False, min_value=0, max_value=65535)
    in_port = forms.IntegerField(
        label="In Port", required=False, min_value=0, max_value=65535)
    # dl_src, dl_dst
    dl_type = forms.ChoiceField(required=False, choices=DL_TYPE_CHOICES)
    # nw_src = forms.GenericIPAddressField(required=False)
    # nw_dst = forms.GenericIPAddressField(required=False)
    nw_src = forms.CharField(required=False)
    nw_dst = forms.CharField(required=False)
    # ipv6_src = forms.GenericIPAddressField(required=False)
    # ipv6_dst = forms.GenericIPAddressField(required=False)
    ipv6_src = forms.CharField(required=False)
    ipv6_dst = forms.CharField(required=False)
    nw_proto = forms.ChoiceField(required=False, choices=NW_PROTO_CHOICES)
    tp_src = forms.IntegerField(
        label="TP SRC", required=False, min_value=0, max_value=65535)
    tp_dst = forms.IntegerField(
        label="TP DST", required=False, min_value=0, max_value=65535)
    actions = forms.ChoiceField(choices=ACTION_CHOICES)


class SimplifiedRuleForm(forms.Form):
    """
    a bit simplified
    """

    NW_PROTO_CHOICES = (
        ('', '-'),
        ('TCP', 'TCP'),
        ('UDP', 'UDP'),
        ('ICMP', 'ICMP'),
        ('ICMPv6', 'ICMPv6'),
    )

    ACTION_CHOICES = (
        ('ALLOW', 'ALLOW'),
        ('DENY', 'DENY'),
    )

    PORT_CHOICES = (
        ('80', 'HTTP'),
        ('443', 'HTTPS'),
        ('21', 'FTP Connection'),
        ('22', 'FTP Data'),
        ('25', 'SMTP'),
        ('110', 'POP'),
        ('53', 'DNS'),
        ('23', 'Telnet'),
    )

    priority = forms.IntegerField(label="Priority", required=False, min_value=0, max_value=65535)
    nw_src = forms.CharField(required=False)
    nw_dst = forms.CharField(required=False)
    ipv6_src = forms.CharField(required=False)
    ipv6_dst = forms.CharField(required=False)
    nw_proto = forms.ChoiceField(required=False, choices=NW_PROTO_CHOICES)
    tp_src = forms.ChoiceField(required=False, choices=PORT_CHOICES)
    tp_dst = forms.ChoiceField(required=False, choices=PORT_CHOICES)
    actions = forms.ChoiceField(choices=ACTION_CHOICES)


class IPAddrRuleForm(forms.Form):
    """
    If only the IPv4 addr (range) is cared
    """

    DL_TYPE_CHOICES = (
        ('', '-'),
        ('ARP', 'ARP'),
        ('IPv4', 'IPv4'),
        ('IPv6', 'IPv6'),
    )

    ACTION_CHOICES = (
        ('ALLOW', 'ALLOW'),
        ('DENY', 'DENY'),
    )

    priority = forms.IntegerField(label="Priority", required=False, min_value=0, max_value=65535)
    nw_src = forms.CharField(required=False)
    nw_dst = forms.CharField(required=False)
    actions = forms.ChoiceField(choices=ACTION_CHOICES)

class flowForm(forms.Form):
    dpid  = forms.IntegerField(label="Priority", required=False, min_value=0, max_value=65535)
    cookie = forms.IntegerField(required=False)
    cookie_mask = forms.IntegerField(required=False)
    table_id = forms.IntegerField(required=False)
    idle_timeout = forms.IntegerField(required=False)
    hard_timeout = forms.IntegerField(required=False)
    priority = forms.IntegerField(required=False)
    flags = forms.IntegerField(required=False)
    match = forms.IntegerField(required=False)

