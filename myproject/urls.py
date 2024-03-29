"""google URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views as auth_views
from userapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login,name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('social-auth/',include('social_django.urls',namespace='social')),
    # path('oauth/',include('social_django.urls',namespace='social2')),
    path('',views.home,name='home'),
    # path('upimage/',include('img.urls')),
    path("",views.home),
    path("LogIn",views.LogIn),
    path("forgot",views.forgot),
    path("changepass",views.changepass),
    path("otpvar",views.otpvar),
    path("passwordchange",views.passwordchange),
    path("SignUp",views.SignUp),
    path("checklogin",views.checklogin),
    path("savedata",views.savedata),
    path("Admin",views.Admin),
    path("writepost",views.writepost),
    path("post",views.post),
    path("home2",views.home2),
    path("preview",views.preview),
    path("Del",views.Del),
    path("Faculty",views.Faculty),
    path("Deletepost",views.Deletepost),
    path("useredit",views.useredit),
    path("passchange",views.passchange),
    path("blogDelete",views.blogDelete),
    path("savemsg",views.savemsg),


    # path('addproduct',views.addproduct),
    # path('show',views.show),
]
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

