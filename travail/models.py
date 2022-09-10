from django.db import models

class Country(models.Model):
      name = models.CharField(max_length=100,primary_key=True)
      class Meta:
          db_table="country"
      def __str__(self):
          return "Name:  ".format(self.name)
          
class Speciality(models.Model):
      name = models.CharField(max_length=100,primary_key=True)
      class Meta:
          db_table="speciality"
      def __str__(self):
          return "Name:  ".format(self.name)
class Worker(models.Model):
      cin = models.IntegerField(primary_key=True)
      name = models.CharField(max_length=25)
      lastname = models.CharField(max_length=25)
      country=models.CharField(max_length=15)
      phone=models.IntegerField()
      mail=models.EmailField()
      speciality=models.CharField(max_length=20)
      class Meta:
          db_table="worker"
      def __str__(self):
          return "Cin:  {} \n Name: {}\n LastName:  {}\n   Country:  {}\n Phone:  {}\n Mail:  {}\n Speciality:  {}\n".format(self.cin,self.name,self.lastname,self.country,self.phone,self.mail,self.speciality)
class Contact(models.Model):
      email = models.CharField(primary_key=True, max_length=50)
      name = models.CharField(max_length=20)
     
      message = models.CharField(max_length=200)
     
      class Meta:
          db_table="contact"
      def __str__(self):
          return "email:  {} \n Name: {}\n message:  {}\n ".format(self.email,self.name,self.message)    