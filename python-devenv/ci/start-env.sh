docker container stop python-dev
docker container rm python-dev

docker run -it -p 8006:8006 -v "$(pwd)/app:/app" --name python-dev python-dev-env