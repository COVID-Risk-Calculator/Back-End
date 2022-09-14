from django.db import models
# from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):

#     def __str__(self):
#         return self.username


class Test(models.Model):
    NONE = "None"
    PCR = "PCR"
    RAPID_HOME = "Rapid At-Home"
    RAPID_MED = "Rapid Medically-Administered"

    TEST_CHOICES = [
        (NONE, 'none'),
        (PCR, 'pcr'),
        (RAPID_HOME, 'rapid-at-home'),
        (RAPID_MED, 'rapid-medical'),
    ]

    tested = models.TextField(choices=TEST_CHOICES, default=NONE)
    test_date = models.DateField(null=True, blank=True)


class Guest(models.Model):
    county = models.CharField(max_length=255, null=True)
    case_data = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    vaccination_rate = models.DecimalField(max_digits=10, decimal_places=2,
                                           null=True, blank=True)
    risk_mutliplier = models.DecimalField(max_digits=10, decimal_places=2,
                                          null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    test = models.ForeignKey(Test, on_delete=models.CASCADE,
                             related_name='geusts')


class Event(models.Model):
    pass
