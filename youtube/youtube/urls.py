
from django.contrib import admin
from django.urls import path
from websit import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base_view),
    path('z/', views.z_view),
    path('k/', views.k_view),
]
