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

PUBLISH SITE IN PYTHON ANYWHERE
-  
         > navigate to PythonAnywhere
         > launch bash window
         > copy git repo url and run command "git clone <repo name>"
         > $cd django3-personal-portfolio                                                                                                                       
            ~/django3-personal-portfolio (main)$
   ***CREATE VENV****
   -
         > mkvirtualenv --python=/usr/bin/pyhton3.8 portfoliovenv
         > it will create and activate venv
         > (portfoliovenv) 02:31 ~/django3-personal-portfolio (main)$
         > to deactivate venv > ht command deactivate
         > if you first time start bash and move to venv : workon <venvname>
   ***TO LIST VENV***
   -  
         > cd .virtualenvs/
         > ls
   ***INSTALL NEW: django and pillow***
   -
         > pip install django pillow

   ***PYTHON ANYWHERE***
   -
         > navigate to new window PythoAnywhere
         > click on Web buttong on top menu
         > add new web app > next
         > select python web framework - manual configuration
         > select python version
         > scroll down at Virtualenv section and provide your virtual env path ( providing name will automatically select env path)
         > scroll up "code" section and update "source code"  and "Working Dir" path of your project cloned.
         > copy WSGI config file path, click on it.
         > open WSGI file and 
         > scroll down until you see # +++++++++++ DJANGO +++++++++++
         > keep that section and delete all other
         > then edit path: to actual project cloned path
         > os.environ['DJANGO_SETTINGS_MODULE'] should be updated to -> personal_portfolio.settings
         > for eg. 
               ── personal_portfolio
            │   ├── __init__.py
            │   ├── __pycache__
            │   │   ├── __init__.cpython-38.pyc
            │   │   ├── settings.cpython-38.pyc
            │   │   ├── urls.cpython-38.pyc
            │   │   └── wsgi.cpython-38.pyc
            │   ├── asgi.py
            │   ├── settings.py
            │   ├── urls.py
            │   └── wsgi.py
         > save
         > go back to pythonanywhere
         > click on web
         > clikc on reload 

   ***RESOLVE ISSUE****
   -
       1.ALLOWED HOST: add url in setting.py ALLOWED_HOST = ["achincholkar.pythonanywhere.com"]
       2. go to settings.py file and set DEBUG=False
       3. to show all our static file : udpate STAIC_ROOT = os.path.join(BASE_DIR, "static")
       4. go to BASH console or project dir where manage.py is and run command "python manage.py collectstatic" : it will collect all and put all static under there

   ***UPDATE STATIC FILE PATH***
   -
      1. click on web
      2. scroll down to static files section
      3. under URL /static/ 
      4. for DIR go to BASH - cd static and pwd

   ***gitignore***
   -
      1. in pythonanywhere console
      2. > nano .gitingore
         ### Django ###
         *.log
         *.pot
         *.pyc
         __pycache__/
         /static/
      3. ctrl+x
      4. git add .gitignore in pythonanywhere console
      5. (portfoliovenv) 18:11 ~/django3-personal-portfolio (main)$ git config --global user.email "ashish_chincholkar@hotmail.com"
         (portfoliovenv) 18:11 ~/django3-personal-portfolio (main)$ git config --global user.name "Ashish"
      6. git rm -r --cached .
      7. git add .
      8. step 6 and 7 will remove pyc file
      6. git commit -m "added gitignore"

   ***SOMETIME PYTHONANYWHERE Linux PUSH Issue****
   -
      1. git remote -v

         git remote set-url git@github.com:ashuchincholkar/django3-personal-portfolio.git