from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import LoginView, SignupView
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('role/', RedirectView.as_view(url="/admin/"), name="go-to-admin"),
    path('registrations/login', LoginView.as_view(), name='login'),
    path('registrations/signup', SignupView.as_view(), name='signup'),
]
