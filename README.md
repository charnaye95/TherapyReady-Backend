# TherapyReady - Backend App
 
[Link Deployed on Heroku](https://therapyready-backend.herokuapp.com/)
 
## Screenshots of the app
<br>

Clinics
![Clinics](https://i.imgur.com/iN4S3ZK.png "Clinics-backend")
<br>

Therapists
![Therapists](https://i.imgur.com/xFBvlvJ.png "Therapists-backend")
 
## Technologies used

Python, Django, Django Rest Frameworks

## Description

This application is part 1 of 2 of a full stack project. It holds the API for clinics and therapists within an area. A superuser was created and can be used in admin. The hope is to add clinics and therapists information with their prermission and fill up the database for people to use the site as a great resource.


## User Stories

A user could create, read, update, and delete information from the database.

## Stretch Goals and Major Hurdles

<ul>
<li>I would like to add user authentication from Django.</li>
<li>One major hurdle was trying to access the id of my objects. I didn't specifically put it in my models because Django is supposed to provide that. And they do, but I found out that you have to add it as a field to your serializers for it to show up.</li>
<li>A stretch goal would to be to change persmissions to only allow admins with a login to be able to CRUD information from the database.</li>
</ul>
