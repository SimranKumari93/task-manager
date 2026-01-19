from rest_framework.routers import DefaultRouter
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = router.urls

class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
