# Drumstick Authentication Module

## Introduction 
For starters Drumstick architecture is entirely decoupled. 
* We have the backend server that handles all requests and exposed APIs to be consumed by clients.
* We have clients consuming the exposed API's on the backend server.\
For now, the clients we have are:\
 - A web application. (Check it here)
 - A cross-platform flutter application (Check it here)

## Requirements
To understand how the Authentication works, you need to understand what it consists of.\
1. Registered clients - For an application to consume our API's it has to be a registered Client\ 
with a Client ID. (Follow this steps to obtain your client ID) 

## What Authentication methods are there?
We currently support 2 Authentication methods.
 1. Email and Password Authentication (Read more)
 2. Google Sign in (Read more) (NOT DONE)

### Email and Password Authentication
Before using this authentication method, please ensure you have satisfied the Requirements section (Requirements section)\

If you have. Let's proceed.

#### How it works
So the flow of how the request works from the client to the server and back to the client is as follows:\
Let's take an example of a signup request. (For the full list of endpoints, please check here)\

A client makes a post request to the server on the endpoint `api/signup`\
The required fields are:\
```javascript
    "email": "user_email@email.com",
    "username": "Username to be assigned for the user",
    "password": "A strong enough password",
    "client_id": "The client ID of the client making the request" 
```
If any of these fields are missing or not correct, an error is thrown. (Please check here for more details)\

If you want to jump straight to the responses section go here.

#### So what happens next?
After the fields are satisfied the module is called through the method `signup_with_email_and_password(username, email, password)` (Check module doc for more info)\
An internal method `check_if_user_exists(email)` is called to check if a user with that email exists. If they do an error is thrown.\
Another method `check_if_username_exists(username)` is called, and if a user with that username exists, an error is also thrown.\
If all those pass, a method ` create_user_account(username, email, password):` is called that records the users credentials in the database. (Of course the user's password is hashed first.)\
If that is also successful, `generate_auth_token(user_id)` is called. This method takes in the user's id and encrypts and generates a jwt token. (Read more on jwt tokens). The token being generated also has a few more payloads added to it.
`'iat': That is when the token was issued,`\
`'exp': That is when the token will expire and the user will have to generate a new token.`\
We also require our PRIVATE_KEY to encode the token and PUBLIC_KEY while decoding it. We currently use the `RS256` algorithm for encoding. (Requires a PUBLIC_KEY PRIVATE_KEY combo to encode(PRIVATE_KEY) and decode (PUBLIC_KEY))\
Finally the jwt token is returned to the client with the appropriate success code.

That is the general flow of all the requests we expect on our server.

IMOPRTANT\
Just to reiterate, we require:
1. All requests to protected routes to contain the Authorization token on the request header.
2. All requests to contain valid client_id of the client from which the requests originates from.

