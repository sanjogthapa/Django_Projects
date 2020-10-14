from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy

from std_mgmt_sys.models import Books, Teachers, Tutorials
from std_mgmt_sys.forms import *
from django import views
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, DetailView,UpdateView


# Create your views here.

def first_View(request):
    return render(request, 'index.html')

def books_view(request):
    b = Books.objects.all()
    return render(request,'sms/books_view.html',context={'books':b})

def teachers_view(request):
    c= Teachers.objects.all()
    return render(request,'sms/teachers_view.html', context={'teachers':c})

def tutorials_view(request):
    d= Tutorials.objects.all()
    return render(request,'sms/tutorials_view.html', {'tutorials':d})

def add_teacher(request):
    if request.method == 'GET':
        return render(request,'sms/add_teacher.html')
    elif request.method == 'POST':
        english = request.POST['english']
        maths= request.POST['maths']
        science = request.POST.get('science')
        author = Teachers.objects.create(english=english, maths = maths, science = science)
        return HttpResponse('The form is submitted')

def add_books(request):
    if request.method == 'GET':
        add_books_form = AddBooksForm()
        return render(request,'sms/add_books.html',{'form': add_books_form})

    if request.method == 'POST':
        name = request.POST['name']
        author = request.POST['author']
        published_date = request.POST['published_date']
        price = request.POST['price']
        b2 = Books.objects.create(name= name, author= author, published_date = published_date, price= price)
        return HttpResponse('data saved in database')


def add_tutorials(request):
    if request.method == 'GET':
        tutorials_form=TutorialsModelForm()
        return render(request,'sms/add_tutorials.html', {'form_tutorials': tutorials_form})

    else:
        tutorials_form = TutorialsModelForm(request.POST)
        if tutorials_form.is_valid():
            tutorials_form.save()
            return redirect('sms:tutorials_view')
        else:
            return render(request,'sms/add_tutorials.html', {'form_tutorials': tutorials_form})

def edit_tutorials(request, id):
    tutorial= Tutorials.objects.get(id=id)
    if request.method == 'GET':
        form= TutorialsModelForm(instance=tutorial)
        return render(request,'sms/edit_tutorials.html', {'form': form})
    elif request.method == 'POST':
        form= TutorialsModelForm(request.POST, instance=tutorial)
        if form.is_valid():
            form.save()
            return redirect('sms:tutorials_view')
        else:
            return render(request, 'sms/edit_tutorials.html', {'form': form})


def delete_tutorials(request,id):
    book= Tutorials.objects.get(id=id)
    book.delete()
    return redirect('sms:tutorials_view')


def addbooks_model(request):
    if request.method == 'GET':
        books_form=AddBooksModelForm()
        return render(request,'sms/addbooks_model.html', {'books_form': books_form})

    else:
        books_form=AddBooksModelForm(request.POST, request.FILES)
        if books_form.is_valid():
            books_form.save()
            return redirect('sms:books_view')
        else:
            return render(request,'sms/add_tutorials.html', {'books_form': books_form})


class AddStudents(views.View):
    def get(self, request):
        add_students= AddStudentsModelform()
        return render(request, 'sms/add_student.html', {'form': add_students})

    def post(self, request):
        add_students = AddStudentsModelform(request.POST)
        if add_students.is_valid():
            add_students.save()
            return HttpResponse('data is saved in database')
        else:
            return render(request, 'sms/add_student.html', {'form': add_students})



class AboutUsView(TemplateView):
    template_name = 'sms/about_us.html'

    def get_context_data(self):
        return {'phone': 9849150687}

class TutorialsListView(ListView):
    model = Tutorials
    template_name = 'sms/tutorials_view.html'
    context_object_name = 'tutorials'


class AddTeacherGeneric(CreateView):
    model = Teachers
    template_name = 'sms/add_teacher_generic.html'
    fields = '__all__'
    success_url = reverse_lazy('sms:teachers_view')


class UpdateTeacherGeneric(UpdateView):
    model = Teachers
    fields = '__all__'
    template_name = 'sms/update_teacher.html'
    success_url = reverse_lazy('sms:teachers_view')


class TeacherDetailGeneric(DetailView):
    model = Teachers
    template_name = 'sms/detail_teacher.html'


class TeacherDeleteGeneric(DeleteView):
    model = Teachers
    template_name = 'sms/delete_teacher.html'
    success_url = reverse_lazy('sms:teachers_view')

