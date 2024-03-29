from django.urls import URLPattern, path
from apps.api.views import SnippetList, SnippetDetail, UserList

urlpatterns: list[URLPattern] = [
    path("snippets/", SnippetList.as_view(), name="snippet-list"),
    path("snippets/<int:pk>/", SnippetDetail.as_view(), name="snippet-detail"),
    path("users/", UserList.as_view(), name="user-list"),
]
