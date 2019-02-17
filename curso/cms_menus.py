from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool


from .models import Periodo
#from .views import periodo_detail as periodo_view
#from .views import materia as materia_view

class PeriodoMenu(CMSAttachMenu):

    name = _("Periodo Menu")  # give the menu a name this is required.

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = []
        for periodo in Periodo.objects.order_by('numero').prefetch_related('materias'):
            node = NavigationNode(
                title=periodo.titulo,
                url=periodo.get_absolute_url(),
                id=periodo.numero,  # unique id for this node within the menu
                attr={'visible_for_anonymous': False},
            )
            print(node)
            nodes.append(node)
            for materia in periodo.materias.all():
                node = NavigationNode(
                    title=materia.titulo,
                    url=materia.get_absolute_url(),
                    id=materia.pk,  # unique id for this node within the menu
                    parent_id=periodo.numero,
                    attr={'visible_for_anonymous': False},
                )

                print(node)
                nodes.append(node)

        return nodes

menu_pool.register_menu(PeriodoMenu)
