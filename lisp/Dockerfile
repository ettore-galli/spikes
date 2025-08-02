FROM ubuntu:22.04

# 1. Installa dipendenze essenziali
RUN apt-get update && \
    apt-get install -y \
    sbcl cl-asdf \
    git \
    curl \
    rlwrap \
    && rm -rf /var/lib/apt/lists/*

 
# 2. Installa Quicklisp  
RUN curl -sO https://beta.quicklisp.org/quicklisp.lisp && \
    curl -sO https://beta.quicklisp.org/quicklisp.lisp.asc && \
    sbcl --load quicklisp.lisp \
         --eval '(quicklisp-quickstart:install :path "/root/quicklisp")' \
         --eval '(ql-util:without-prompting (ql:add-to-init-file))' \
         --eval '(ql:update-all-dists)' \
         --quit

RUN git clone \
    https://github.com/nobody-famous/alive-lsp.git \
    /root/quicklisp/local-projects/alive-lsp
         
# Copia script di avvio  
COPY ./start-live-lsp.lisp /start-live-lsp.lisp    

EXPOSE 8006

CMD ["rlwrap", "sbcl",  "--load", "/start-live-lsp.lisp"]