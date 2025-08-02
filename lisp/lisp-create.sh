docker container stop lisp-dev
docker container rm lisp-dev
docker build -t common-lisp-env .
docker run -it -p 8006:8006 -v "$(pwd)/app:/app" --name lisp-dev common-lisp-env