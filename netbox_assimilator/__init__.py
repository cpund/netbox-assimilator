from extras.plugins import PluginConfig



class NetboxAssimilatorConfig(PluginConfig):
    name = 'netbox_assimilator'
    verbose_name = 'Netbox Assimilator'
    description = 'Your devices will be assimilated into Netbox'
    version = '0.1'
    author = 'Craig Pund'
    author_email = 'cpund@iuhealth.org'
    base_url = 'assimilator'
    required_settings = []
    default_settings = {}

config = NetboxAssimilatorConfig
