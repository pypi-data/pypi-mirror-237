from extras.plugins import PluginMenuItem, PluginMenu, PluginMenuButton
from utilities.choices import ButtonColorChoices
from django.conf import settings

plugin_settings = settings.PLUGINS_CONFIG.get('netbox_subsystems', {})


class MyPluginMenu(PluginMenu):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name = name

    @property
    def name(self):
        return self._name


if plugin_settings.get('enable_navigation_menu'):
    menuitem = []
    # Add a menu item for Subsystems if enabled
    if plugin_settings.get('enable_subsystems'):
        menuitem.append(
            PluginMenuItem(
                link='plugins:netbox_subsystems:subsystems_list',
                link_text='Системы',
                buttons=[PluginMenuButton(
                    link='plugins:netbox_subsystems:subsystems_add',
                    title='Создать',
                    icon_class='mdi mdi-plus-thick',
                    color=ButtonColorChoices.GREEN
                )],
                permissions=['dcim.view_device']
            )
        )

    # If we are using NB 3.4.0+ display the new top level navigation option
    if settings.VERSION >= '3.4.0':
        menu = MyPluginMenu(
            name='subsystemsPl',
            label='Системы',
            groups=(
                ('', menuitem),
            ),
            icon_class='mdi mdi-microsoft-xbox-controller-off'
        )

    else:
        # Fall back to pre 3.4 navigation option
        menu_items = menuitem
