from extras.plugins import PluginTemplateExtension
from django.conf import settings
from .models import Subsystems

plugin_settings = settings.PLUGINS_CONFIG.get('netbox_subsystems', {})


class SubsystemsList(PluginTemplateExtension):
    model = 'tenancy.tenant'

    def left_page(self):
        if plugin_settings.get('enable_subsystems') and plugin_settings.get('subsystems_location') == 'left':

            return self.render('netbox_subsystems/subsystems_include.html', extra_context={
                'subsystems': Subsystems.objects.filter(tenant=self.context['object'])
            })
        else:
            return ""

    def right_page(self):
        if plugin_settings.get('enable_subsystems') and plugin_settings.get('subsystems_location') == 'right':

            return self.render('netbox_subsystems/subsystems_include.html', extra_context={
                'subsystems': Subsystems.objects.filter(tenant=self.context['object'])
            })
        else:
            return ""


template_extensions = [SubsystemsList]
