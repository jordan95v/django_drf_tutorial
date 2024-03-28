from django.urls import URLPattern, path
from apps.api.views import SnippetList

urlpatterns: list[URLPattern] = [
    path("snippets/", SnippetList.as_view(), name="snippet-list"),
]
