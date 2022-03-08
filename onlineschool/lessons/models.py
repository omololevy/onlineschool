from django.db import models

# Create your models here.

class Sinflar(models.Model):
    sinf = models.IntegerField(unique=True)
    sinf_text = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.sinf_text

    class Meta:
        verbose_name = "Sinf"
        verbose_name_plural = "Sinflar"


class Fanlar(models.Model):
    sinf = models.ForeignKey(Sinflar, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    duration = models.IntegerField()

    def __str__(self) -> str:
        return str(self.sinf.sinf) + "-sinf " + self.name

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"


class Mavzular(models.Model):
    fan = models.ForeignKey(Fanlar, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Mavzu"
        verbose_name_plural = "Mavzular"

class Amaliyot(models.Model):
    mavzu = models.ForeignKey(Mavzular, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.mavzu.name) + " maruza darsi" + self.name

    class Meta:
        verbose_name = "Maruza dars"
        verbose_name_plural = "Maruza darslar"

class Maruza(models.Model):
    mavzu = models.ForeignKey(Mavzular, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.mavzu.name) + " amaliy darsi" + self.name

    class Meta:
        verbose_name = "Amaliy mashq"
        verbose_name_plural = "Amaliy mashqlar"


