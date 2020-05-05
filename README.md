# heycar-test

## To run the app in docker (from the project root dir)
docker-compose -f .docker/development/docker-compose.yml up --build

This should perform the migrations etc and get you an app available locally at http://localhost:8080/ui/

## Running the (very) basic integration tests
Shell into the docker container with `docker exec -ti heycar-test-app bash`

Run `pytest` from with the `/app` dir

## To use
visit http://localhost:8080/ui/ 

POST an image (upload one - click the "Try it out" button in the UI)

Grab the image id that's returned in the JSON

Go to the GET section and again click "Try it out"

Paste in the image_id and retrieve the details as JSON

Try visiting the image URL given in the response
