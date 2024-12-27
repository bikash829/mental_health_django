step 1: Run 
    - python manage.py makemigrations
    - python manage.py migrate
    - python manage.py setup_roles # to create user group 

step 2 : 
    - run fixture for specialization 
    - python manage.py loaddata doctor/specialization.json