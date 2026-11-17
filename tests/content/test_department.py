from plone import api
from plone.app.testing import SITE_OWNER_NAME
from udala.sailak.content.datagrid import KeepEmptyDataGridFieldConverter
from udala.sailak.content.datagrid import KeepEmptyDataGridFieldFactory
from udala.sailak.content.department import IDepartment
from z3c.form.interfaces import IContextAware
from z3c.form.interfaces import IDataConverter
from zope.interface import alsoProvides


def _create_department(portal):
    with api.env.adopt_user(SITE_OWNER_NAME):
        return api.content.create(
            container=portal,
            type="Department",
            id="department",
            title="Department",
        )


def _update_widget(department, request):
    widget = KeepEmptyDataGridFieldFactory(IDepartment["sociallinks"], request)
    widget.context = department
    alsoProvides(widget, IContextAware)
    widget.update()
    return widget


def test_empty_sociallinks_are_stored_as_empty_list(integration, portal):
    department = _create_department(portal)
    widget = _update_widget(department, portal.REQUEST)
    converter = IDataConverter(widget)

    assert isinstance(converter, KeepEmptyDataGridFieldConverter)
    assert converter.toFieldValue([]) == []


def test_empty_sociallinks_are_not_replaced_by_default(integration, portal):
    department = _create_department(portal)
    department.sociallinks = []

    widget = _update_widget(department, portal.REQUEST)

    assert widget.value == []


def test_default_sociallinks_are_shown_when_there_is_no_value(integration, portal):
    department = _create_department(portal)

    widget = _update_widget(department, portal.REQUEST)

    assert [row["name"] for row in widget.value] == [
        "Twitter",
        "FaceBook",
        "Youtube",
    ]
