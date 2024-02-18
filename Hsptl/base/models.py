from django.db import models

# Create your models here.
class Departments(models.Model):
    dep_name=models.CharField(max_length=50)
    dep_description=models.TextField()

    def __str__(self) -> str:
        return self.dep_name
    
    

class Doctors(models.Model):
    doc_name = models.CharField(max_length=50)
    doc_spec = models.TextField()
    doc_dep = models.ForeignKey(Departments,on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors',default='img.jpg')

    def __str__(self) -> str:
        return 'Dr. ' +self.doc_name


    

class Booking(models.Model):
    p_name = models.CharField(max_length=50)
    p_phone = models.CharField(max_length=15)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on= models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.p_name
        
    
