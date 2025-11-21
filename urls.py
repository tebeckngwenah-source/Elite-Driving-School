import debug_toolbar
from django.contrib import admin
from django.urls import path,include
from . import views
from django.urls import path
# from unfold.contrib.filters.urls import get_urls

urlpatterns = [
    # path('admin/filters/', get_urls()),  # If using filters
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', views.home_page, name='index'),
    path('course/', views.course_add, name= 'courses'),
    path('user/', views.users, name = 'user'),
    path('accounts/', include('account.urls'))
]
