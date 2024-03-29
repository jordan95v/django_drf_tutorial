from django.urls import URLPattern, path
from apps.api.views import SnippetList, SnippetDetail, UserDetails, UserList

urlpatterns: list[URLPattern] = [
    path("snippets/", SnippetList.as_view(), name="snippet-list"),
    path("snippets/<int:pk>/", SnippetDetail.as_view(), name="snippet-detail"),
    path("users/", UserList.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetails.as_view(), name="user-detail"),
]
