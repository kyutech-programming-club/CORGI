from django.db import models
from django.core import validators

class Valuelec_register(models.Model):
    class_style = (
        (1, '非同期'),
        (2, '同期or対面'),
        (3, '同期と非同期両方'),
    )
    five_evaluation = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    lec_id = models.IntegerField()
    total_evaluation = models.IntegerField(
        '総合評価',
        choices=five_evaluation,
        default=3,
    )
    lec_simplicity = models.IntegerField(
        '講義の簡単さ',
        choices=five_evaluation,
        default=3,
    )
    credit_simplicity = models.IntegerField(
        '単位の取りやすさ',
        choices=five_evaluation,
        default=3,
    )
    task_smallness = models.IntegerField(
        '課題の少なさ',
        choices=five_evaluation,
        default=3,
    )
    class_style = models.IntegerField(
        '授業形態',
        choices=class_style,
        default=1
    )
    comment = models.CharField(
        'コメント',
        max_length=1000,
        blank=True,
    )
    pub_date = models.DateTimeField(
        '登録日',
        auto_now_add=True,
    )



class Lecture(models.Model):
    lec_name = models.CharField(
        '講義名',
        max_length=20,
        unique=True,
        validators=[validators.RegexValidator(
            regex=u'^[ぁ-んァ-ヶー一-龠]+$',
            message='講義名は漢字・ひらがな・カタカナのみです',
        )],
    )

    lec_name_for_url = models.CharField(
        '講義名（ローマ字or英語）',
        max_length=30,
        unique=True,
        validators=[validators.RegexValidator(
            regex=r'^[a-zA-Z]*$',
            message='英数字のみです',
        )],
    )

    teacher_name = models.CharField(
        '教授名',
        max_length=20,
        validators=[validators.RegexValidator(
            regex=u'^[ぁ-んァ-ヶー一-龠]+\u3000[ぁ-んァ-ヶー一-龠]+$',
            message='氏名は漢字・ひらがな・カタカナのみとし、氏と名の間に全角スペースを入れてください',
        )],
    )
