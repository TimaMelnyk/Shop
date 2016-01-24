from django.contrib import admin
from polls.models import *

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','price')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
class ZakazAdmin(admin.ModelAdmin):
    list_display = ('id','name','date')
        
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','firstName','lastName','login','password','phoneNumber')
    


admin.site.register(Item,ItemAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Zakaz,ZakazAdmin)
admin.site.register(User,UserAdmin)
    #code
