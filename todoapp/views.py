from django.shortcuts import render,redirect
from todoapp.models import *
from django.http import HttpResponse

# Create your views here.






def homepage(request):
    tododatas=Todo.objects.all().order_by("-id")
    content= {
        'todo':tododatas,'form':Todoform()
    }
    if request.method=="POST":
        data = request.POST
        form = Todoform(data)
        if form.is_valid():
            form.save()
            return redirect("/") 
        return render(request,"todoapps/index.html",)
         
    return render(request,"todoapps/index.html",{'datas':content})



def Edittodo(request,id):
    try:
        tdata=Todo.objects.get(id=id)
        tdata.delete()
        return HttpResponse("<h1>Todo is Deleted</h1>")

    except:
        return redirect("/")
    return HttpResponse(f"<h1>{id}</h1>")


def Updatetodo(request,id):
    try:
        tdata=Todo.objects.get(id=id)
        context={'todo':tdata}

        return render(request,"todoapps/update.html",context)
    except:
        return redirect("/")

def Update(request):
    if request.method == "POST":
        data = request.POST
        todo = data['todoform']
        todoi = data['todoid']
        obj = Todo.objects.get(id=todoi)
        obj.text = todo
        obj.save()

        return redirect("/")
    else:
        return HttpResponse("<h1>Something is wrong ! Try again")