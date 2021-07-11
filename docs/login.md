Login
Used to collect a Token for a registered User.

URL : /api/child/rest-auth/login/

Method : POST

Auth required : yes

Data constraints

{
    "username": "[unique name]",
    "email": "[valid email address]",
    "password": "[password in plain text]"
    "password 2": "[reconfirm your password]",
}
<!-- Data example

{
    "email": " ",
    "password": " "
}
Success Response
Code : 200 OK -->

<!-- Content example

{
    "status":"success",
    "token": "93144b288eb1fdccbe46d6fc0f241a51766ecd3d",
    "store": {
        "_id": "60d97bb252737cb5b8c3e30c",
        "name": "",
        "email": "",
        "address": " ",
        "__v": 0
    }
} -->
Error Response
Condition : If 'email' and 'password' combination is wrong.

Code : 500 Internal Server Error

Content :

<!-- <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>Error: Incorrect email or password<br> &nbsp; &nbsp;at exports.login</pre>
</body>
</html> -->
