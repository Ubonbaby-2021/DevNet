#######################################################################################
# FirstName/Surname:
# Netacad username:
# Academy name:
# Github repository URL: 
#######################################################################################
# Instruction
# Reads README.md in https://github.com/chotipat/ITCDevNetFinal2021 for more information.
#######################################################################################
 
#######################################################################################
# 1. Import libraries for API requests, JSON formatting, and time.

<!!!REPLACEME with code for libraries>

#######################################################################################
# 2. Assign the Webex hard-coded access token to the variable accessToken.


accessToken = "Bearer <!!!REPLACEME with hard-coded token!!!>" 

#######################################################################################
# 3. Prepare GetParameters to get the latest message for messages API.

# Defines a variable that will hold the roomId 
roomIdToGetMessages = "<!!!REPLACEME with roomID of the ITCProctoredFinal2021 Webex Teams room!!!>" 

while True:
    # always add 1 second of delay to the loop to not go over a rate limit of API calls
    time.sleep(1)

    # the Webex Teams GET parameters
    #  "roomId" is the ID of the selected room
    #  "max": 1  limits to get only the very last message in the room
    GetParameters = {
                            "roomId": roomIdToGetMessages,
                            "max": 1
                        }
  
# 4. Provide the URL to the Webex Teams messages API, and extract location from the received message.
    # Send a GET request to the Webex Teams messages API.
    # - Use the GetParameters to get only the latest message.
    # - Store the message in the "r" variable.
    r = requests.get("<!!!REPLACEME with URL!!!>",
                         params = GetParameters, 
                         headers = {"Authorization": accessToken}
                    )
    # verify if the retuned HTTP status code is 200/OK
    if not r.status_code == 200:
        raise Exception( "Incorrect reply from Webex Teams API. Status code: {}. Text: {}".format(r.status_code, r.text))
    
    # get the JSON formatted returned data
    json_data = r.json()
    # check if there are any messages in the "items" array
    if len(json_data["items"]) == 0:
        raise Exception("There are no messages in the room.")
    
    # store the array of messages
    messages = json_data["items"]
    # store the text of the first message in the array
    message = messages[0]["text"]
    print("Received message: " + message)
    
    # check if the text of the message starts with the magic character "/" and yourname followed by a location name
    # e.g.  "/chotipat San Jose"
    if message.find("<!!!REPLACEME!!!>") == 0:
        # extract name of a location (city) where we check for GPS coordinates using the MapQuest API
        # Enter code below to hold city name in location variable.
        # For example location should be "San Jose" if the message is "/chotipat San Jose".
        location = "<!!!REPLACEME!!!>" 
     
# 5. Provide your MapQuest API consumer key.
        # MapQuest API GET parameters:
        # - "location" is the the location to lookup
        # - "key" is the Consumer Key you generated at https://developer.mapquest.com/user/me/apps
        mapsAPIGetParameters = { 
                                "location": location, 
                                "key": "<!!!REPLACEME with your MapQuest API Key!!!>" 
                               }
        
# 6. Provide the URL to the MapQuest address API.
        # Get location information using the MapQuest API geocode service using the HTTP GET method
        r = requests.get("<!!!REPLACEME with URL!!!>", 
                             params = mapsAPIGetParameters
                        )
        # Verify if the returned JSON data from the MapQuest API service are OK
        json_data = r.json()
        # check if the status key in the returned JSON data is "0"
        if not json_data["info"]["statuscode"] == 0:
            raise Exception("Incorrect reply from MapQuest API. Status code: {}".format(r.statuscode))

# 7. Provide the MapQuest key values for latitude and longitude.
        # Set the lat and lng key as retuned by the MapQuest API in variables
        locationLat = json_data["<!!!REPLACEME!!!> with path to latitude key!!!>"]
        locationLng = json_data["<!!!REPLACEME!!!> with path to longitude key!!!>"]

# 8. Prepare openweatherAPIGetParameters for OpenWeather API; current weather data for one location by geographic coordinates.
        # Use current weather data for one location by geographic coordinates API service in Openweathermap
        openweatherAPIGetParameters = {
                                "<!!!REPLACEME!!!> with all key:value pairs of parameters!!!>"
                            }

# 9. Provide the URL to the OpenWeather API; current weather data for one location.
        rw = requests.get("<!!!REPLACEME with URL!!!>", 
                             params = openweatherAPIGetParameters
                        )
        json_data_weather = rw.json()

        if not "weather" in json_data_weather:
            raise Exception("Incorrect reply from openweathermap API. Status code: {}. Text: {}".format(rw.status_code, rw.text))

# 10. Complete the code to get weather description and weather temperature
        weather_desc = json_data_weather["<!!!REPLACEME!!!> with path to weather description key!!!>"]
        weather_temp = json_data_weather["<!!!REPLACEME!!!> with path to weather temperature key!!!>"]

# 11. Complete the code to format the response message.
        # Example responseMessage result: In Austin, Texas (latitude: 30.264979, longitute: -97.746598), the current weather is clear sky and the temperature is 12.61 degree celsius.
        responseMessage = "In {} (latitude: {}, longitute: {}), the current weather is {} and the temperature is {} degree celsius.\n".format(<!!!REPLACEME with required variables!!!>)
        # print("Sending to Webex Teams: " + responseMessage)


# 12. Complete the code to post the message to the Webex Teams room.         
        # the Webex Teams HTTP headers, including the Authoriztion and Content-Type
        HTTPHeaders = { 
                             "Authorization": <!!!REPLACEME!!!>,
                             "Content-Type": "application/json"
                           }
        # The Webex Teams POST JSON data
        # - "roomId" is is ID of the selected room
        # - "text": is the responseMessage assembled above
        PostData = {
                            "roomId": <!!!REPLACEME!!!>,
                            "text": <!!!REPLACEME!!!>
                        }
        # Post the call to the Webex Teams message API.
        r = requests.post( "<!!!REPLACEME with URL!!!>", 
                              data = json.dumps(<!!!REPLACEME!!!>), 
                              headers = <!!!REPLACEME!!!>
                         )
        if not r.status_code == 200:
            raise Exception("Incorrect reply from Webex Teams API. Status code: {}. Text: {}".format(r.status_code, r.text))
