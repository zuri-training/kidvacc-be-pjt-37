Register as a Parent
A parent creates an account on the Kidvacc site to be able to able to book an appointment for their Children.
 and receive a token.

URL : https://kidvacc.herokuapp.com/api/child/rest-auth/registration/

Method : POST

Auth required : yes

<!-- Data constraints

{
    "name": "[    ]",
    "email": "[]",
    "password": "[password in plain text]",
    "passwordConfirm": "[repeat password in plain text]",
    
    } -->
}
<!-- Data example

{
    "name": "",
    "email": "",
    "password": "",
    "passwordConfirm": "password1",
    "address": "",
    
    }
} -->
Success Response
Code : 200 OK

<!-- Content example

{
    "status": "success",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYwZDliY2U4MzdkYTNiY2M5MGU0M2UzZSIsImlhdCI6MTYyNDg4MjQwOCwiZXhwIjoxNjI0ODgyNDA4fQ.h4pEwyypPh3ZaPu37kQnBrhrxPEmENDxWSBppKNAX24",
    "store": {
        "_id": "60d9bce837da3bcc90e43e3e",
        "name": "",
        "email": "",
        "address": "",
        "
        },
        "__v": 0
    }
} -->
Error Response
Condition : If 'email' is wrong.

Code : 500 Internal Server error

<!-- Content :

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
