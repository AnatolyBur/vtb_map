from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'department', DepartmentViewSet)
router.register(r'service', ServiceViewSet)

urlpatterns = router.urls