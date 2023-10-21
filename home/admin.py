from django.contrib import admin
from home.models import Home, Contact, Order, GetJob ,Softwares,SoftwareType
# Register your models here.

# superuser name - recxo , email - regular, password - recxo098
# user for experiment name - jay, password - jignesh6^^9


# these all classes will arrange the list shown on the django admin.

class HomeAdmin(admin.ModelAdmin):
    list_display = ("fullname", "username",'email' )


admin.site.register(Home,HomeAdmin),


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email",)


admin.site.register(Contact,ContactAdmin),


class OrderAdmin(admin.ModelAdmin):
    list_display = ("soft_name",'soft_amount' )


admin.site.register(Order, OrderAdmin),


class JobAdmin(admin.ModelAdmin):
    list_display = ("name", "UserName", "email", "jobrole")


admin.site.register(GetJob, JobAdmin)

admin.site.register(Softwares)

admin.site.register(SoftwareType)
