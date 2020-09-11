from django.db import models
from django.core.exceptions import NON_FIELD_ERRORS

# Create your models here.


LANGUAGES = [
    ('RU', "Русский"),
    ('EN', "Английский"),
    ('UA', "Украинский"),
    ('PO', "Португальский"),
]


class Person(models.Model):
    first_name = models.CharField(
        "имя",
        max_length=30,
        help_text="Введите имя"
    )
    last_name = models.CharField("фамилия", max_length=30, help_text="Введите фамилию")
    age = models.IntegerField("возраст", help_text="Введите возраст")
    active = models.BooleanField("активность", default=True, help_text="Активен ли")
    avatar = models.ImageField("аватар", upload_to="images", null=True, blank=True, help_text="Загрузите фото")
    languages = models.CharField("языки", choices=LANGUAGES, max_length=2, null=True, blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name[0]}."
