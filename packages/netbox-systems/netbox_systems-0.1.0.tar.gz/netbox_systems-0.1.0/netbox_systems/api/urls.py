from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_systems'

router = NetBoxRouter()
router.register('systems', views.SystemSerializer)

urlpatterns = router.urls
