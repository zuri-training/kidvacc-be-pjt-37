REST API docs for Kidvacc API
Base URL : Kidvacc API

~~~Open Endpoints~~~
Open endpoints requires Authentication.

Register : POST /api/child/rest-auth/registration/
Login : POST /api/child/rest-auth/login/
password reset: api/child/rest-auth/password/reset/

Endpoints that require Authentication
Closed endpoints require a valid Token to be included in the header of the request. A Token can be acquired from the Login view above.

Parent/Child profile to book an appointment
Each endpoint manipulates or displays information related to the User whose Token is provided with the request:

  child profile  : https://kidvacc.herokuapp.com/api/child/child
  parent profile : https://kidvacc.herokuapp.com/api/child/parent
  appointment :    https://kidvacc.herokuapp.com/api/child/appointment
  Hospital_type:   https://kidvacc.herokuapp.com/api/child/hospital_type
  Hospital_ details:https://kidvacc.herokuapp.com/api/child/hospital_details
  Payments      :   https://kidvacc.herokuapp.com/api/child/payments


Logout : GET https://kidvacc.herokuapp.com/api/child/rest-auth/logout/ 