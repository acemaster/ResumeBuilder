# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from main.models import PersonalProfile,Section

# Register your models here.
admin.site.register(PersonalProfile)
admin.site.register(Section)