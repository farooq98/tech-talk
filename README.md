# tech-talk

Hi 👋, I'm Farooq Hidyat
This is a tutorial for ***Django Begineers***

Follow the steps below to run this project

* Clone the project
* Install Python (https://www.python.org/downloads/)
* Install pip 

For linux, open ternimal and type this command

    $ sudo apt install python3-pip
    
* Install Virtual Environment

Open terminal and type this command if `pip` does not work try `pip3`.

    $ pip3 install virtualenv

* Create Virtiual Environment

Open terminal and type this command.

    $ python3 -m virtualenv venv
    
* Activate Virtiual Environment

Open terminal and type this command for linux.

    $ source venv/bin/activate

For windows.

    $ venv\Scripts\activate
    
* Install Requirements

Moved to the cloned directory, open terminal and type this command.

    $ pip install -r requirements.txt
    
* Migrate Database

Moved to the project directory `tech_talk`, open terminal and type this command.

    $ python manage.py migrate
    
* Create Super User

Moved to the project directory `tech_talk`, open terminal and type this command and provide the required data.

    $ python manage.py createsuperuser
    
* Run Project

Moved to the project directory `tech_talk`, open terminal and type this command.

    $ python manage.py runserver
    
* View On Browser (open your favourite browser and type: http://127.0.0.1:8000/admin in the url and press enter)
* Login with the above created credentials 
