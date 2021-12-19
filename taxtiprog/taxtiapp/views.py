from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .basa import *

class MainPage(View):
    def get(self, request):
       # fp,sc,th = get_user()
        context = {



            }
        return render(request, 'h-p.html', context=context)

    def post(self, request):
        vhod_Gde = request.POST.get("Adress1")
        vhod_kyda = request.POST.get("Adress2")
        vhod_data = request.POST.get("calendar")
        vhod_car = request.POST.get("Care-mark")
        vhod_mesage = request.POST.get("koment")
        vhod_people = request.POST.get("people3")
        zayvk_masm = [vhod_Gde, vhod_kyda, vhod_data, vhod_car, vhod_mesage, vhod_people]
        request.session['data'] = zayvk_masm
        return HttpResponseRedirect('car.html')

class cars(View):
    def get(self, request, ):
        peredacha = request.session.get("data")

        context = {
            'gde':peredacha[0],
            'kyda':peredacha[1],
            'data':peredacha[2],
            'car':peredacha[3],
            'mess': peredacha[4],
            'people99':peredacha[5],


            "cars": viebka(peredacha[5], peredacha[3])
            }

        return render(request, 'car.html', context=context)

    def post(self, request):

          if request.method == "POST" and '4t' in request.POST:

              return HttpResponseRedirect('../')

          try:
            peredacha = request.session.get("data")
            user_id = request.session.get("user")

            Driv_entered_id = request.POST.get("id")

            zayavka_pk = create_order(peredacha, user_id, Driv_entered_id)

            request.session['kluch'] = zayavka_pk

            return HttpResponseRedirect('page_payback.html')

          except:

            return HttpResponseRedirect('2.html')

class admin_castom(View):
        def get(self, request):

            context = {
                "cars": get_all_cars(),
                'gays': get_all_Orders()
            }
            return render(request, 'admin.html', context=context)

        def post(self, request):
            entered_fio = request.POST.get("fio")
            entered_ctatys= request.POST.get("stat")
            entered_teel = request.POST.get("tel")
            entered_mark = request.POST.get("mark")
            entered_kolpass = request.POST.get("people")
            entered_pryse1 = request.POST.get("pryse1")
            if request.method == "POST" and 'fio' in request.POST:
                create_care(entered_fio, entered_ctatys, entered_teel, entered_mark, entered_kolpass, entered_pryse1)
            elif request.method == "POST" and 'fio_2' in request.POST:
                entered_fio2 = request.POST.get("fio_2")
                entered_ctatys2 = request.POST.get("stat2")
                entered_teel2 = request.POST.get("tel2")
                entered_mark2 = request.POST.get("mark2")
                entered_kolpass2 = request.POST.get("people2")
                entered_pryse12 = request.POST.get("pryse12")
                entered_id = request.POST.get("id")
                Chenge_care(entered_fio2, entered_ctatys2, entered_teel2, entered_mark2, entered_kolpass2, entered_pryse12,entered_id)

            elif request.method == "POST" and 'statys1' in request.POST:
                entered_fio23 = request.POST.get("statys1")
                entered_id1 = request.POST.get("id1")
                Chenge_statys(entered_fio23,entered_id1)
                print(1111111111111111111111111111111111111111111111111111111)
            elif request.method == "POST" and 'y5' in request.POST:
                print(1111111111111111111111111111111111111111111111111111111)
                entered_id = request.POST.get("id")
                drop_care(entered_id)


            else:
                del request.session['user']
                return HttpResponseRedirect('../')

            return HttpResponseRedirect('admin.html')




class users(View):
        def get(self, request):
            user_id = request.session.get("user")
            # fp,sc,th = get_user(user_id)
            context = {
                'name_use': name_user(user_id),
                'gay': get_all_zayafkas(user_id)
            }
            return render(request, 'user.html', context=context)
        def post(self, request):
            del request.session['user']

            return HttpResponseRedirect('../')

class login(View):
            def get(self, request):
                # fp,sc,th = get_user()
                context = {

                }
                try:
                    if request.session['user'] is None:

                       return render(request, '2.html', context=context)
                    else:
                        if get_role(request.session.get("user")):

                            return HttpResponseRedirect('admin.html')
                        else:

                            return HttpResponseRedirect('user.html')
                except:
                    return render(request, '2.html', context=context)

            def post(self, request):
                entered_login = request.POST.get("log_login")
                entered_passw = request.POST.get("log_pass")


                if not check_login_user(entered_login):
                        context = {
                            'error_message': 'Пользователя с таким именнем не существует'
                        }
                        return render(request, '2.html', context=context)
                else:
                        if not check_pass(entered_login, entered_passw):
                            context = {
                                'error_message': 'Не правильный ввод данных'
                            }
                            return render(request, '2.html', context=context)
                        else:
                            user = get_info_user(entered_login)
                            request.session['user'] = user.pk
                            if get_role(request.session.get("user") ):

                                return HttpResponseRedirect('admin.html')
                            else:

                                return HttpResponseRedirect('user.html')




class registration(View):
            def get(self, request):
                context = {

                }

                return render(request, 'page_registr.html', context=context)

            def post(self, request):

                entered_login = request.POST.get("log_login")
                entered_passw = request.POST.get("log_pass")

                if len(entered_login) <= 0 or len(entered_passw) <= 0:
                    context = {
                        'error_message': 'Заполните все поля'
                    }
                    return render(request, 'page_registr.html', context=context)
                elif len(entered_login) > 25:
                    context = {
                        'error_message': 'Логин не должен быть больше 25 символов'
                    }
                    return render(request, 'page_registr.html', context=context)
                elif len(entered_passw) > 10:
                    context = {
                        'error_message': 'Пароль не должен быть больше 10 символов'
                    }
                    return render(request, 'page_registr.html', context=context)

                elif check_login_user(entered_login):
                    context = {
                        'error_message': 'Пользователь с таким именнем уже существует'
                    }
                    return render(request, 'page_registr.html', context=context)
                else:
                    create_account(entered_login, entered_passw)

                    return HttpResponseRedirect('2.html')


class Page_payback(View):
    def get(self, request, ):
        peredacha = request.session.get("data")
        zayavka_pk_pay = request.session.get("kluch")
        context = {

            'sum_pass': sum_order(peredacha[5],zayavka_pk_pay)

        }
        return render(request, 'page_payback.html', context=context)


    def post(self, request):
        zayavka_pk_pay = request.session.get("kluch")
        peredacha = request.session.get("data")
        bablo = sum_order(peredacha[5],zayavka_pk_pay)
        create_oplata(zayavka_pk_pay, bablo)

        return HttpResponseRedirect('user.html')








    #     card_detail = request.POST.get("number_card")
    #     if len(card_detail) <= 0:
    #         context = {
    #             'error_message': 'Заполните поле'
    #         }
    #         return render(request, 'page_payback.html', context=context)
    #     else:
    #
    #         del request.session['sum_order']
    #         del request.session['number_month']
    #         return HttpResponseRedirect('user.html')