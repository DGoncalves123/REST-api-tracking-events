
![alt text](https://static.djangoproject.com/img/logos/django-logo-positive.svg "Logo Title Text 1")
![alt text](https://wiki.postgresql.org/images/thumb/a/a4/PostgreSQL_logo.3colors.svg/116px-PostgreSQL_logo.3colors.svg.png "Logo Title Text 1")


# REST API to track spatial occurrences

A REST API to allows the creation and edition of users, after which it allows for the creation of occurrences of several types.

Includes a starter Docker deployment configuration.

Includes a small Postman collection with some of the actions available and examples.

## Getting Started

Get a copy of the files and place them in the current disposition on the desired location.

### Prerequisites

Install [Docker](https://www.docker.com/products/docker-desktop) and docker compose, if on windows or mac, the installer from the link already includes docker compose.


### Installing

For windows: 
* Start a command line at the root of the project.
* Do 'docker-compose build', which will create an image of all the components.
* Do 'docker-compose up', to send the images to a container and starting it. **The django server is set to debug mode.**
* Open a command line to the container which has the django application running and create a superuser, using 'python manage.py createsuperuser' and following the steps that appear.



## Results of the installation

The database admin should be running on the local machine at port :5454, the database should be running at port :5432 and the REST server should be running at :8000.
The parameters defined are:
* admin@admin.com - postgres : as user and password for the db admin
* admin - diogo : as user and password for the database

## API structure
* /
  * admin/
  * api/
     * users/
          * 'user_id'/
      * situation/
          * 'situation_id'/
      * auth/
          * login/
          * logout/
     

## Main endpoints
*Every endpoint can read json,x-www-urlencoded and form data and can return json or html*

* **POST** Create user account 
* **GET** See all users <sup>1</sup>
```
/api/users/
```
* **POST** Login
```
/api/auth/login/
```
* **POST** Add new occurrence
* **GET** See all occurrences, different header variables can be useed to filter <sup>1</sup>
```
/api/situation/
```
*<sup>1</sup> For user and situation see the specific object by adding the object id at the end of the endpoint (e.g.: /api/users/1/), which can also be used to edit the object*

E.G. 
* **POST** To change the object entirely
* **PATCH** To edit a field, such as status in an occurrence
```
/api/situation/1/
```

## Endpoint's main permissions

Using the CSFR and session from the login endpoint, you can obtain the 'logged in user' or 'admin' permission depending on the type of account logged in.

* **Everyone**: See occurrences, create user account
* **UserLoggedIn**: Create occurrences, edit user account
* **Admin**: Edit occurrences, get all user accounts

## Tests with Postman

* Open the postman application.
* Import the .json file inside postman_collection.
* Change whichever values you desire, inside of the available options, or simply execute each request as is.




## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST framework](https://www.django-rest-framework.org/) - An extension for the web framework
* [PostgreSQL](https://www.postgresql.org/) - Used to store the data
* [Docker](https://www.docker.com/) - Used to deploy the whole system more easily
* [Postman](https://www.postman.com/) - Used to give examples of usage
* Some other smaller ones 



## Authors

* **Diogo Goncalves** - *Whole project* - [Personal github](https://github.com/DGoncalves123)

