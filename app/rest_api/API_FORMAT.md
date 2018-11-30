# API Format

The API for Flim aims to have a clear and concise format that will allow developers to utilize this API quickly and easily.


## Messages

Messages, such as the ones that would be shown with the `flash()` function in flask, would be put under the key `"msg"` instead.


## Errors

Error messages will be put in the `"error_msg"` tag.

For example, if we try to retrieve a user that does not exist, we will see:

```json
{
	"msg": "error",
	"error_msg": "The user you requested does not exist."
	
}
```

## Models

Models will use the variable names that were defined in the class. Let's take a look at an example here.
In this case, we will use the 'Users' class as an example with fabricated values:

 
```json
{
	"id": 34,
	"first_name": 34,
	"last_name": 34,
	"email": 34,
	"about": 34,
	"password_hashed": 34,
	"username": 34,
	
	"posts": [
		1228,2522,4213,8442
	],
	
	"responses": [
		34,51,92,4
	],
	
	"groups": [
		1,2,4,5
	],
}
```

In this case, if we look at the User class, we will find that instance variables that are retrieved from the database are usually under the same or similar name in the REST API.


