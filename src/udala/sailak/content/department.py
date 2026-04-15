from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield.registry import DictRow
from plone.app.dexterity import textindexer
from plone.app.multilingual.dx.interfaces import ILanguageIndependentField
from plone.app.textfield import RichText
from plone.autoform.directives import widget
from plone.dexterity.content import Container
from plone.namedfile import field as namedfile
from plone.supermodel import model
from udala.sailak import _
from zope import schema
from zope.interface import alsoProvides
from zope.interface import implementer
from zope.interface import Interface


class ISocialLinkRowSchema(Interface):
    name = schema.TextLine(title=_("Name of social network"))
    url = schema.TextLine(title=_("URL of social network"))
    iconname = schema.TextLine(title=_("Plone icon name to be applied to this item"))


class IExtraDataRowSchema(Interface):
    name = schema.TextLine(title=_("Name of the field"))
    value = schema.TextLine(title=_("Value of the field"))


class IDepartment(model.Schema):
    """Marker interface and Dexterity Python Schema for Department"""

    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    bannerimage = namedfile.NamedBlobImage(
        title=_("Banner-like image of the Department home"),
        required=False,
    )

    sailaicon = namedfile.NamedBlobImage(
        title=_("Department icon (only used in the department listing)"),
        required=False,
    )

    textindexer.searchable("sectiontitle")
    sectiontitle = schema.TextLine(
        title=_("Official name of the department"),
        description=_(
            "Fill this in if you want to have a different title in the "
            "department listing (the title) and here (this one)"
        ),
        required=False,
    )

    textindexer.searchable("sectionsubtitle")
    sectionsubtitle = schema.TextLine(
        title=_("Subtitle that will be shown below the department name"),
        required=False,
    )

    textindexer.searchable("meeting_agenda")
    hours = RichText(title=_("Opening hours"), required=False)

    widget(sociallinks=DataGridFieldFactory)
    sociallinks = schema.List(
        title=_("Social network links"),
        value_type=DictRow(title=_("Social network link"), schema=ISocialLinkRowSchema),
        default=[
            {
                "name": "Twitter",
                "url": "https://twitter.com/EibarkoUdala",
                "iconname": "twitter",
            },
            {
                "name": "FaceBook",
                "url": "https://www.facebook.com/pages/Eibarko-Udala/371951916348590",
                "iconname": "facebook",
            },
            {
                "name": "Youtube",
                "url": "https://www.youtube.com/channel/UCTNEPKwdQgEuhO0S4nUGaPw",
                "iconname": "youtube",
            },
        ],
        required=False,
    )

    widget(extradata=DataGridFieldFactory)
    extradata = schema.List(
        title=_("Extra information"),
        description=_(
            "Field to add arbitrary extra information. Ex.: responsible name, "
            "telephone number, email, ..."
        ),
        value_type=DictRow(title=_("Extra information"), schema=IExtraDataRowSchema),
        default=[
            {"name": "Arduraduna", "value": ""},
            {"name": "Zinegotzia", "value": ""},
            {"name": "Helbidea", "value": ""},
            {"name": "Telefonoa", "value": ""},
            {"name": "Eposta", "value": ""},
            {"name": "Faxa", "value": ""},
            {"name": "Webgunea", "value": ""},
        ],
        required=False,
    )


alsoProvides(IDepartment["bannerimage"], ILanguageIndependentField)
alsoProvides(IDepartment["sailaicon"], ILanguageIndependentField)
alsoProvides(IDepartment["sociallinks"], ILanguageIndependentField)


@implementer(IDepartment)
class Department(Container):
    """Content-type class for IDepartment"""
