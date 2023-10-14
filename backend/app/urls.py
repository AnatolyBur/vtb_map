from garpixcms.urls import *  # noqa
from django.conf import settings

API_URL = getattr(settings, 'API_URL', 'api')


urlpatterns = [
    path(f'{API_URL}/', include('bank.urls'))   # noqa: F405
] + urlpatterns  # noqa
