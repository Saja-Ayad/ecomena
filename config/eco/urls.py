from . import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('blog1', views.PostList.as_view(), name='post'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
  
    path('contact/', views.contact, name='contact'),
    path("", views.index, name="index"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)