REST API docs for Kidvacc API
Base URL : Kidvacc API

Open Endpoints
Open endpoints requires Authentication.

Register : POST /api/v1/user/register
Login : POST /api/v1/user/login
password reset:
Endpoints that require Authentication
Closed endpoints require a valid Token to be included in the header of the request. A Token can be acquired from the Login view above.

Parent/Child profile to book an appointment
Each endpoint manipulates or displays information related to the User whose Token is provided with the request:



Logout : GET https://kidvacc.herokuapp.com/api/child/rest-auth/logout/ 