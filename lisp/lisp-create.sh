docker build -t common-lisp-env .
docker run -it -p 4005:4005 -v "$(pwd):/app" --name lisp-dev common-lisp-env