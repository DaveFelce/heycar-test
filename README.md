# heycar-test

## To run the app in docker (from the project root dir)
docker-compose -f .docker/development/docker-compose.yml up --build

This should perform the migrations etc and get you an app available locally at http://localhost:8080/ui/

## Running the (very) basic integration tests
Shell into the docker container with `docker exec -ti heycar-test-app bash`

Run `pytest` from with the `/app` dir

