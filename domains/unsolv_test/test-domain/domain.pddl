(define (domain toggle)

    (:requirements :equality :typing)

    (:predicates 
            (p) (q) (g)
    )

    (:action toggle1
        :parameters ()
        :precondition (and (p))
        :effect (and (not (p)) (q))
    )
    
    (:action toggle2
        :parameters ()
        :precondition (and (q))
        :effect (and (not (q)) (p))
    )
    
    (:action win
        :parameters ()
        :precondition (and (p) (q))
        :effect (and (g))
    )
)
