from django.db import models
from django.core import validators


class Lecture(models.Model):
    lec_name = models.CharField(
        '講義名',
        max_length=20,
        validators=[validators.RegexValidator(
            regex=u'^[ぁ-んァ-ヶー一-龠]+$',
            message='講義名は漢字・ひらがな・カタカナのみです',
        )],
    )
    teacher_name = models.CharField(
        '教授名',
        max_length=20,
        validators=[validators.RegexValidator(
            regex=u'^[ぁ-んァ-ヶー一-龠]+$',
            message='氏名は漢字・ひらがな・カタカナのみとし、氏と名の間に全角スペースを入れてください',
        )],
    )
    def __str__(self):
        set =  self.lec_name + "   " + self.teacher_name
        return set

class Valuelec_register(models.Model):
    class_style = (
        ('非同期', '非同期'),
        ('同期or対面', '同期or対面'),
        ('同期と非同期両方', '同期と非同期両方'),
    )
    five_evaluation = (
        ('★', '★'),
        ('★★', '★★'),
        ('★★★', '★★★'),
        ('★★★★', '★★★★'),
        ('★★★★★', '★★★★★'),
    )
    the_class = models.ForeignKey(
        Lecture,
        verbose_name='講義名',
        on_delete=models.CASCADE
        )
    total_evaluation = models.CharField(
        '総合評価',
        choices=five_evaluation,
        max_length=7,
    )
    lec_simplicity = models.CharField(
        '講義の簡単さ',
        choices=five_evaluation,
        max_length=7,
    )
    credit_simplicity = models.CharField(
        '単位の取りやすさ',
        choices=five_evaluation,
        max_length=7,
    )
    task_smallness = models.CharField(
        '課題の少なさ',
        choices=five_evaluation,
        max_length=7,
    )
    class_style = models.CharField(
        '授業形態',
        choices=class_style,
        max_length=15,
    )
    comment = models.TextField(
        'コメント',
        max_length=1000,
        blank=True,
    )
    pub_date = models.DateTimeField(
        '登録日',
        auto_now_add=True,
    )

class Question(models.Model):
    question_id = models.ForeignKey(
        Lecture,
        verbose_name='講義名',
        on_delete=models.CASCADE,
    )
    question = models.TextField(
        'コメント',
        max_length=1000,
        blank=True,
    )
    pub_date = models.DateTimeField(
        '質問日',
        auto_now_add=True,
    )

    def __str__(self):
        return self.question

class Answer(models.Model):
    answer_id = models.ForeignKey(
        Question,
        verbose_name='回答',
        on_delete=models.CASCADE,
    )
    answer = models.TextField(
        'コメント',
        max_length=1000,
        blank=True,
    )
    pub_date = models.DateTimeField(
        '回答日',
        auto_now_add=True,
    )
