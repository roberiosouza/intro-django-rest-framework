# from django.urls import path
# from app.views import TodoListAndCreate, TodoDetailChangeAndDelete

# urlpatterns = [
#     path('', TodoListAndCreate.as_view()),
#     path('<int:pk>/', TodoDetailChangeAndDelete.as_view()),
# ]

from rest_framework.routers import DefaultRouter
from app.views import TodoViewSet

router = DefaultRouter()
router.register(r'', TodoViewSet)
urlpatterns = router.urls