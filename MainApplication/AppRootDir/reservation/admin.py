from django.contrib import admin
from .models import Table, Reservation

# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_id','cap','occupied')# 要显示哪些信息
    list_display_links = ('table_id',)#点击哪些信息可以进入编辑页面
    search_fields = ['table_id']   #指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
    list_filter =['table_id']#指定列表过滤器，右边将会出现一个快捷的过滤选项

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('rsv_number','table_id','user','date','rsv_time','expired')# 要显示哪些信息
    list_display_links = ('rsv_number',)#点击哪些信息可以进入编辑页面
    search_fields = ['rsv_number']   #指定要搜索的字段，将会出现一个搜索框让管理员搜索关键词
    list_filter =['rsv_number']#指定列表过滤器，右边将会出现一个快捷的过滤选项