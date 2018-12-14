from django.shortcuts import render
from .models import Person
from .tables import PersonTable
from django_tables2 import RequestConfig


def people(request):
    table = PersonTable(Person.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'tables/people.html', {'table': table})
