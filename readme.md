## Environment Variables

Before running the project, make sure to set up the required environment variables. Create a `.env` file in the project root directory and define the following variables:

```plaintext
POSTGRES_USER=value  
POSTGRES_PASSWORD=value  
POSTGRES_DB=value  
POSTGRES_HOST=value  
POSTGRES_PORT=value  
REDIS_HOST=value  
REDIS_PORT=value  
```
#### Note! 
POSTGRES_HOST, REDIS_HOST vars should be set as container names, you can get names from docker-compose.yml.  
## Running

To run the project execute below command
<code> $ docker compose up --build </code>  
#### Note! What does this command do?  
It starts all services, provided in docker-compose.yml. At the end of starting 'web' service   
docker executes 'scripts/start_api.sh' bash script. This script is written to easy your work, feel free  
to change it, if you in need.

## Check tasks 
### task1
Copy provided below snippet and run it in terminal. Ps.Make sure to have curl installed.
<code>  
curl -X 'POST' \
  'http://0.0.0.0:8000/api/v1/questions/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "question_num": 2
}'  
</code>  
or if you prefer QUI, go to http://0.0.0.0:8000/docs#/question/save_questions_api_v1_questions__post  
### task2
My personal recomendation for checking task2 is to use swagger at http://0.0.0.0:8000/docs#.  
But incase if you are the terminal boy, then you can use next commands:  
***
Curl request to create user  
<code>
curl -X 'POST' \
  'http://0.0.0.0:8000/api/v1/users/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "string"
}</code>  
*** 
Curl request to upload wav file with user credentials
<code>  
curl -X 'POST' \
  'http://0.0.0.0:8000/api/v1/audios/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'audio_file=@file_example_WAV_1MG.wav;type=audio/x-wav' \
  -F 'id=user_id' \
  -F 'token=user_token'
</code>  
***
Curl request to downloadload mp3 file
<code>  
curl -X 'GET' \
  'http://0.0.0.0:8000/record?id=<file_id>&user=<user_id>' \
  -H 'accept: application/json'
</code>  
***


