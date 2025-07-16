from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.db.models import Value, CharField, F
from rest_framework.viewsets import ModelViewSet
from django.contrib.postgres.aggregates import ArrayAgg

from apiapp import models as models_file
from apiapp import forms as forms_file
from django.db import models
from django import forms
import requests


def get_all(model_name: models.Model, *args):
    return model_name.objects.all().order_by(*args)


def add_or_edit(request: requests.Request, 
        form_name: forms.ModelForm,
        instance=None
        ): 
    opts = form_name._meta  
    if instance is None:
            instance = opts.model() 
            opts = form_name._meta  
    if request.method == "POST":
        form = form_name(request.POST, instance=instance)
        if form.is_valid():
            form.save()
    else:
        form = form_name(instance=instance)
        return form
    

