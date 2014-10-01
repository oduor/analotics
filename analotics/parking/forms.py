#!/usr/bin/env python
# encoding: utf-8

from django import forms

class CheckInForm(forms.Form):
    license = forms.FileField()
