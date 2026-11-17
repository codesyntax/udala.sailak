"""Data grid widgets that keep an explicitly cleared value cleared."""

from collective.z3cform.datagridfield.datagridfield import DataGridFieldConverter
from collective.z3cform.datagridfield.datagridfield import DataGridFieldWidget
from z3c.form import interfaces
from z3c.form.interfaces import IDataConverter
from z3c.form.interfaces import IFormLayer
from z3c.form.widget import FieldWidget
from zope.component import adapter
from zope.interface import implementer
from zope.schema.interfaces import IField
from zope.schema.interfaces import IList


class KeepEmptyDataGridFieldWidget(DataGridFieldWidget):
    """Data grid widget that stores an empty grid as an empty list."""


@adapter(IField, IFormLayer)
@implementer(interfaces.IFieldWidget)
def KeepEmptyDataGridFieldFactory(field, request):
    return FieldWidget(field, KeepEmptyDataGridFieldWidget(request))


@adapter(IList, KeepEmptyDataGridFieldWidget)
@implementer(IDataConverter)
class KeepEmptyDataGridFieldConverter(DataGridFieldConverter):
    """Converter that does not turn an empty grid into the missing value.

    By default an empty list is converted to ``field.missing_value``. The
    widget then falls back to ``field.default``, which makes the default rows
    reappear when the edit form is opened again.
    """

    def toFieldValue(self, value):
        if not value:
            return []
        return super().toFieldValue(value)
