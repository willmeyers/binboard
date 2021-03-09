from .routers import public_posts_router, user_posts_router


app_name = 'posts'


urlpatterns = [

] + public_posts_router.urls + user_posts_router.urls
