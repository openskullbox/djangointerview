# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Answer, Attempt


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Attempt)