from .routers import public_note_router, user_note_router


app_name = 'notes'


urlpatterns = [

] + public_note_router.urls + user_note_router.urls
