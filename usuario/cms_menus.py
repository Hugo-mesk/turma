from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from django.urls import reverse

from menus.menu_pool import menu_pool



class UsuarioMenu(CMSAttachMenu):

    name = _("usuario_menu")  # give the menu a name this is required.

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = []

        node = NavigationNode(
            title="Login",
            url=reverse('usuario-allauth'),
            id=51,  # unique id for this node within the menu
            attr={'visible_for_anonymous': True},
        )

        nodes.append(node)

        return nodes

menu_pool.register_menu(UsuarioMenu)
