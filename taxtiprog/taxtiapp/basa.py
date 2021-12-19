from .models import *
from django.utils import timezone
from datetime import datetime

def check_login_user(login_user):
    login = Users.objects.filter(login=login_user) #запрос из бд abkmnhetv gj kjubye фильтруем по логину
    if len(login) > 0:
        return True
    else:
        return False

def create_account(entered_login, entered_passw): #з создание записи
    new_user = Users(login=entered_login, password=entered_passw)
    new_user.save()

def create_care(entered_fio, entered_ctatys, entered_teel, entered_mark, entered_kolpass, entered_pryse1): #з создание записи
    new_car = Cars(Fio_driver=entered_fio,status_Car =entered_ctatys,Phone_Driver =entered_teel, Car_mark=entered_mark, people_num=entered_kolpass,Price =entered_pryse1)
    new_car.save()

def check_pass(login, password):
    get_user_pass = Users.objects.filter(login=login)
    if get_user_pass[0].password == password:
        return True
    else:
        return False

def get_info_user(login):
    user = Users.objects.filter(login=login)
    return user[0]

def get_role(id_user):
    role_user = Users.objects.filter(pk=id_user)
    if role_user[0].role == 'admin':
        return True
    else:
        return False

def get_all_cars():
    bibikas = Cars.objects.all()# Бибикас выборка из масива
    return bibikas

def  Chenge_care(entered_fio2, entered_ctatys2,entered_teel2,entered_mark2,entered_kolpass2,entered_pryse12,entered_id):
    bibicak = Cars.objects.get(pk=entered_id)
    bibicak.Phone_Driver = entered_teel2
    bibicak.Price = entered_pryse12
    bibicak.status_Car = entered_ctatys2
    bibicak.Fio_driver = entered_fio2
    bibicak.people_num = entered_kolpass2
    bibicak.Car_mark = entered_mark2

    bibicak.save()

def get_some_cars():
    mashina = Cars.objects.all()# Бибикас выборка из масива
    return mashina

def viebka(entered_kolpass,entered_mark):
    cabriolet = Cars.objects.filter(Car_mark=entered_mark)
    pasmas = []
    entered_kolpass = int(entered_kolpass)
    for i in cabriolet:
        if i.people_num>=entered_kolpass:
            pasmas.append(i)
    if len(pasmas)== 0 :
        return False

    return pasmas

def create_order(peredacha,user_id,Driv_entered_id):

    new_order1 = Cars.objects.filter(pk=Driv_entered_id)
    new_order2 = Users.objects.filter(pk=user_id)

    new_order = zayavka(Cars_idCars=new_order1[0], Users_idUsers=new_order2[0], Data_start_drive=peredacha[2], Start_point=peredacha[0], End_point=peredacha[1], Pozelanie=peredacha[4], people_num=peredacha[5])
    new_order.save()
    return new_order.pk

def get_all_zayafkas(user_id):

        # ass = Users.objects.filter(pk=user_id)
        zayafka = Orders.objects.all()
        ass = []
        for i in zayafka:
            if i.zayavka_idzayavka.Users_idUsers.pk == user_id:
                ass.append(i)

        return ass

def sum_order(sum_kolpas,Sum_car):
    new_order1 = zayavka.objects.filter(pk=Sum_car)
    sum_Car = new_order1[0].Cars_idCars.Price * float(sum_kolpas )
    return sum_Car

def  create_oplata(zayavka_pk_pay, bablo):

    new_order1 = zayavka.objects.filter(pk=zayavka_pk_pay)
    new_order = Orders(OrderSum=bablo, zayavka_idzayavka=new_order1[0])

    new_order.save()


def name_user(user_id):
    zayafka = Users.objects.filter(pk=user_id)

    return zayafka[0]

def get_all_Orders():
    bibikas = Orders.objects.all()# Бибикас выборка из масива
    return bibikas



def  Chenge_statys(entered_fio23,entered_id1):
    bibicak = Orders.objects.get(pk=entered_id1)
    bibicak.active_status = entered_fio23
    bibicak.save()

    print(11111111)
    print(bibicak.active_status)

def drop_care(entered_id):
    deleteA = Cars.objects.filter(id=entered_id).delete()
