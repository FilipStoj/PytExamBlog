from django.db import models
from django.utils import timezone
# Importing Users. Post model og User model kommer til at have en relationship fordi users kommer til at skrive posts.
# Det one to many relationship. Fordi en User kan have flere post, men en post kan kun have en forfatter. (Foreign key)
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    Titel = models.CharField(max_length=100)
    Content = models.TextField()
    Dato = models.DateTimeField(default=timezone.now)
    # On_delete fordi vi skal fortælle django hvad vi vil gøre hvis Useren som oprettede posted bliver slettet = Post bliver sletet (CASCADE). 
    Forfatter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Titel

    # Opretter "get absolute URL metode" for at fortælle Django hvordan den skal finde URL'en til enhver specifik instance af et post.
    def get_absolute_url(self):
        # Reverse vil returnere den fulde path som en string 
        return reverse('post-detail', kwargs={'pk': self.pk})