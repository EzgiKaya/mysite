from django.db import models



class Gebruikers(models.Model):
    GebruikersID = models.CharField(max_length=20)

    
class Reviews(models.Model):
    ReviewID = models.IntegerField(max_length=10)
    ReviewTekst = models.CharField(max_length=500)
    ReviewTitel = models.CharField(max_length=50)
    ReviewRating = models.IntegerField(max_length=5)
    Datum = models.DateTimeField('date published')
    Goedgekeurd = models.NullBooleanField()
    GebruikersID = models.ForeignKey(Gebruikers)
