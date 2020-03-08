# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    question_txt = models.CharField(max_length=200)

    def __str__(self):
        return self.question_txt

class Answer(models.Model):
    id = models.IntegerField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans_txt = models.CharField(max_length=200)
    is_correct = models.BooleanField()

    def __str__(self):
        return str(self.question_id) + ": " + self.ans_txt

class Attempt(models.Model):
    try_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    question_id = models.ForeignKey(Question)
    answer_id = models.ForeignKey(Answer)
    score = models.SmallIntegerField()

    def __str__(self):
        return str(self.try_id) + " with score " + str(self.score)

    @classmethod
    def create_instance(cls, ans):
        db_ans = Answer.objects.get(id=ans)
        return {"user_id": 1, "question_id": db_ans.question_id, "answer_id": db_ans,
                "score": 1 if db_ans.is_correct else 0}