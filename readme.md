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
## Running

To run the project run 
<code> $ docker compose up --build </code>
Apply migrations to database.  
To do it run next command
<code>$ docker exec -it "container-name of web" bash scripts/migrate </code>


## Check tasks 
#### task1
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
