from django.shortcuts import render
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView
from task.forms import Encrypdata
from task.forms import Decrypdata
from task.methods import reverse
from task.methods import Encryption
from task.methods import Decryption


# Create your views here.
def homepage(request):
    return render(request,'index.html')


def Encrypdataview(request):
    form= Encrypdata
    enform={'form':form}
    if request.method=="POST":
        form = Encrypdata(request.POST)
        if form.is_valid():
            Entext=Encryption(form.cleaned_data['Rawdata'],form.cleaned_data['depth'])
            endict={"text":Entext}
            return render(request,'index.html',endict)
    return render(request,'task/EncrypDataview.html',enform);

def Decrypdataview(request):
    form= Decrypdata
    deform={'form':form}
    if request.method=="POST":
        form = Decrypdata(request.POST)
        if form.is_valid():
            Detext=Decryption(form.cleaned_data['Rawdata'],form.cleaned_data['depth'])
            dedict={"text":Detext}
            return render(request,'index.html',dedict)
    return render(request,'task/DecrypDataview.html',deform);
