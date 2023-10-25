from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_subsystems'

router = NetBoxRouter()
router.register('subsystems', views.SubsystemSerializer)

urlpatterns = router.urls
