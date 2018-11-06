# Six-Degrees-Of-Spotify
Testing out the "Six degrees of seperation" idea using Spotify's API. It works by looking at an artists "related artists" and runs a best first search algorithm.

## How to run script
To run the script you will have to have a Spotify account. 

Follow this guide to get a client id and client secret: https://developer.spotify.com/documentation/web-api/quick-start/

You will have to add a redirect url for your app under "edit settings" on the Dashboard page. 

When you are done with that, add the client id, client secret and redirect url to the script and run the script with "artist 1" as first argument and "artist 2" as second argument. 
```python
client_id = "" ## insert your client_id
client_secret = "" ##insert your client_secret
```
