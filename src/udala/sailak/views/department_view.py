from Products.Five.browser import BrowserView


class DepartmentView(BrowserView):
    def title(self):
        title = self.context.Title().strip()
        if self.context.sectiontitle:
            sectiontitle = self.context.sectiontitle.strip()
        else:
            sectiontitle = ""
        return sectiontitle or title

    def department_data(self):
        department_dict = {}

        if self.context.bannerimage:
            featured_scales = self.context.restrictedTraverse("@@images")
            department_dict["bannerimage"] = featured_scales.scale(
                "bannerimage", width=850, height=220
            ).url
        else:
            department_dict["bannerimage"] = ""

        return department_dict
