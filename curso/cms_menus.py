from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool

from .models import Periodo, Materia
from .views import periodo_detail, materia

class PeriodoMenu(CMSAttachMenu):
    name = _("Periodo Menu")  # give the menu a name this is required.

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = []
        for periodo in Periodo.objects.all():
            node = NavigationNode(
                title=periodo.slug,
                url=reverse(periodo_detail, kwargs={'periodo_slug': periodo.slug}),
                id=periodo.numero,  # unique id for this node within the menu
                attr={'visible_for_anonymous': False},
            )

            nodes.append(node)

            for materia in periodo.materia_set.all():
                node = NavigationNode(
                    title=material.titulo,
                    url=reverse(materia, kwargs={'materia_titulo': materia.titulo}),
                    id=materia.pk,  # unique id for this node within the menu
                    parent_id=periodo.numero,
                    attr={'visible_for_anonymous': False},
                )

                nodes.append(node)

        return nodes

menu_pool.register_menu(PeriodoMenu)
