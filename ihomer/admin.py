from django.contrib import admin
from ihomer.models import NodePost


# Register your models here.
class NodePostAdmin(admin.ModelAdmin):
    list_display = ['nodeid', 'nodename', 'nodestatus', 'nodetime']


admin.site.register(NodePost, NodePostAdmin)
# Register your models here.
