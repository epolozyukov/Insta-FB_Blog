# MultiBlog
1.Create the virtual env - python -m venv venv
2.Activate env - venv\Scripts\activate.bat
3.Install django - pip install Django
4.Start django project - django-admin startproject multiblog
5.create the app - python manage.py startapp myblog
6.To start the process of creating our database, we need to create a migration- python manage.py makemigrations myblog
7.you need to apply the migrations set out in the migrations file and create your database using the migrate command - python manage.py migrate myblog


Run app - python manage.py runserver
