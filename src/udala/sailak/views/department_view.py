from Products.Five.browser import BrowserView


class DepartmentView(BrowserView):
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

    def department_data(self):
        saila_dict = {}

        if self.context.bannerimage:
            featured_scales = self.context.restrictedTraverse("@@images")
            saila_dict["bannerimage"] = featured_scales.scale(
                "bannerimage", width=850, height=220
            ).url
        else:
            saila_dict["bannerimage"] = ""

        return saila_dict
