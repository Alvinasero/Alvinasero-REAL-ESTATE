from django.shortcuts import render

from accounts.permissions import admin_required

def property_list(request):
    return render(request, 'properties/listings.html', {'active_page': 'listings'})


def property_detail(request):
    return render(request, 'properties/detail.html', {'active_page': 'listings'})


@admin_required
def manage_properties(request):
    return render(request, 'properties/manage.html', {'active_page': 'manage'})


@admin_required
def add_property(request):
    return render(request, 'properties/add.html', {'active_page': 'manage'})


@admin_required
def edit_property(request):
    return render(request, 'properties/edit.html', {'active_page': 'manage'})
