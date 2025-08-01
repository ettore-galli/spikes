(ql:quickload :swank)

;; Configurazioni ESSENZIALI per Docker
(setq swank:*communication-style* :fd-handler)   

;; Logging
(let ((log-file #P"/tmp/swank.log"))
  (ensure-directories-exist log-file)
  (setf swank::*log-events* t
        swank::*log-output* (open log-file :direction :output 
                                      :if-exists :append 
                                      :if-does-not-exist :create)))

(swank:create-server 
  :port 4005
  :style :fd-handler   
  :dont-close t
  :interface "0.0.0.0")   