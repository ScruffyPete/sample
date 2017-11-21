from rest_framework import routers

from clients import views

router = routers.SimpleRouter()
router.register('', views.ClientViewSet, base_name='clients')

urlpatterns = router.urls
