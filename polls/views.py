from django.shortcuts import render, HttpResponse
from django.http.request import HttpRequest

from .forms import PersonForm
from .models import Person


def index(request: HttpRequest):
    if request.method == "GET":
        return render(request, "index.html", context={"form": PersonForm})
    else:
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse(form.errors)
        return render(request, "index.html", context={"form": form})


