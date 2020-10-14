from django.db import models

# Create your models here.
class Books(models.Model):
    name= models.CharField(max_length=40)
    author = models.CharField(max_length=50)
    published_date = models.IntegerField()
    price = models.IntegerField()
    profile_photo= models.ImageField(upload_to='book_photos', default='sanjog.jpg')

    def __str__(self):
        return self.name

class Teachers(models.Model):
    english = models.CharField(max_length=25)
    maths= models.CharField(max_length=25)
    science= models.CharField(max_length=25)

    def __str__(self):
        return self.english

class Tutorials(models.Model):
    subject= models.ForeignKey(Teachers, on_delete=models.CASCADE, null= True)
    teacher= models.CharField(max_length=25)
    date_submission= models.IntegerField()

    def __str__(self):
        return self.subject

class Assignments(models.Model):
    subject=models.CharField(max_length=25)
    teacher= models.OneToOneField(Teachers, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

class Students(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField()
    submit=models.ManyToManyField(Books)

    def __str__(self):
        return self.submit










