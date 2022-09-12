from django.urls import path, include

from .views import form_view
from .api.router import router


urlpatterns = [
    path('ttask/', form_view),
    path('api/', include((router.urls, 'api')))
]
