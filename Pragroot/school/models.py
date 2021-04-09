from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    REQUIRED_FIELDS = ['email']
    

    def __str__(self):
        return self.email
    
    class Meta:
        unique_together = ('email',)
    

class Teacher(models.Model):
    ROLES = [
        ('AD', 'Administrator'),
        ('AS', 'Assistant'),
        ('RT', 'Regular Teacher'),
    ]
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    teaching_since = models.DateTimeField(auto_now_add=True)
    instrument = models.CharField(max_length=200)
    # email = models.EmailField()
    role = models.CharField(max_length=30, choices=ROLES, null=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Teacher')
        verbose_name_plural = ("Teachers")

    def __str__(self):
        return self.user.username
    


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    skill_level = models.IntegerField(help_text="Please Enter between 1 to 10")
    instrument = models.CharField(max_length=200)
    student_since = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    birthday = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ('Student')
        verbose_name_plural = ("Students")

    def __str__(self):
        return self.first_name + " " + self.last_name


class School(models.Model):
    school_name = models.CharField(max_length=205)
    address = models.CharField(max_length=300)
    phone_number = models.IntegerField()

    class Meta:
        verbose_name = ('School')
        verbose_name_plural = ('School(s)')
    

    def __str__(self):
        return self.school_name



