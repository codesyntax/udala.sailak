# from udala.sailak import _
from Products.Five.browser import BrowserView
from zope.interface import implementer
from zope.interface import Interface


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ISailaView(Interface):
    """Marker Interface for ISailaView"""


@implementer(ISailaView)
class SailaView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('saila_view.pt')
    def title(self):
        title = self.context.Title().strip()
        if self.context.sectiontitle:
            sectiontitle = self.context.sectiontitle.strip()
        else:
            sectiontitle = ""
        return sectiontitle or title

    def saila_data(self):
        saila_dict = {}

        if self.context.bannerimage:
            featured_scales = self.context.restrictedTraverse("@@images")
            saila_dict["bannerimage"] = featured_scales.scale(
                "bannerimage", width=850, height=220
            ).url
        else:
            saila_dict["bannerimage"] = ""

        return saila_dict
