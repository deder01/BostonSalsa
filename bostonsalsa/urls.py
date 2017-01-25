"""bostonsalsa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# .. Imports

# Django
from django.conf.urls import url, include
from django.contrib import admin

# Third party
from rest_framework_nested import routers

# Project
from account.views import AccountViewSet
from bostonsalsa.views import IndexView

# .. End Imports

# define routers
router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)


# define the url patterns
urlpatterns = [
    # urls for accounts
    #   /accounts
    #   /accounts/<username>
    #url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', admin.site.urls),

    # all others re-route to home page
    url(r'^.*$', IndexView.as_view(), name='index'),
]
