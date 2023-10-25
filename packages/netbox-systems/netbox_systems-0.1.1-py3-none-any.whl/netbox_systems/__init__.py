from extras.plugins import PluginConfig


class NetboxSoftware(PluginConfig):
    name = 'netbox_systems'
    verbose_name = 'Системы и подсистемы'
    description = 'Manage systems in Netbox'
    version = '0.0.1'
    author = 'Ilya Zakharov'
    author_email = 'me@izakharov.ru'
    min_version = '3.2.0'
    base_url = 'pl_systems'
    default_settings = {
        "enable_navigation_menu": True,
        "enable_system": True,
        "system_location": "left",
    }


config = NetboxSoftware
