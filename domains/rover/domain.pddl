(define (domain rover)
(:requirements :strips :typing)
(:types rover waypoint store lander objective)

(:predicates (at ?x - rover ?y - waypoint) 
             (at_lander ?x - lander ?y - waypoint)
             (can_traverse ?r - rover ?x - waypoint ?y - waypoint)
             (equipped_for_rock_analysis ?r - rover)
             (empty ?s - store)
             (have_rock_analysis ?r - rover ?w - waypoint)
             (full ?s - store)
             (available ?r - rover)
             (visible ?w - waypoint ?p - waypoint)
             (communicated_rock_data ?w - waypoint)
	         (at_rock_sample ?w - waypoint)
             (visible_from ?o - objective ?w - waypoint)
	         (store_of ?s - store ?r - rover)
	         (channel_free ?l - lander)
             (can_stabilize)
             (rover_is_stable)
             (inexploration)
)

(:action stabilize
:parameters ()
:precondition (and (can_stabilize))
:effect (and (rover_is_stable))
)

(:action stabilized_navigate
:parameters (?x - rover ?y - waypoint ?z - waypoint) 
:precondition (and (can_traverse ?x ?y ?z) (available ?x) (at ?x ?y) 
                (visible ?y ?z) (rover_is_stable))
:effect (and (not (at ?x ?y)) (not (rover_is_stable)) (at ?x ?z))
)

(:action navigate
:parameters (?x - rover ?y - waypoint ?z - waypoint) 
:precondition (and (can_traverse ?x ?y ?z) (available ?x) (at ?x ?y) 
                (visible ?y ?z))
:effect (and (not (at ?x ?y)) (at ?x ?z)))


(:action sample_rock
:parameters (?x - rover ?s - store ?p - waypoint)
:precondition (and (at ?x ?p) (at_rock_sample ?p) 
	           (equipped_for_rock_analysis ?x) (store_of ?s ?x)(empty ?s))
:effect (and (not (empty ?s)) (full ?s) (have_rock_analysis ?x ?p) 
	     (not (at_rock_sample ?p))))

(:action drop
:parameters (?x - rover ?y - store)
:precondition (and (store_of ?y ?x) (full ?y))
:effect (and (not (full ?y)) (empty ?y)))


(:action communicate_rock_data
 :parameters (?r - rover ?l - lander ?p - waypoint ?x - waypoint ?y - waypoint)
 :precondition (and (at ?r ?x)(at_lander ?l ?y)(have_rock_analysis ?r ?p)
                   (visible ?x ?y)(available ?r)(channel_free ?l))
 :effect (and (not (available ?r))(not (channel_free ?l))
	      (channel_free ?l)(communicated_rock_data ?p)(available ?r)))


(:action end_exploration
:parameters ()
:precondition (and (inexploration))
:effect (and (not (inexploration)))
)
)
