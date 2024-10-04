;; Peg Solitaire domain

(define (domain pegsolitaire-netbenefit)
    (:requirements :typing )
    (:types location - object)
    (:predicates
        (IN-LINE ?x ?y ?z - location)
        (occupied ?l - location)
        (free ?l - location)
        {}
    )
        {}

)
