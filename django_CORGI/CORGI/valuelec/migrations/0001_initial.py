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
                ('lec_name', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='講義名は漢字・ひらがな・カタカナのみです', regex='^[ぁ-んァ-ヶー一-龠]+$')], verbose_name='講義名')),
                ('teacher_name', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='氏名は漢字・ひらがな・カタカナのみとし、氏と名の間に全角スペースを入れてください', regex='^[ぁ-んァ-ヶー一-龠]+$')], verbose_name='教授名')),
            ],
        ),
        migrations.CreateModel(
            name='Valuelec_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_evaluation', models.CharField(choices=[('★', '★'), ('★★', '★★'), ('★★★', '★★★'), ('★★★★', '★★★★'), ('★★★★★', '★★★★★')], max_length=7, verbose_name='総合評価')),
                ('lec_simplicity', models.CharField(choices=[('★', '★'), ('★★', '★★'), ('★★★', '★★★'), ('★★★★', '★★★★'), ('★★★★★', '★★★★★')], max_length=7, verbose_name='講義の簡単さ')),
                ('credit_simplicity', models.CharField(choices=[('★', '★'), ('★★', '★★'), ('★★★', '★★★'), ('★★★★', '★★★★'), ('★★★★★', '★★★★★')], max_length=7, verbose_name='単位の取りやすさ')),
                ('task_smallness', models.CharField(choices=[('★', '★'), ('★★', '★★'), ('★★★', '★★★'), ('★★★★', '★★★★'), ('★★★★★', '★★★★★')], max_length=7, verbose_name='課題の少なさ')),
                ('class_style', models.CharField(choices=[('非同期', '非同期'), ('同期or対面', '同期or対面'), ('同期と非同期両方', '同期と非同期両方')], max_length=15, verbose_name='授業形態')),
                ('comment', models.TextField(blank=True, max_length=1000, verbose_name='コメント')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='登録日')),
                ('the_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valuelec.lecture', verbose_name='講義名')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, max_length=1000, verbose_name='コメント')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='質問日')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valuelec.lecture', verbose_name='講義名')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(blank=True, max_length=1000, verbose_name='コメント')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='回答日')),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='valuelec.question', verbose_name='回答')),
            ],
        ),
    ]
