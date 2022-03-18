from django.contrib import admin
from .models import *
class usersAdmin(admin.ModelAdmin):
    list_display = ('id','card_series','card_number','date_of_issue_of_the_card','date_of_last_use_of_the_card','status_card')
    list_display_links =  ('id','card_series','card_number','date_of_issue_of_the_card','date_of_last_use_of_the_card','status_card')
    search_fields =  ('id','card_series','card_number','date_of_issue_of_the_card','date_of_last_use_of_the_card','status_card')
class subscriberAdmin(admin.ModelAdmin):
    list_display = ('rate','days1')
    list_display_links = ('rate','days1')
    search_fields = ('rate','days1')
class personal_subscriberAdmin(admin.ModelAdmin):
    list_display = ('title','days2')
    list_display_links = ('title','days2')
    search_fields = ('title','days2')
class time_status_cardAdmin(admin.ModelAdmin):
    list_display = ('name','status','subscriber_days_but','subscriber_days_must','personal_subscriber_days_but','personal_subscriber_days_must')
    list_display_links = ('name','status','subscriber_days_but','subscriber_days_must','personal_subscriber_days_but','personal_subscriber_days_must')
    search_fields = ('name','status','subscriber_days_but','subscriber_days_must','personal_subscriber_days_but','personal_subscriber_days_must')
admin.site.register(time_status_card,time_status_cardAdmin)
admin.site.register(personal_subscriber,personal_subscriberAdmin)
admin.site.register(subscriber,subscriberAdmin)
admin.site.register(users,usersAdmin)
admin.site.site_title='Админ-панель сайта о фитнесе'
admin.site.site_headler='Админ-панель фитеса'
# Register your models here.
