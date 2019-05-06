# :grin:__ONE-DAKIKA-PITCH__:grin:

# __AUTHOR: BRIGHTON ASUMANI__
# __PROJECT: ONEMINUTEPITCH APPLICATION__
# __ABOUT APPLICATION__

## ***__DESCRIPTION__***
> In life you only have 60 seconds to impress someone. 1 minute to make or break you.
> How do we make sure that you use your 1 minute to actually say something meaningful?.
> So this application helps you to do the following:

        > Create categories
        > Create pitches related to those categories
        > Make comments on those Pitches
        > All this content will be stored in your browser
        > The application also has a cool GUI and instructions listed on the home or index page


## ***__INSTALLATION__***
You can install this application in different ways. They include:
1. You can clone this repository and download the requirements which i have listed in my requirements.txt file.
 *For you to clone this application you need to have the following installed in your machine : git, virtual.(virtual is very important. since your application cannot run without a virtual).
This is how you install virtual you need the following:*

### __I used ubuntu:  sudo apt-get install python3.6-venv python3.6 -m venv virtual__

> Repo: https://github.com/BRIGHTON-ASUMANI/one-dakika-pitch.git
> some requirements(check on requirements.txt). you can also check the on the apps functionality in specs.md
> note: you can check this application's functionality in heroku since it is hosted there:

# DEPLOYMENT TO HEROKU
1. $ heroku apps:destroy
> This removes your application so that we can start a fresh

2. $ heroku create <app>
> to create the application name

3. $ heroku addons:create heroku-postgresql:hobby-dev
> to create a new postgresql in the heroku database which is an addons application...i think..but the application will
not have your current data in your localhost

4. $ heroku run python3.6
> just to make it clear the application we would like to make in the heroku website will not be based in your localhost..it will be in the heroku database so your DATABASE_URL will >
> change.Looking like it will be encrypted or something.that is why we are running run python.

__we first import the os to get the necessary methods__
* import os
* os.environ.get("DATABASE_URL")
* you will get a foreign url like
> 'postgres://sahkwiwajjbmmm:40aea754da09ca490ed37e87c04aa36b931a04aa1713569561ab9d062c8c0131@ec2-54-235-196-250.compute-1.amazonaws.com:5432/d3f9jva5utjk0t'
> this is a good sign....it means progress
> Then paste it to the exports in the start.sh

> **export DATABASE_URL='postgres://komkrhtvhkqhpf:d1f780c5d2f7b58754ef26f4b85a8dbd6934d59cba70f8400ffca2845f5bb1b7@ec2-54-227-247-225.compute-1.amazonaws.com:5432/d6bgqi19ennurv'
python3.6 manage.py server**

>  afterward we do this in the ProdConfig function in the config.py this line of code

>  class ProdConfig(Config):

>  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

>  and this will help you to recieve the localhost in Heroku.

> we then run this in our terminal after doing the git stuff...

> $ git add .

> $ git commit -m "Deploying to heroku"

> $ git push heroku master

> $ heroku run python3.6 manage.py shell

> this will head us to our shell where we need to create the db so as to run it right?

> db.create_all()

> exit()

> now we have created our database so we will need to export everything to our heroku

> if you had exports such as

> MAIL,PASSWORDS,SECRET_KEY

> $ heroku config:set <the line of export>

> the line of export may be like SECRET_KEY='12345'

> PLease make sure you have no error

> to confirm if your psql is working run

> $ heroku pg:psql

***for any queries please contact @ asumanibrighton@gmail.com***
