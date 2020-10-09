from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True) # blank pozwala nam decydować, czy URL ma byc dostępne np. po kliknięciu obrazka - TRUE, czy też ma być chwilowo niedostepne - FALSE - by default it is set to FALSE