# 91Social first test

Based on python (Flask) and database as MongoDB

# note
For security reasons config file has been removed from public repostry. Please replace ``` config.py ``` in the root directory with the ``` config.py ``` attached to the submission email 


## Initial setup 

Install Virtual environment for python 

``` pip install virtualenv```

setup virtual environment

``` virtualenv env```

start virtual environment

for windows

``` env\Scripts\activate ```

for Linux 

``` source env/bin/activate ```


## APP Setup 

Run the Virtual Environment

```virtualenv virtual_environmen_name```

Using Virtual environment using

```cd virtual_environmen_name```

Activate Virtual environment

```source bin/activate```

After you have successfully activated your virtual environment, cd into the source code were the "requirements.txt" file is

run ``` pip install -r requirements.txt ``` to install all the requirements

then run ``` flask run ``` to start the server


## Running with docker 
Install docker in your local machine and run the following comands 

``` docker build -t socailbe .```

``` docker run -p 8080:8080 -it socailbe```