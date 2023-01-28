HOW TO START THE SERVER
-
***********************

cd "[project dir]"
1. django-admin startproject <password-generator-project(project name)
2. using settings "<password-generator-project(project name)"
3. python manage.py runserver


HOW PROJECTS SETUP:
-
*****************
password_generator : this is main django folder project dir
different file details are explained below

1. asig.py: important when we deploy the website
2. wsgi.py: important when we deploy the website
3. setting.py: project location secret key etc
4. urls.py: contains 

HOW TO ADD APP IN YOUR DJANGO PROJ
-
1. Create generator package through command line.
    -
    > python manage.py startapp generator
2. Project details will be created as below 
   - 
   - Migration > __init__.py
   - __init__.py
   - app.py
   - admin.py
   - model.py
   - tests.py
   - views.py

URL
-
    1.locate url.py file in DJANGO proj app
    2. import respective project package and module 
        > from generator import views
    3. locate urlpatterns dictionary
        > urlpatterns = [
            path("", views.home),
            path("eggs", views.eggs)
           ]
    4. locate views.py in APP dir and add function with request and return

TEMPLATE
-
    this section is for main HTML website view part
    1. create templates folder
    2. add app specific template folder for eg. 'generator' here
    3. inside create HTML template
    4. navigate to views.py and return your HTML response.

REFERENCING THE URL NAME WITH OTHER NAME
-
      1. go to DJANGO urls.py and add path
         > path("generatedpassword", views.password, name="password")
      2. Now this [ name = "password" ] will reference to the URL in HTML page.
      3. views.py password function will looks like below
         > def password(request):
            return render(request, "generator/password.html")
      3. navigate to HTML password.html will have reference in action with url replacement
         > action="{% url 'password' %}"

CHAPTER3: Making Random Password
-
      Modify views.py and password functions to return the password to HTML page.

USING FORM DATA
-
      request.GET.get('length') : we can get data from one sender HTML to second

INSTALL GIT
--
      in macbook https://git-scm.com/download/mac
      > /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      > command line hit 'git' and see if git installed

HOW TO MAKE PROJECT GIT Initialized
-  
      > cd <project>
      > git init
      > ls -a to see hidden folder
      > git add -A : to add the changes
      > git commit -m 'modifed password html'
      > git

DESIGN PORTFOLIO
-
   MODEL API
   -
      > navigate to model.py
      > create class and inherrits models.Model
      MODEL API: is the class to implement to create the database by providing database properties
   ***MIGRATING new changes apps***

      > python manage.py migrate
      : to migrate DATABASE model run below
      > python manage.py makemigrations
         Migrations for 'portfolio':
           portfolio/migrations/0001_initial.py
             - Create model Project
      > python manage.py migrate
            Operations to perform:
              Apply all migrations: admin, auth, contenttypes, portfolio, sessions
            Running migrations:
              Applying portfolio.0001_initial... OK
    
   ***WHERE TO SEE THIS PORTFOLIO Model changes applied***
   -
        > navigate to 'portfolio/migrations' project
        > 0001_initial.py file would be created
        > do not manually modify this file at all
        
   ***ADMIN URL***   
   -
        > admin is the default URL http://localhost:8000/admin added in urls.py
        > you need to create userid and password there
        > python manage.py createsuperuser
        TO CHANGE THE PASSWORD:
        > python manage.py changepassword <username ashish>
   ***ADMIN.PY: register Model to view in ADMIN page***
   -
         > go to admin.py screen
         > register site admin.sit.register(Blog) 
         > make sure you import the Model here

   ***STATIC: Images***
   -
         > inside setting STATIC_URL = "static/" tag allow us to references images there
         > create 'static' dir and any folder name to upload your image

   ***CHANGE ADMIN LOOK***
   -
         > open mdoel.py and define funtion under model as below
         >     def __str__(self):
                  return self.summary_header
         > this will overwrite the behavior of admin page how the project/blog looks like

REVERT MIGRATION
-
   ***REVERT MIGRATION****
   -

         > NAVIGATE TO MIGARTION DIR IN PROJECT AND DELETE