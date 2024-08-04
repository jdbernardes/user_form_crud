# User Form APP

This small app has been developed in order to practice the concepts of conteinerization and environment variables.
This is a very simple app that will:
    1.Connect to a postgres DB\n
    2.Create a table called users\n
    3.Load a form with 3 fields using streamlit\n
    4.Once user adds the name, last name and age it will insert into the table and also display the list of users in the DB\n

Instructions to deploy complete:
    1.Run *git clone* on this repository
    2.[Download and install docker](https://docs.docker.com/get-docker/)
    3.Make sure you have [Docker Compose](https://docs.docker.com/compose/install/)
    4.Create a file called .env in your root directory and provide values for the following variables:
        1.**POSTGRES_DB**=  Define the name of your database
        2.**POSTGRES_USER**= Define your postgres username
        3.**POSTGRES_PASSWORD**: Define your DB password
        4.**PGADMIN_DEFAULT_EMAIL**: Define your pgadmin user to access pgadmin page
        5.**PGADMIN_DEFAULT_PASSWORD**: Define your pgadmin password to access pgadmin page
        5.**HOSTNAME_SERVER**: Here you define a hostname for your postgres
        7.**DB_CONTAINER_NAME**: Define the postgres container name
        8.**PG_CONTAINER_NAME**: Define PG admin container name
        9.**APP_CONTAINER_NAME**: Define your APP container name
        10.**DB_PORT_INTERN**: You should set this as 5432
    5.Run *docker-compose up -d* : the "-d" will make your compose to run in detached mode which doesn't locks your terminal

Instructions to deploy only DB and PGAdmin and run the app locally:
    1.Run *git clone* on this repository
    2.[Download and install docker](https://docs.docker.com/get-docker/)
    3.Make sure you have [Docker Compose](https://docs.docker.com/compose/install/)
    4.In the file *docker-compose.yaml* remove or comment everythinf between the following sessions
        1."#APP session START / END" and "#APP volume START / END"
    5.Install [Poetry](https://python-poetry.org/)
    6.Make sure you set the parameter "virtualenvs.in-project true"
    7.Run command poetry shell: this command must create the .venv folder, if doesn't work, review step 6
    8.Run comman poetry install: this will install all dependencies in the virtual environment
    9.In the folder APP, create a .env file and set the following parameters:
        1.**DB_NAME** = Will be the sabe value you defined for **POSTGRES_DB**
        2.**DB_USER** = Will be the sabe value you defined for **POSTGRES_USER**
        3.**DB_USER** = Will be the sabe value you defined for **POSTGRES_PASSWORD**
        4.**DB_HOST** = "localhost"
        5.**DB_PORT** = Make sure port is: *15432*
    10.Run comand *poetry run streamlit run app/app.py*
    

    
