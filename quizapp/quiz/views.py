# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login
import json
from django.shortcuts import render
from .models import Question, Attempt

def index(request):
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #    login(request, user)
    questions = Question.objects.all()
    return render(request, "quiz.html", {"questions": questions})

def save_try(request):
    submitted_ans = request.POST
    score = 0
    for key in submitted_ans:
        if key[:6] == "answer":
            test_in = Attempt.create_instance(submitted_ans[key])
            score += test_in["score"]
            test = Attempt(**test_in)
            test.save()
    return render(request, "score.html", {"score": score})