"""
URL configuration for publicblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
# from publicblog.views import custom_upload_view
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views as ckeditor_views
from django.urls import re_path
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    # Account URLs
    path("account/", include('accounts.urls'), name="account"),
    # Post URLs
    path("", include('posts.urls')),
        # Favicon URL
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon/favicon.ico'))),

    
    # path('ckeditor/',include("ckeditor_uploader.urls")), 

# path('ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
# path('ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)), name='ckeditor_browse'),

path('ckeditor/upload/',ckeditor_views.upload, name='ckeditor_upload'),
path('ckeditor/browse/', never_cache(ckeditor_views.browse), name='ckeditor_browse'),  

path('firebase_messaging_sw.js', serve, {'path': 'firebase_messaging_sw.js', 'document_root': settings.BASE_DIR}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

