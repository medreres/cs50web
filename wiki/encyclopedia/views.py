# from turtle import title
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
import random
from . import libr
import markdown

from . import util
ERROR_MESSAGE = "error_message"


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def page(request, name):
    file = util.get_entry(name)
    if file is None:
        return render(request, "encyclopedia/apology.html", {ERROR_MESSAGE: "Error. Page not found"})
    html = libr.convert(file)
    # html = markdown.markdown(file)
    # print("\n\n\n")
    # print(html)
    return render(request, "encyclopedia/page.html", {
        "entry": html,
        "name": name
    })


def search(request):
    query = request.GET.get('q')
    file = util.get_entry(query)
    # TODO
    # if there is no such entry
    if file is None:
        entries = util.list_entries()
        substrings = []
        for entry in entries:
            if query in entry:
                substrings.append(entry)
        results = {"entries": substrings}
        return render(request, "encyclopedia/search.html", results)
    return page(request, query)


def add(request):
    if request.method == "GET":
        return render(request, "encyclopedia/add.html")
    else:
        title = request.POST.get('title')
        text = request.POST.get('text')
        if len(title) == 0 or len(text) == 0:
            return render(request, "encyclopedia/apology.html", {ERROR_MESSAGE: "Either of the inputs is blank"})
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/apology.html", {ERROR_MESSAGE: "Similar page already exists!"})
        util.save_entry(title, text)
        return page(request, title)


def edit(request, name):
    if request.method == "GET":
        text = util.get_entry(name)
        entry = {"title": name, "text": text}
        return render(request, "encyclopedia/edit.html", entry)
    else:
        text = request.POST.get('text')
        util.save_entry(name, text)
        return HttpResponseRedirect(f"../{name}")


def rand(request):
    entries = util.list_entries()
    index = random.randint(0, len(entries) - 1)
    return HttpResponseRedirect(f"../{entries[index]}")

