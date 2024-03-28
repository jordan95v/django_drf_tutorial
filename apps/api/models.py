from typing import Final
from django.db import models

LANGUAGES: Final[list[tuple[str, str]]] = [
    ("python", "Python"),
    ("javascript", "JavaScript"),
    ("html", "HTML"),
    ("css", "CSS"),
    ("java", "Java"),
    ("c", "C"),
    ("cpp", "C++"),
    ("csharp", "C#"),
    ("php", "PHP"),
    ("ruby", "Ruby"),
    ("perl", "Perl"),
    ("bash", "Bash"),
    ("powershell", "PowerShell"),
    ("sql", "SQL"),
    ("plaintext", "Plain Text"),
]


class Snippet(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    language = models.CharField(
        choices=LANGUAGES, max_length=100, null=False, blank=False
    )
    code = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
