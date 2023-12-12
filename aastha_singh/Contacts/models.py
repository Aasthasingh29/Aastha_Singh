from django.db import models

# Create your models here.
class Contact(models.Model):

    # Fields of the model
    contact_name =  models.CharField(max_length=50)
    contact_email = models.CharField(max_length=200)
    contact_created_time = models.DateTimeField(auto_now_add=True, )
    contact_notes = models.TextField()

    def __str__(self):
        return self.contact_name