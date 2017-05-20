from django.contrib.admin.sites import AdminSite
from django.contrib.auth.admin import UserAdmin,GroupAdmin
from django.contrib.auth.admin import User,Group

#admin site
class MyAdminSite(AdminSite):
    site_header = "WhatIthink Admin"
    site_title = "WhatIthink Admin"

myAdminSite= MyAdminSite()
myAdminSite.register(User,UserAdmin)
myAdminSite.register(Group,GroupAdmin)
