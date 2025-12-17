from django.contrib import admin
from .models import PollOptionModel,PollsModel,UserModel,VotesModel
# Register your models here.
@admin.register(VotesModel)
class VotesAdmin(admin.ModelAdmin):
    list_display= ("option_id",)
    list_filter=('option_id',)
    search_fields=('option_id',)
    list_display_links=('option_id',)

    pass
@admin.register(PollOptionModel)
class PollOptionAdmin(admin.ModelAdmin):
    list_display=("option_text","poll_id",)
    list_filter=('option_text',)
    search_fields=('option_text',)
    list_display_links=('option_text',)

    pass
@admin.register(PollsModel)
class PollsAdmin(admin.ModelAdmin):
    list_display=("title",'description',)
    list_filter=('title',)
    search_fields=('title',)
    list_display_links=('title','description',)

    pass
"""
@admin.register(UserModel)
class VotesAdmin(admin.ModelAdmin):
    pass
"""