from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.timezone import now
import uuid
# Create your models here.
User = get_user_model()

class Book(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cover = models.ImageField(blank=True, upload_to='media/cover/%Y/%m/%d')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_date = models.DateTimeField(default=now())
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        permissions = [
            ('Special_status', 'Can read all books')
        ]
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk':self.pk})
    
    
    
class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)