# Authentication on dajngo-rest-framework using Django OAuth Toolkit
Make your own Authorization Server to issue access tokens to client applications for a certain API.

1) Create a virtualenv and install following packages using pip.

		pip install django-oauth-toolkit 

		pip install djangorestframework

2) Run project and visit http://localhost:8000/admin

		create some users
		
3) Register an application : 
To obtain a valid access_token first we must register an application.

		http://localhost:8000/o/applications/
	
4) fill the form with the following data:
		
		1.Name: just a name of your choice
		
		2.Client Type: confidential
		
		3.Authorization Grant Type: Resource owner password-based

5) Get the token:

		To request an access_token. Open your shell and,
		
		curl -X POST -d "grant_type=password&username=<user_name>&password=<password>" -u"<client_id>:<client_secret>" http://localhost:8000/o/token/

		The user_name and password are the credential of the users registered in our Authorization Server, 
		
		Here response should be something like:
		
		{
			"access_token": "<your_access_token>",
			"token_type": "Bearer",
			"expires_in": 36000,
			"refresh_token": "<your_refresh_token>",
			"scope": "read write groups"
		}
		
6) Retrieve users
		
		curl -H "Authorization: Bearer <your_access_token>" http://localhost:8000/users/
