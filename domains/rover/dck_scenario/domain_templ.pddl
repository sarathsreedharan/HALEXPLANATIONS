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
             (store-of ?s - store ?r - rover)
             (equipped-for-rock-analysis ?r - rover)
             (equipped-for-soil-analysis ?r - rover)
             (rover-is-stable)
             (can-stabilize)
             {}
)

            {}
)
