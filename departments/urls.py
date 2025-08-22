from rest_framework import routers
from .views import DepartmentViewSet

router = routers.DefaultRouter()
router.register(r'departments', DepartmentViewSet)

urlpatterns = router.urls
