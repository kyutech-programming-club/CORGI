# Generated by Django 3.1.3 on 2020-12-04 12:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lec_name', models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(message='講義名は漢字・ひらがな・カタカナのみです', regex='^[ぁ-んァ-ヶー一-龠]+$')], verbose_name='講義名')),
                ('teacher_name', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='氏名は漢字・ひらがな・カタカナのみとし、氏と名の間に全角スペースを入れてください', regex='^[ぁ-んァ-ヶー一-龠]+\u3000[ぁ-んァ-ヶー一-龠]+$')], verbose_name='教授名')),
            ],
        ),
        migrations.CreateModel(
            name='Valuelec_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_evaluation', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3, verbose_name='総合評価')),
                ('lec_simplicity', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3, verbose_name='講義の簡単さ')),
                ('credit_simplicity', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3, verbose_name='単位の取りやすさ')),
                ('task_smallness', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3, verbose_name='課題の少なさ')),
                ('class_style', models.IntegerField(choices=[(1, '非同期'), (2, '同期or対面'), (3, '同期と非同期両方')], default=1, verbose_name='授業形態')),
                ('comment', models.CharField(blank=True, max_length=1000, verbose_name='コメント')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
                ('the_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valuelec.lecture')),
            ],
        ),
    ]
