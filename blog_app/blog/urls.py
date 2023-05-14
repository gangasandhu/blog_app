from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:id>', views.post, name='blog-post'),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name='delete-post'),
    path('post/<int:pk>/edit/', views.EditPostView.as_view(), name='edit-post'),
    path('sample/', views.sample, name='sample'),
    path('create/', views.create_post, name='create-post')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)