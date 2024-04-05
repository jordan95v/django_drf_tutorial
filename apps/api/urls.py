from django.urls import URLPattern, path, include
from rest_framework.routers import DefaultRouter
from apps.api.views import SnippetViewSet, UserList, UserDetails

router: DefaultRouter = DefaultRouter()
router.register("snippets", SnippetViewSet, basename="snippet")

urlpatterns: list[URLPattern] = [
    path("", include(router.urls)),
    path("users/", UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetails.as_view(), name="user-detail"),
]
