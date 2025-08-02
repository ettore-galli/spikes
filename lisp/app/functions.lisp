(defun somma (a b &optional c) (
    + a b (or c 100)
))

(defun multi (a) 
    (values a (* a a) (* a a a))
)