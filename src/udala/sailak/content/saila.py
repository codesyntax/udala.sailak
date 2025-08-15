# -*- coding: utf-8 -*-
from collective.z3cform.datagridfield.datagridfield import DataGridFieldFactory
from collective.z3cform.datagridfield.registry import DictRow
from udala.sailak import _
from plone.app.multilingual.dx.interfaces import ILanguageIndependentField
from plone.app.textfield import RichText
from plone.autoform.directives import widget

# from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile import field as namedfile
from plone.supermodel import model

# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from zope.interface import Interface


class ISocialLinkRowSchema(Interface):
    name = schema.TextLine(title=_("Name of social network"))
    url = schema.TextLine(title=_("URL of social network"))
    iconname = schema.TextLine(title=_("Plone icon name to be applied to this item"))


class IExtraDataRowSchema(Interface):
    name = schema.TextLine(title=_("Name of the field"))
    value = schema.TextLine(title=_("Value of the field"))


class ISaila(model.Schema):
    """Marker interface and Dexterity Python Schema for Saila"""

    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    bannerimage = namedfile.NamedBlobImage(
        title=_("Sailaren portadako banner erako irudia)"),
        required=False,
    )

    sailaicon = namedfile.NamedBlobImage(
        title=_("Sailen portadarako irudia. Webgune nagusian bakarrik erabiltzen da)"),
        required=False,
    )

    sectiontitle = schema.TextLine(
        title="Sailaren izen ofiziala",
        required=False,
    )

    sectionsubtitle = schema.TextLine(
        title="Sailaren izenaren azpian agertuko dena",
        required=False,
    )

    hours = RichText(title=_("Ordutegia)"), required=False)

    widget(sociallinks=DataGridFieldFactory)
    sociallinks = schema.List(
        title=_("sociallinks"),
        value_type=DictRow(title=_("sociallinks"), schema=ISocialLinkRowSchema),
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
        title=_("extradata"),
        value_type=DictRow(title=_("extradata"), schema=IExtraDataRowSchema),
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

    # model.load('saila.xml')

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )


@implementer(ISaila)
class Saila(Container):
    """Content-type class for ISaila"""
