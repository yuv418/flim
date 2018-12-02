# API Format

The API for Flim aims to have a clear and concise format that will allow developers to utilize this API quickly and easily.

## Basic Information

### Messages

Messages, such as the ones that would be shown with the `flash()` function in flask, would be put under the key `"msg"` instead.


### Errors

Error messages will be put in the `"error_msg"` tag.

For example, if we try to retrieve a user that does not exist, we will see:

```json
{
	"msg": "error",
	"error_msg": "The user you requested does not exist."
	
}
```




## Retrieving Data

Let's take a look at the basics of retrieving data with this REST API.


### Models

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
Another important point to be mentioned is the fact that any links to other models in the database will always be linked by the id of the resource. For example, if a user makes a post, the posts the user has made will be shown in the id form that can be used in order to find the full post.

## Adding Information

Let's take a look at adding information using this REST API. You'll have to use PUT requests in order to do this. Typically, the program will return

### Models

	To add an entry to a model, you must submit a PUT request with parameters containing similar information to what **you would recieve with a get** request.
	
	Let's take a look at example data that you would put in a PUT request if we were, for example, adding a response to a post, you would send the data:
	```json
	{
		"parent_post": 3171,
		"creator": 3843,
		"content": "I want to second this idea. I really think that this can <b>add a lot of potential</b> to the project.",
		
		
		
	}
	```	
	
	Note: we omit the timestamp because Python will take care of this for us.




