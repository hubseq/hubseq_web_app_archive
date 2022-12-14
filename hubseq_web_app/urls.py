"""HubSeq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.documentation import include_docs_urls, get_schemajs_view

from apps.teams.urls import team_urlpatterns as single_team_urls
from apps.subscriptions.urls import team_urlpatterns as subscriptions_team_urls
from apps.web.urls import team_urlpatterns as web_team_urls

schemajs_view = get_schemajs_view(title="API")

# urls that are unique to using a team should go here
team_urlpatterns = [
    path('', include(web_team_urls)),
    path('subscription/', include(subscriptions_team_urls)),
    path('team/', include(single_team_urls)),
    path('example/', include('apps.teams_example.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/<slug:team_slug>/', include(team_urlpatterns)),
    path('accounts/', include('allauth.urls')),
    path('users/', include('apps.users.urls')),
    path('subscriptions/', include('apps.subscriptions.urls')),
    path('teams/', include('apps.teams.urls')),
    path('', include('apps.web.urls')),
    path('pegasus/', include('pegasus.apps.examples.urls')),
    path('pegasus/employees/', include('pegasus.apps.employees.urls')),
    path('celery-progress/', include('celery_progress.urls')),
    # File explorer
    path('files/', include('apps.files.urls')),
    # API docs
    # these are needed for schema.js
    path('docs/', include_docs_urls(title='API Docs')),
    path('schemajs/', schemajs_view, name='api_schemajs'),
    # djstripe urls - for webhooks
    path("stripe/", include("djstripe.urls", namespace="djstripe")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
