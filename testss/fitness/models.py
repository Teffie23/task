from django.db import models
from django.urls import reverse, reverse_lazy
class users(models.Model):
    card_series= models.IntegerField(verbose_name='серия карты')
    card_number= models.IntegerField(verbose_name='номер карты')
    date_of_issue_of_the_card= models.DateTimeField(auto_now_add=True)
    date_of_initial_issue_of_the_card= models.DateTimeField(auto_now_add=True)
    date_of_last_use_of_the_card= models.DateTimeField(auto_now=True)
    coach= models.CharField(max_length=255,verbose_name='ФИО Тренера')
    card_status= models.BooleanField(verbose_name='Статус карты')
    subscriber= models.ForeignKey('subscriber',on_delete=models.PROTECT,verbose_name='Абонемент')
    personal_subscriber=models.ForeignKey('personal_subscriber',on_delete=models.PROTECT,verbose_name='Персональная тренировка')
    status_card= models.BooleanField(verbose_name='Статус карты')
    time_status_card=models.ForeignKey('time_status_card',on_delete=models.PROTECT,verbose_name='время статуса тренировки')
class subscriber(models.Model):
    rate = models.CharField(max_length=255,verbose_name='тариф')
    days1=models.IntegerField(verbose_name='Срок активности абонемента')
    def __str__(self):
        return self.rate + str(self.days1)
class personal_subscriber(models.Model):
    title=models.CharField(max_length=255,verbose_name='название')
    days2 = models.IntegerField(verbose_name='Срок активности персональной тренировки')
    def __str__(self):
        return self.title + str(self.days2)
class time_status_card(models.Model):
    name=models.CharField(max_length=255,verbose_name='ФИО')
    status = models.BooleanField(verbose_name='статус')
    personal_subscriber_days_but = models.IntegerField(verbose_name='Количество дней абонемента на данный момент')
    subscriber_days_must=models.IntegerField(verbose_name='Количество дней абонемента должно быть')
    personal_subscriber_days_must=models.IntegerField(verbose_name='Количество дней персональных тренировок должно быть')
    subscriber_days_but=models.IntegerField(verbose_name='Количество дней персональных тренировок на данный момент')

# Create your models here.
