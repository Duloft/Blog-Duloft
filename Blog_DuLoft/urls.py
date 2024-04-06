"""
URL configuration for Blog_DuLoft project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from simple_sso.sso_client.client import Client
test_client = Client(settings.SSO_SERVER, settings.SSO_PUBLIC_KEY, settings.SSO_PRIVATE_KEY)

admin.site.site_header = "DuLoft DashBoard"
print(test_client.get_urls())
urlpatterns = [
    re_path(r'^server/', include(test_client.get_urls())),
    path('back-in/', admin.site.urls),
    path('', include('blog.urls')),
    path('join-us/', include('waitlist.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('froala_editor/',include('froala_editor.urls')) 
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



    
    
    