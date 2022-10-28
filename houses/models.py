from django.db import models

# Create your models here.
class House(models.Model):
    """
    Model Definition for Houses
    """

    name = models.CharField(max_length=140, verbose_name="이름")
    price_per_night = models.PositiveIntegerField(verbose_name="가격", help_text="Positive Numbers Only")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
