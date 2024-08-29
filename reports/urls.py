from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('report/', views.report, name='report'),
    path('map/', views.map_view, name='map'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('view-reports/', views.view_reports, name='view_reports'), 
    path('admin/dashboard/', views.admin_view_reports, name='admin_dashboard'),
]


