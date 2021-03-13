Author: Mohammad Abouchama
About: overview of the tech_test project and instructions for running it.

The project was setup on windows with Anaconda Console for Python development. It provides a nice and safe virtual environment to work with Python.

If working on Macos then the following article can be used for setting up a virtual env: https://medium.com/@jayden.chua/virtual-environments-pip-and-pipenv-on-macos-8f3178b13b75
Else, for Ubuntu this can be used https://www.liquidweb.com/kb/creating-virtual-environment-ubuntu-16-04/.

The project relies on Django 3.0, Python 3.7.4. Also, used are django-filter 2.3.0. Django-filer 2.3.0 is used for simple and quick implementation of 
filtering in the templates for the user.

The images or picture for the teacher profiles must be JPG's and/or PNG's. Also, they must be in tech_test/teacherdirectory/media/. Otherwise the images will not be used by
the project. The images can simply be copied into tech_test/teacherdirectory/media/.
A placeholder image will be provided for a teacher profile if the said profile's picture cannot be found in tech_test/teacherdirectory/media/, is not a JPG or PNG, or has no 
file name specified.

The program undertakes a number of assumptions on the structure of the CSV file. It must be similar in structure to the example CSV file provided in the test.
The first row is the first_name, second row is the last_name, third row is for the profile picture, fourth row is for the email address, 
fifth row is for the phone number, 6th row for the room number, and rows 7 and onwards are for subjects.
The program will take the first five subjects it finds, and it will ignore the rest of the subjects, if they exceed the limit of 5. This can be adjusted by 
inserting a new value for MAX_SUBJECTS in tech_test/teacherdirectory/constants.py. The value should be more than 0.

Any teacher profile in the CSV that has a duplicate email address will be ignored and not imported.

Instructions for running the project:
	1. python manage.py makemigrations (unlikely to be needed but good practice)
	2. python manage.py migrate (unlikely to be needed but good practice)
	3. python manage.py runserver
	* That is it, very straight forward.
	** It is a very simple python and django project, no unusual implementations or hacks were done.
	*** For deleting profiles and importing profiles, the user must be signed in.
	**** Create a new superuser, or use the following:
		username: hamade
		password: qweQWE123!@# 
