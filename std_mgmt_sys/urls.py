from django.urls import path
from std_mgmt_sys import views

app_name='sms'

urlpatterns= [
    path('books_view/', views.books_view, name='books_view'),
    path('teachers_view/', views.teachers_view, name='teachers_view'),
    path('tutorials_view/', views.tutorials_view, name='tutorials_view'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('add_books/', views.add_books, name='add_books'),
    path('add_tutorials/', views.add_tutorials, name='add_tutorials'),
    path('edit_tutorials/<int:id>/', views.edit_tutorials, name='edit_tutorials'),
    path('delete_tutorials/<int:id>/', views.delete_tutorials, name='delete_tutorials'),
    path('addbooksmodel/', views.addbooks_model, name='addbooks_model'),
    path('addstudents/', views.AddStudents.as_view(), name='add_students'),
    path('aboutus/', views.AboutUsView.as_view(), name='about_us'),
    path('tutorialslistview/', views.TutorialsListView.as_view(), name='tutorials_listview'),
    path('addteachergeneric/', views.AddTeacherGeneric.as_view(), name='addteacher_generic'),
    path('updateteachergeneric/<int:pk>/', views.UpdateTeacherGeneric.as_view(), name='updateteacher_generic'),
    path('detail_teacher/<int:pk>/', views.TeacherDetailGeneric.as_view(), name='detail_teacher'),
    path('delete_teacher/<int:pk>/', views.TeacherDeleteGeneric.as_view(), name='delete_teacher')

]