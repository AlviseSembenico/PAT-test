"""pat_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from ajax_select import urls as ajax_select_urls
from django.views.generic.base import RedirectView


admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PAT.urls')),
    path('ajax_select/', include(ajax_select_urls)),
    path('accounts/login/', RedirectView.as_view(url='/admin/login?next=/', permanent=False)),
]
