from django.db import models
from django.contrib.auth.models import User

class Model(models.Model):
    model_name = models.CharField(max_length=255)
    learning_type = models.CharField(max_length=100)
    algorithm_used = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    dataset_used = models.CharField(max_length=100)

    def __str__(self):
        return self.model_name
    
class AllPredictions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

class TitanicSurvivalPrediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    survived = models.BooleanField(null=True, blank=True)
    passenger_id = models.IntegerField()
    pclass = models.IntegerField()
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    age = models.FloatField()
    sib_sp = models.IntegerField()
    parch = models.IntegerField()
    ticket = models.CharField(max_length=50)
    fare = models.FloatField()
    cabin = models.CharField(max_length=50)
    embarked = models.CharField(max_length=1)

    def __str__(self):
        return f"Titanic Survival Prediction for User ID {self.user.id}"

class LaptopPricePrediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField(null=True, blank=True)
    msi = models.BooleanField(null=True, blank=True)
    amd_cpu = models.BooleanField(null=True, blank=True)
    intel_cpu = models.BooleanField(null=True, blank=True)
    intel_gpu = models.BooleanField(null=True, blank=True)
    amd_gpu = models.BooleanField(null=True, blank=True)
    acer = models.BooleanField(null=True, blank=True)
    weight = models.FloatField()
    flash = models.BooleanField(null=True, blank=True)
    razer = models.BooleanField(null=True, blank=True)
    workstation = models.BooleanField(null=True, blank=True)
    ultrabook = models.BooleanField(null=True, blank=True)
    nvidia_gpu = models.BooleanField(null=True, blank=True)
    gaming = models.BooleanField(null=True, blank=True)
    hdd = models.BooleanField(null=True, blank=True)
    cpu_frequency = models.FloatField()
    ssd = models.BooleanField(null=True, blank=True)
    notebook = models.BooleanField(null=True, blank=True)
    screen_height = models.IntegerField()
    screen_width = models.IntegerField()
    ram = models.IntegerField()

    def __str__(self):
        return f"Laptop Price Prediction for User ID {self.user.id}"

