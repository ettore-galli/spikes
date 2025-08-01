FROM ubuntu:22.04

# 1. Installa dipendenze essenziali
RUN apt-get update && \
    apt-get install -y \
    sbcl \
    git \
    curl \
    rlwrap \
    && rm -rf /var/lib/apt/lists/*

# 2. Installa Quicklisp  
RUN curl -sO https://beta.quicklisp.org/quicklisp.lisp && \
    curl -sO https://beta.quicklisp.org/quicklisp.lisp.asc && \
    sbcl --load quicklisp.lisp \
         --eval '(quicklisp-quickstart:install)' \
         --eval '(ql-util:without-prompting (ql:add-to-init-file))' \
         --eval '(ql:quickload :swank)' \
         --quit

# Copia script di avvio  
COPY ./start-swank.lisp /start-swank.lisp    

EXPOSE 4005
CMD ["sbcl",  "--load", "/start-swank.lisp"]