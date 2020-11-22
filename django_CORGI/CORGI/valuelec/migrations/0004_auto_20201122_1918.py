# Generated by Django 3.1.3 on 2020-11-22 10:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valuelec', '0003_auto_20201122_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='total_evaluation',
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lec_name',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='講義名は漢字・ひらがな・カタカナのみです', regex='^[ぁ-んァ-ヶー一-龠]+$')], verbose_name='講義名'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='teacher_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='氏名は漢字・ひらがな・カタカナのみとし、氏と名の間に全角スペースを入れてください', regex='^[ぁ-んァ-ヶー一-龠]+\u3000[ぁ-んァ-ヶー一-龠]+$')], verbose_name='教授名'),
        ),
        migrations.AlterField(
            model_name='valuelec_register',
            name='lec_id',
            field=models.IntegerField(),
        ),
    ]
