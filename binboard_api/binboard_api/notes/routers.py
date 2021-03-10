from rest_framework import routers

from .viewsets import PublicNoteViewSet, UserNoteViewSet


public_note_router = routers.DefaultRouter()
public_note_router.register('notes', PublicNoteViewSet)

user_note_router = routers.DefaultRouter()
user_note_router.register('user/notes', UserNoteViewSet)
