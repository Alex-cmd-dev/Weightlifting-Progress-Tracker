from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts")  
    def __str__(self):
        return f"Workout on {self.date.strftime('%Y-%m-%d')} by {self.user.username}"

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="exercises")  
    name = models.CharField(max_length=100)  
    sets = models.PositiveIntegerField()  
    reps = models.PositiveIntegerField()  
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # Weight lifted (up to 999.99)

    def __str__(self):
        return f"{self.name} ({self.sets}x{self.reps} @ {self.weight}kg)"
