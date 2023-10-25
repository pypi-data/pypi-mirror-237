from extras.plugins import PluginTemplateExtension
from django.conf import settings
from .models import System

plugin_settings = settings.PLUGINS_CONFIG.get('netbox_systems', {})


class SystemList(PluginTemplateExtension):
    model = 'tenancy.tenant'

    def left_page(self):
        if plugin_settings.get('enable_device_software') and plugin_settings.get('device_software_location') == 'left':

            return self.render('netbox_systems/system_include.html', extra_context={
                'systems': System.objects.filter(tenant=self.context['object'])
            })
        else:
            return ""

    def right_page(self):
        if plugin_settings.get('enable_device_software') and plugin_settings.get('device_software_location') == 'right':

            return self.render('netbox_systems/system_include.html', extra_context={
                'systems': System.objects.filter(tenant=self.context['object'])
            })
        else:
            return ""


template_extensions = [SystemList]
