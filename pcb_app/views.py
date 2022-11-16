from contextlib import redirect_stderr
from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import *
from django import forms
from .forms import *
from django.http import JsonResponse

def list(request):
    fm=phone_book.objects.all().values()
    print("val :",fm)
    return render(request,"list_contact.html",{"frm":fm})


def view_dtls(request,id):   
    context = {}
    phone_contact_book_dtls = phone_book.objects.get(id=id)
    context = {'pcb_dtls':phone_contact_book_dtls}
    return render(request,'view_contact.html',context)

def view_contact_dtls(request):   
    context = {}
    fm = PhoneBookContactForm()
    context = {'contact_form':fm}
    return render(request,'create_new_contact.html',context)


def contact_add_sv(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax and request.method == "POST":
        fm = PhoneBookContactForm(request.POST)        
        if fm.is_valid():
            fm.save()
            return JsonResponse({"Sucess": True}, status=200)
        else:
            return JsonResponse({"error": fm.errors}, status=400)
            
    return JsonResponse({"error": ""}, status=400)


def edit(request,id):
    context = {}
    object=phone_book.objects.get(id=id)
    form=PhoneBookContactForm(instance=object) 
    if request.method == 'POST':
        form = PhoneBookContactForm(request.POST,instance=object)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form_edit':form}
    return render(request,'edit_contact.html',context)


def delete(request,id):
    if request.method=="POST":
        context = {}
        obj=phone_book.objects.get(id=id)
        obj.delete()
        return redirect('/')
    else:
        return redirect('/')



    



   
