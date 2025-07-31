# Usa un'immagine base Ubuntu
FROM ubuntu:22.04

# Installa dipendenze
RUN apt-get update && \
    apt-get install -y \
    sbcl \
    git \
    curl \
    make \
    rlwrap \
    gpg \
    && rm -rf /var/lib/apt/lists/*

# Configura ambiente SBCL e Quicklisp
RUN curl -O https://beta.quicklisp.org/quicklisp.lisp && \
    curl -O https://beta.quicklisp.org/quicklisp.lisp.asc && \
    sbcl --load quicklisp.lisp \
         --eval '(quicklisp-quickstart:install)' \
         --eval '(let ((ql-util::*do-not-prompt* t)) (ql:add-to-init-file))' \
         --quit

# Carica Quicklisp automaticamente in SBCL
RUN echo '(load "~/quicklisp/setup.lisp")' >> ~/.sbclrc

# Installa Swank
RUN sbcl --eval '(load "~/quicklisp/setup.lisp")' \
         --eval '(ql:quickload :swank)' \
         --quit

# Crea script di avvio
RUN echo '(load "~/quicklisp/setup.lisp")' > /start-swank.lisp && \
    echo '(ql:quickload :swank)' >> /start-swank.lisp && \
    echo '(swank:create-server :port 4005 :dont-close t)' >> /start-swank.lisp

# Esponi porta e avvia
EXPOSE 4005
CMD ["sbcl", "--load", "/start-swank.lisp"]