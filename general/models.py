from django.db import models

from main.settings import AUTH_USER_MODEL

STATUS = (
    ('basic', 'BASIC'),
    ('premium', 'PREMIUM'),
    ('pro', 'PRO')
)

class Service(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 500)
    illustration = models.CharField(max_length = 20)

    def __str__(self) -> str:
        return self.title 
    class Meta:
        ordering = ['-title']

class FeedBack(models.Model):
    message = models.CharField(max_length = 500)
    author_user = models.ForeignKey(AUTH_USER_MODEL, related_name = 'FeedBack', blank = True, null = True, on_delete = models.CASCADE)
    author = models.CharField(max_length = 100, blank = True, null = True)
    description = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.author or self.author_user
    class Meta:
        ordering = ['-message']

class Price(models.Model):
    status = models.CharField(max_length = 50, choices=STATUS)
    description = models.CharField(max_length = 100)
    amount = models.IntegerField()
    duration = models.IntegerField()
    limited = models.BooleanField(db_default = True)
    number = models.IntegerField()
    service = models.ForeignKey(Service, related_name = 'price', on_delete = models.CASCADE)

