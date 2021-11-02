# Eiya Test (Joseph)

### Get Project to work 
* Create a virtual environment and install packages with
```pip install -r /etc/requirements.txt```
* Run migrations ```./manage.py migrate ```
* To populate cities and distances run ```./manage.py create_test_cities```
* To create "n" test vehicles run ```./manage.py create_test_vehicles n```
* Run project with ```./manage.py runserver```
* Go to http://127.0.0.1:8000


### How to use

There is only 1 screen at /.
Here you can create, update or delete vehicles and also register new
trips for them.

Registering new cities can be done from django admin at usual url http://127.0.0.1:8000/admin

For best performance be sure to register distances between cities every time you 
create a new city.

### How it works
There are 2 main modules, Vehicles and Cities.
Cities is used to register new cities and distances between them.
Vehicles is used to register vehicles and keep record of their trips.

#### Cities
*Model City:

    "name": str

*Model Distance:

    "city_1": FK to City
    "city_2": FK to City
    "distance": float

Distance objects are planned to be symmetric, i.e, if distance from A to B
is defined as 20, it would understand that distance from B to A is also 20 and 
therefore there can only be one distance object involving city A and B (in any order).


####Vehicles
*Model Trip:

    "vehicle": FK to Vehicle
    "origin": FK to City
    "destiny": FK to City
    "distance_traveled": float (non editable)
    "created": creation timestamp

Trips with same origin and destiny are not allowed.
Trips are only allowed if trip's origin is vehicle's current_location.
distance_traveled is auto calculated searching a Distance instance 
involving trip's origin and destiny, if there is not such instance it would be None.


*Model Vehicle:

    "id": str
    "current_location": FK to City
    "fuel_consumption": float
    "distance_traveled": float (non editable)
    "fuel_consumed": float (non editable)

distance_traveled is auto calculated as the sum of the vehicle's trips distances.
fuel_consumed is calculated as distance_traveled / fuel_consumption 


### Things that could be done to improve the app

Here I write a list of some improvements that i wanted to do but
I couldn't complete in time, (I'll try to make at least one before the end of the day)

* Vehicle Delete confirmation.
* Print API response Errors in screen when sending a wrong form.
* Update Trips distance when Distance between cities change and therefore vehicle's calculated variables (Not sure if this would be a desired behavior)
* A Screen to see Vehicle's trips history.
* Allow city and distances registration outside django admin.