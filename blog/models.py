from django.db import models

class Blog(models.Model):
    GENERAL = 'General'
    WORK = 'Work'
    BUSINESS = 'Business'
    FOOD = 'Food'
    MOVIES = 'Movies'
    BOOKS = 'Books'
    MOM = 'Mom'
    TRAVEL = 'Travel'
    LIFESTYLE = 'Lifestyle'
    DIY = 'DIY'
    PARENTING = 'Parenting'
    SOCIAL = 'Social'
    STUDY= 'Study'
    DAILY= 'Daily'
    CATEGORY_CHOICES = [
        (GENERAL, 'General'),
        (WORK, 'Work'),
        (BUSINESS, 'Business'),
        (FOOD, 'Food'),
        (MOVIES, 'Movies'),
        (BOOKS, 'Books'),
        (MOM, 'Mom'),
        (TRAVEL, 'Travel'),
        (LIFESTYLE, 'Lifestyle'),
        (DIY, 'Diy'),
        (PARENTING, 'Parenting'),
        (SOCIAL, 'Social'),
        (STUDY, 'Study'),
        (DAILY, 'Daily'),
    ]
    category = models.CharField(max_length=255,choices=CATEGORY_CHOICES,default=GENERAL)
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] + str(' ...')

    def pub_date_pretty(self):
        return self.pub_date.strftime('%B %e, %Y')
