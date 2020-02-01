from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """ Message Admin Definitions """

    pass


@admin.register(models.Conversation)
class ConversationsAdmin(admin.ModelAdmin):

    """ Conversation Admin Definitions """

    pass
