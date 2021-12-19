from django.db import models

class Users(models.Model):
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=10)
    role = models.CharField(max_length=10, default="user")

class Cars(models.Model):
    Phone_Driver = models.IntegerField()
    Price = models.FloatField()
    status_Car = models.CharField(max_length=15)
    Fio_driver = models.CharField(max_length=30)
    Car_mark = models.CharField(max_length=30)
    people_num = models.IntegerField()

class zayavka(models.Model):
    Data_start_drive = models.DateField()
    Start_point = models.CharField(max_length=45)
    End_point = models.CharField(max_length=45)
    Pozelanie = models.CharField(max_length=60)
    people_num = models.IntegerField()
    Cars_idCars = models.ForeignKey(Cars, on_delete=models.CASCADE)
    Users_idUsers = models.ForeignKey(Users, on_delete=models.CASCADE)

class Orders(models.Model):
    OrderSum = models.FloatField()
    active_status = models.CharField(max_length=30,default="В процессе")
    zayavka_idzayavka = models.ForeignKey(zayavka, on_delete=models.CASCADE)


class Review(models.Model):
        text_review = models.CharField(max_length=145)
        user_iduser = models.ForeignKey(Users, on_delete=models.CASCADE)
        Order_idOrder = models.ForeignKey(Orders, on_delete=models.CASCADE)