from django.contrib import admin
from .models import UserAccount
from django.utils import timezone

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ("name", "lastname", "email", "age")
    list_filter = ("name","email")
    actions = ("set_emails_to_null", )
    search_fields = ("is_staff", )
    fields = (("name", "lastname"), "email", "age")
    list_per_page = 20
    

    def get_ordering(self, request):
        if request.user.is_superuser:
            return ("name", "is_staff")
        return ("email", )
    
    
    def set_emails_to_null(self, request, queryset):
        email_status = queryset.update(email="")
        self.message_user(request, "{}the selected users emails seted to none successfully".format(email_status))

    set_emails_to_null.short_description = "mark selected users emails to none"
        
         
admin.site.register(UserAccount, UserAccountAdmin)


