from django.shortcuts import render
from .forms import ProductForm, StyledForm
from django.http import HttpResponseRedirect


def forms_index(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/forms/')
    else:
        form = ProductForm()

    styled_form = StyledForm()

    return render(request, 'forms/form.html', {'form': form, 'styled_form': styled_form})
