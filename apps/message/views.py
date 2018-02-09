# -*- coding=utf-8 -*-
from django.shortcuts import render
from .models import UserMessage


# Create your views here.
def getform(request):
    all_message = UserMessage.objects.all()
    for message in all_message:
        print message.name
    if request.method == 'POST':
        name = request.POST.get('name','')
        address = request.POST.get('address', '')
        message = request.POST.get('message', '')
        email = request.POST.get('email', '')


        user_message = UserMessage()

        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.object_id = "yy"

        user_message.save()
    #all_message = UserMessage.objects.filter(name='guojunwei', address='厦门')
    #all_message.delete()

    #for message in all_message:
        # 删除取到的message对象
        #message.detele()
        # print message.name
    message = None
    all_message = UserMessage.objects.filter(name='mtianyan2', address='西安')

    if all_message:
        message = all_message[0]

    return render(request,'message_form.html',{
        'my_message': message,
    })