(ql:quickload :swank)

(setq 
    swank:*communication-style* :fd-handler
    swank::*log-events* t
)
 

(swank:create-server 
  :port 4005
  :style :fd-handler   
  :dont-close t
  :interface "0.0.0.0"
)   

(force-output)