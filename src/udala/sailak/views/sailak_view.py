# -*- coding: utf-8 -*-

# from udala.sailak import _
from plone import api
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ISailakView(Interface):
    """Marker Interface for ISailakView"""


@implementer(ISailakView)
class SailakView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('sailak_view.pt')

    def sailak(self):
        context_path = self.context.getPhysicalPath()
        brains = api.content.find(
            portal_type="Saila",
            sort_on="getObjPositionInParent",
            Language=self.context.Language(),
            path="/".join(context_path),
        )
        return_list = []
        for brain in brains:
            saila = brain.getObject()
            return_list.append(saila)
        return return_list
