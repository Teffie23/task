# Generated by Django 3.2.9 on 2022-03-16 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='personal_subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('days2', models.IntegerField(verbose_name='Срок активности персональной тренировки')),
            ],
        ),
        migrations.CreateModel(
            name='subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(max_length=255, verbose_name='тариф')),
                ('days1', models.IntegerField(verbose_name='Срок активности абонемента')),
            ],
        ),
        migrations.CreateModel(
            name='time_status_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('status', models.BooleanField(verbose_name='статус')),
                ('personal_subscriber_days_but', models.IntegerField(verbose_name='Количество дней абонемента на данный момент')),
                ('subscriber_days_must', models.IntegerField(verbose_name='Количество дней абонемента должно быть')),
                ('personal_subscriber_days_must', models.IntegerField(verbose_name='Количество дней персональных тренировок должно быть')),
                ('subscriber_days_but', models.IntegerField(verbose_name='Количество дней персональных тренировок на данный момент')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_series', models.IntegerField(verbose_name='серия карты')),
                ('card_number', models.IntegerField(verbose_name='номер карты')),
                ('date_of_issue_of_the_card', models.DateTimeField(auto_now_add=True)),
                ('date_of_initial_issue_of_the_card', models.DateTimeField(auto_now_add=True)),
                ('date_of_last_use_of_the_card', models.DateTimeField(auto_now=True)),
                ('coach', models.CharField(max_length=255, verbose_name='ФИО Тренера')),
                ('card_status', models.BooleanField(verbose_name='Статус карты')),
                ('status_card', models.BooleanField(verbose_name='Статус карты')),
                ('personal_subscriber', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fitness.personal_subscriber', verbose_name='Персональная тренировка')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fitness.subscriber', verbose_name='Абонемент')),
                ('time_status_card', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fitness.time_status_card', verbose_name='время статуса тренировки')),
            ],
        ),
    ]