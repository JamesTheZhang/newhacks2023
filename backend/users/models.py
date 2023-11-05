from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from multiselectfield import MultiSelectField

class UserProfile(models.Model):
    class GenderChoices(models.TextChoices):
        Male = 'Male'
        Female = 'Female'
        Other = 'Other'

    class LocationChoices(models.TextChoices):
        Robarts = "Robarts"
        University_College_Library = "University College Library"
        Sandford_Fleming_Library = "Sandford Fleming Library"
        Knox_College_Library = "Knox College Library"
        Bahen = "Bahen"
        Myhal = "Myhal"
        Hart_House = "Hart House"

    class InterestChoices(models.TextChoices):
        sports = "sports"
        animals = "animals"
        movies = "movies"
        gaming = "gaming"
        music = "music"
        literature = "literature"
        magic = "magic"
        cooking = "cooking"
        hiking = "hiking"
        gym_and_fitness = "gym and fitness"
        dance = "dance"
        technology = "technology"
        fashion = "fashion"
        photography = "photography"
        travel = "travel"
        arts_and_crafts = "arts and crafts"
        knitting = "knitting"
        pottery = "pottery"
        volunteering = "volunteering"
        skiing_and_snowboarding = "skiing and snowboarding"
        robotics = "robotics"
        coding = "coding"

    class MajorChoices(models.TextChoices):
        engineering = "engineering"
        business = "business"
        physics = "physics"
        math = "math"
        science = "science"
        political_science = "political science"
        nursing = "nursing"
        life_science = "life_science"
        health_science = "health science"
        arts = "arts"
        computer_science = "computer science"
        humanities = "humanities"
        social_sciences = "social sciences"

    class YearChoices(models.IntegerChoices):
        first = 1
        second = 2
        third = 3
        fourth = 4
        fifth = 5

    # Associated user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Preference Data
    gender = models.CharField(choices=GenderChoices.choices, max_length=100, blank=False, default="Unspecified")
    same_gender_pref = models.BooleanField(blank=False, null=False, default=False)
    fav_location = models.CharField(choices=LocationChoices.choices, max_length=100, blank=False, default="None")
    cur_longitude = models.FloatField(default=0.0)
    cur_latitude = models.FloatField(default=0.0)
    major = models.CharField(choices=MajorChoices.choices, max_length=100, blank=False, default="Unspecified")
    year_of_study = models.PositiveSmallIntegerField(choices=YearChoices.choices, blank=False, default=0)
    interests = MultiSelectField(choices=InterestChoices.choices, max_choices=3, max_length=100, blank=False, default="Unspecified")

    # Used to keep preferences for people they enjoyed meeting with and disliked
    positive_users = models.ManyToManyField("self", blank=True)
    negative_users = models.ManyToManyField("self", blank=True)
    
    profile_picture = models.ImageField(default='default.png', upload_to='profile_pics')
    friends_list = models.ManyToManyField("self", blank=True)

    # Excludes/includes user from search pool
    available = models.BooleanField(blank=False, null=False, default=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ID: {self.pk}"
    
    # Override save to handle images
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_picture.path)

        # Resize image if greater than display dimensions
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_picture.path)
    
    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
