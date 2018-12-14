import django_tables2 as tables
from .models import Person


class PersonTable(tables.Table):
    name = tables.Column(attrs={'th': {'id': 'foo'}})

    class Meta:
        model = Person
