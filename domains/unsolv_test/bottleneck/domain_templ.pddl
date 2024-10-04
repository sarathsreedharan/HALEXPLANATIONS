(define (domain Resources)
	(:requirements :typing)
    (:types pers loc)
	(:predicates (location ?loc - loc)
		     (person ?p - pers)
		     (person-at ?p - pers ?loc - loc)
		     (connected ?loc1 - loc ?loc2 - loc)
		     (active ?loc - loc)
             {}
    )


    {}

)
