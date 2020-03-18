
from django.contrib import admin
#from django.utils.translation import ugettext_lazy as _
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#from .models import Occurrence


#class OccProfileInline(admin.StackedInline):
#    model = Occurrence
#    can_delete = False#


#@admin.register(Occurrence)
#class OccAdmin(BaseUserAdmin):
#    fieldsets = (
#        (None, {'fields': ('email', 'password')}),
#    )
#    list_display = ('description', 'location', 'creator', 'creation_date','update_date','status')
#    search_fields = ('location', 'creator', 'status')
#    ordering = ('creation_date',)
#    inlines = (OccProfileInline, )