# Flim API Format

The API for Flim aims to have a clear and concise format that will allow developers to utilize this API quickly and easily.

## Basic Information

### Messages

Messages, such as the ones that would be shown with the `flash()` function in flask, would be put under the key `"msg"` instead.


### Errors

Error messages will be put in the `"error_msg"` tag.

For example, if we try to retrieve a user that does not exist, we will see:

```json
GET /api/user/1810181

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
GET /api/user/34

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
"data": {
	"parent_post": 3171,
	"creator": 3843,
	"content": "I want to second this idea. I really think that this can <b>add a lot of potential</b> to the project.",
}
```
	
Note: we omit the timestamp because Python will take care of this for us.

## Authentication

To keep things simple, we omitted API keys and HTTP basic authentication from other requests, but you must provide authentication or you will get a 403 Forbidden error when tryng to do something with the API.

### Using API Keys

#### Creating 

In order to retrieve an API key, send a PUT request to `/api/key/retrieve` with HTTP basic authentication, with your username as the username and password that you normally use to log in to Flim. The API key retrieval will then send you a response such as this:

```json
PUT /api/key/retrieve

{
	"api_key" : "SAMPLEAPIKEY",
	"days_till_expiry": 30
}
```

The `days_till_expiry` key will tell you how many **days** after the day of requesting the API key the current API key will expire. The reason we do this is so that administrators can set the expiry date for API keys.

#### Destroying

In order to destroy an API key, send a PUT request to `/api/key/destroy` with the parameters:

```json
"data": {
	"api_key": "YOUR_API_KEY_HERE"
}

```

## URLs


### Finding and Using URLs

With access URLs, you can append `/by-<column_name>` in order to access the model by a certain value. For example, if we wanted to access the user with `id` 3291, we would send a GET request to `/api/user/by-id/3291`. Similarly, if we wanted to access posts with topic "Announcements", we would send our GET request to `/api/user/by-topic/Announcement`.
With delete URLs, you must append a valid column identifier. 
With modify URLs, you must append a valid column identifier along with the new values for the columns that you wish to alter.


Model|Access URL|Add URL|Modify URL|Delete URL
--- | --- | --- | --- | ---
|Users|`/api/user/retrieve`|`/api/user/add`|`/api/user/modify`|`/api/user/delete`
|Post|`/api/post/retrieve`|`/api/post/add`|`/api/post/modify`|`/api/post/delete`

