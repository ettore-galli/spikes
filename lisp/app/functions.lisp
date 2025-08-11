(defun somma (a b &optional c) (
    + a b (or c 100)
))

(defun multi (a) 
    (values a (* a a) (* a a a))
)

(defun circlearea (r)
    (let ((pig 3.1415927))
        (* pig r r)
    )
)

(defparameter *parametro* 100)

(defun prtvari ()
  (print *parametro*))

(defun loops() 
    (print "x")  
    (loops)
)