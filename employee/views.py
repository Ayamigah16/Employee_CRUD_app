from django.shortcuts import render, redirect

from employee.forms import EmployeeForm  # modelform created 
from employee.models import Employee        # db_table created

from django.views.decorators.http import require_http_methods
# Create your views here.

@require_http_methods(["GET","POST"])  # FOR GET and POST request

# functions to validate the form
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        
        if form.is_valid():     # when form inputs are valid
            try:
                form.save()         # save input data
                return redirect('/show')    # display the show page
            except:
                pass
        # if form data is invalid, show the index page for the user to reinput the correct data
    else:
        form = EmployeeForm()
        return render(request, 'index.html', {'form':form})
        

# a function to diaplay the show page
def show(request):
    employees = Employee.objects.all()         # assigning all table columns
    # displaying the employee table on show page
    return render(request, 'show.html', {'employees': employees})


# afunction to display the edit page
def edit(request, id):
    employee = Employee.objects.get(id = id)      # fetching values for the employee id
    return render(request, 'edit.html', {'employee': employee})
    

# a function to update inputs in the edit page
def update(request, id):
    employee = Employee.objects.get(id=id)      # fetching employee details
    form = EmployeeForm(request.POST, instance= employee) # displaying the form for the employee instace
    
    # validating updated inputs
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'employee': employee})

# a function to delete a row in the database
def delete(request, id):
    employee = Employee.objects.get(id=id)  #fetching employee details based on the id
    employee.delete()       # deleting employee data
