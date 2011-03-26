from django.db import models

class Driver:
    forename = models.CharField(
        max_length = 30
    )
    
    surname = models.CharField(
        max_length = 30,
        db_index = True
    )
    
    @property
    def name(self):
        '%s %s' % (forename, surname)
        
class Team:
    name = models.CharField(
        max_length = 30,
        db_index = True
    )
    
class Car:
    num = models.PositiveSmallIntegerField(
        unique = True
    )
    
    driver = models.ForeignKey(Driver,
        unique = True
    )
    
    team = models.ForeignKey(Team)
    
    class Meta:
        unique_together = ("driver", "team")
        
class Race:
    name = models.CharField(
        max_length = 30
    )
    
    date = models.DateField(
        db_index = True
    )