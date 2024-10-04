(define (domain rover)
(:requirements :strips :typing)
(:types rover waypoint store lander objective)

(:predicates 
             (at ?x - rover ?y - waypoint) 
             (can-traverse ?r - rover ?x - waypoint ?y - waypoint)
             (have-rock-analysis ?r - rover)
             (have-soil-analysis ?r - rover)
             (available ?r - rover)
             (connected ?w - waypoint ?p - waypoint)
	         (at-rock-sample ?w - waypoint)
	         (at-soil-sample ?w - waypoint)
             (equipped-for-rock-analysis ?r - rover)
             (equipped-for-soil-analysis ?r - rover)
             (rover-is-stable)
             (can-stabilize)
)

(:action stabilize
:parameters ()
:precondition (and (can-stabilize))
:effect (and (rover-is-stable))
)

(:action stabilized-navigate
:parameters (?x - rover ?y - waypoint ?z - waypoint)
:precondition (and (available ?x) (at ?x ?y)
                (connected ?y ?z) (rover-is-stable))
:effect (and (not (at ?x ?y)) (not (rover-is-stable)) (at ?x ?z))
)

(:action navigate
:parameters (?x - rover ?y - waypoint ?z - waypoint) 
:precondition (and (can-traverse ?x ?y ?z) (available ?x) (at ?x ?y) 
                (connected ?y ?z))
:effect (and (not (at ?x ?y)) (at ?x ?z)))


(:action sample-rock
:parameters (?x - rover ?p - waypoint)
:precondition (and (at ?x ?p) (at-rock-sample ?p) 
	           (equipped-for-rock-analysis ?x) )
:effect (and (have-rock-analysis ?x) 
	     (not (at-rock-sample ?p))))


(:action sample-soil
:parameters (?x - rover ?p - waypoint)
:precondition (and (at ?x ?p) (at-soil-sample ?p) 
	           (equipped-for-soil-analysis ?x) )
:effect (and (have-soil-analysis ?x)
	     (not (at-rock-sample ?p))
        )
)

)
