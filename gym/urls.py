from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path

from gym.views import index, explore_more, watch_video, weight_lifting, select_plan, render_post, EmailView
from gym.views import LoginView, RegisterView
from gym.views import payment


urlpatterns = [
    path('', index, name='index'),
    path('explore-more/', explore_more, name='explore-more'),
    path('watch-video/', watch_video, name='watch-video'),
    path('weight-lifting/', weight_lifting, name='weight_lifting'),
    path('select-plan/', select_plan, name='select-plan'),
    path('payment/', payment, name='payment'),
    path('blog/', render_post, name='blog'),
    path('subscribe/', EmailView.as_view(), name='subscribe'),


    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)