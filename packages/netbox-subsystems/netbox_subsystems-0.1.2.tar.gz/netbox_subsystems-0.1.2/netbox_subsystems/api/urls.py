from netbox.api.routers import NetBoxRouter
from .views import SubsystemsViewSet

app_name = 'netbox_subsystems'

router = NetBoxRouter()
router.register('subsystems', SubsystemsViewSet)

urlpatterns = router.urls
