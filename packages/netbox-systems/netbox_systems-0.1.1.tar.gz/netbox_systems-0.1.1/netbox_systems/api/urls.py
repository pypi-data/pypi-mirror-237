from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_systems'

router = NetBoxRouter()
router.register('pl_systems', views.SystemSerializer)

urlpatterns = router.urls
