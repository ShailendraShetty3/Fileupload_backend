from django.db import models

class Reviews(models.Model):
    book_id = models.CharField(max_length=300, default='default_book_id')  # Set a default value
    review_author = models.CharField(max_length=200)
    review_date = models.DateField(null=True, blank=True, default=None)
    review_comment = models.CharField(max_length=500)
    
    def __str__(self):
        return self.review_author
