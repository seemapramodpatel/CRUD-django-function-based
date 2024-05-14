from django.shortcuts import render , redirect , get_object_or_404
from api.models import Employees

# Create your views here.

def INDEX(request):
    emp = Employees.objects.all()

    context ={
        'emp': emp,
    }
    return render(request, 'index.html', context)

def ADD(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')


        emp = Employees(
            name = name,
            email = email,
            address = address,
            phone = phone
        ) 

        emp.save()
        return redirect('home')
    return render(request, 'index.html',emp)



def Edit(request):
    emp = Employees.objects.all()
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

    emp = Employees(
        name = name,
        email = email,
        address = address,
        phone = phone
    ) 
    context = {
        'emp' : emp,
    }

    return redirect(request, 'index.html', context)

def Update(request, id):
    # Retrieve the existing employee object
    emp = get_object_or_404(Employees, id=id)

    if request.method == "POST":
        # Update the fields of the existing employee object
        emp.name = request.POST.get('name')
        emp.email = request.POST.get('email')
        emp.address = request.POST.get('address')
        emp.phone = request.POST.get('phone')

        # Save the updated employee object
        emp.save()

        # Redirect to a different URL after updating (replace 'home' with your desired URL or view name)
        return redirect('home')

    # If the request method is not POST, render the update form with the existing employee object
    return render(request, 'index.html', {'emp': emp})


def Delete(request,id):
    emp = Employees.objects.filter(id=id)
    emp.delete ()
    context ={
            'emp':emp,
    }
    return redirect('home')
