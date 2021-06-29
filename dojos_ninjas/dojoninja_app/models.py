from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=2)
    desc = models.TextField(max_length=255)
    def __repr__(self): 
        return f"<{self.name} {self.city} {self.state}"

class Ninja(models.Model):
    dojo_id = models.CharField(max_length=45)
    school_dojo = models.ForeignKey(Dojo, related_name="school_ninjas", on_delete = models.CASCADE)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    def __repr__(self): 
        return f"<{self.dojo_id} {self.first_name} {self.last_name}"