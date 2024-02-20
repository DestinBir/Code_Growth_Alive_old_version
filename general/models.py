from django.db import models

from main.settings import AUTH_USER_MODEL


class Service(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    illustration = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-title"]


class FeedBack(models.Model):
    message = models.CharField(max_length=500)
    author_user = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name="FeedBack",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    author = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.author or self.author_user

    class Meta:
        ordering = ["-message"]
    

