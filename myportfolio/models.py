from django.db import models
#from django.conf import settings


# Create your models here.
class Personal(models.Model):
    myFirstName = models.CharField(max_length=50, verbose_name='First Name')
    myLastName = models.CharField(max_length=50, verbose_name='Last Name')
    myPic = models.ImageField(upload_to='myportfolio/media', max_length=100, verbose_name='Image')
    #myPic = models.ImageField(upload_to=MEDIA_URL, max_length=100, verbose_name='Image')
    myProfession = models.CharField(max_length=50, verbose_name='Profession')
    myDescription = models.TextField(max_length=500, verbose_name='Description')

    def __str__(self):
        return self.myFirstName

class Contact(models.Model):
    contactName = models.CharField(max_length=50, verbose_name='Contact name')
    contactData = models.CharField(max_length=50, verbose_name='Contact data')

    def __str__(self):
        return self.contactName

class Skill(models.Model):
    skillType = models.CharField(max_length=20, verbose_name='Skill type')
    skillBar = models.IntegerField(blank=True)

    def __str__(self):
        return self.skillType

class History(models.Model):
    historyPosition = models.CharField(max_length=50, verbose_name='History Position')
    historyFirm = models.CharField(max_length=50, verbose_name='History Firm')
    historyDateFrom = models.CharField(blank=True, max_length=10)
    historyDateTo = models.CharField(blank=True, max_length=10)
    historyDescription = models.TextField(max_length=500, verbose_name='History Description')
    historySkills = models.CharField(max_length=100, verbose_name='History Skills')

    def __str__(self):
        return self.historyPosition

class Course(models.Model):
    courseName = models.CharField(max_length=100, verbose_name="Course Name")
    courseDateFrom = models.CharField(blank=True, max_length=10)
    courseDateTo = models.CharField(blank=True, max_length=10)

    def __str__(self):
        return self.courseName

class Portfolio(models.Model):
    portfolioName = models.CharField(max_length=50, verbose_name="Portfolio Name")
    portfolioType = models.CharField(max_length=50, verbose_name="Portfolio Type")
    portfolioMedia = models.ImageField(upload_to='myportfolio/media', max_length=100)
    portfolioURL = models.URLField(blank=True)

    def __str__(self):
        return self.portfolioName
