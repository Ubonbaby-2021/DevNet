# ITCDevNetFinal2021
- Name/Surname:
- Netacad username:
- Academy name:
- Github repository URL: 

## Instruction
1. Complete all 12 tasks below by replacing code to all <!!!REPLACEME!!!!> in this file within 1:30 hour
2. Fork a repository from https://github.com/chotipat/ITCDevNetFinal2021.git to your github repository.
3. Add chotipat@it.kmitl.ac.th as a collaborator in your github repository.
4. Rename file name by appending your name to "devasc-sa-dec2021.py" (e.g. devasc-sa-dec2021-chotipat.py).
5. Clone your github repository to your local computer repository.
6. Commit devasc-sa-dec2021-yourname.py to your local repository once in a while (e.g. every 15-20 mins) or whenever you completed some of the 12 tasks.
7. Push your local repository to your github repository.
8. As a backup route, please (attach) devasc-sa-dec2021-yourname.py and send email to chotipat@it.kmitl.ac.th within 10 minutes after exam.

## This program:
- Uses the hard-coded access token.
- Monitors the ITCProctoredFinal2021 Webex Team room every second for "/yourname location" message.
- Extract the location (city name) from a message starting with “/yourname location” (e.g. /chotipat Washington, DC -> Washington, DC).
- Discovers GPS coordinates (latitude and longitude) for the "location" using MapQuest API.
- Discovers the current weather description and temperature in degree Celsius of the specified latitude and longitude using openweathermap API. 
- Format and send the results back to the ITCProctoredFinal2021 Webex Teams room

## The examinee will:
1. Import libraries for API requests, JSON formatting, and time.
2. Assign the Webex hard-coded access token to the variable accessToken.
3. Prepare parameters get the latest message for messages API.
4. Provide the URL to the Webex Teams messages API, and extract location from the received message.
5. Provide your MapQuest API consumer key.
6. Provide the URL to the MapQuest address API.
7. Provide the MapQuest key values for latitude and longitude.
8. Prepare openweatherAPIGetParameters for OpenWeather API; current weather data for one location by geographic coordinates.
9. Provide the URL to the OpenWeather API; current weather data for one location.
10. Complete the code to get weather description and weather temperature.
11. Complete the code to format the response message.
12. Complete the code to post the message to the Webex Teams room.  

