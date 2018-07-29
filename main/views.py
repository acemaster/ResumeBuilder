# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from main.models import PersonalProfile,Section


def home(request):
	response = {}
	profiles = PersonalProfile.objects.all()
	if len(profiles) == 0 :
		return render(request,'404.djt',{})
	response['profile'] = profiles[0]
	sections = Section.objects.all()
	response['sections'] = {}
	for section in sections:
		if section.title in response['sections']:
			response['sections'][section.title].append(section)
		else:
			response['sections'][section.title] = []
			response['sections'][section.title].append(section)
	return render(request,'index.djt',response)

