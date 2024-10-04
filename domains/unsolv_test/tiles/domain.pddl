
;; The sliding-tile puzzle (i.e. the eight/fifteen/twentyfour puzzle).
;; Tile positions are encoded by the predicate (at <tile> <x> <y>), i.e.
;; using one object for horizontal position and one for vertical (there's
;; a separate predicate for the position of the blank). The predicates
;; "inc" and "dec" encode addition/subtraction of positions.

;; The instance files come in two flavors: The vanilla one uses the same
;; objects for both x and y coordinates, while the other (files that have
;; an "x" at the end of their name) uses different objects for x and y
;; coordinates; this is because some planners seem to require different
;; objects for each parameter of an operator.

(define (domain strips-sliding-tile)
  (:requirements :strips :typing)
  (:types obj - object)
  (:predicates
   (tile ?x - obj) (xposition ?x - obj) (yposition ?x - obj)
   (at ?t ?x - obj ?y - obj) (blank ?x - obj ?y - obj)
   (inc ?p - obj ?pp - obj) (dec ?p - obj ?pp - obj))



  (:action move-up
    :parameters (?a - obj ?b - obj ?c - obj ?d - obj)
    :precondition (and
		   (tile ?a) (xposition ?b) (yposition ?c) (yposition ?d)
		   (dec ?d ?c) (blank ?b ?d) (at ?a ?b ?c))
    :effect (and (not (blank ?b ?d)) (not (at ?a ?b ?c))
		 (blank ?b ?c) (at ?a ?b ?d)))

  (:action move-down
    :parameters (?a - obj ?b - obj ?c - obj ?d - obj)
    :precondition (and
		   (tile ?a) (xposition ?b) (yposition ?c) (yposition ?d)
		   (inc ?d ?c) (blank ?b ?d) (at ?a ?b ?c))
    :effect (and (not (blank ?b ?d)) (not (at ?a ?b ?c))
		 (blank ?b ?c) (at ?a ?b ?d)))

  (:action move-left
    :parameters (?a - obj ?b - obj ?c - obj ?d - obj)
    :precondition (and
		   (tile ?a) (xposition ?b) (yposition ?c) (xposition ?d)
		   (dec ?d ?b) (blank ?d ?c) (at ?a ?b ?c))
    :effect (and (not (blank ?d ?c)) (not (at ?a ?b ?c))
		 (blank ?b ?c) (at ?a ?d ?c)))

  (:action move-right
    :parameters (?a - obj ?b - obj ?c - obj ?d - obj)
    :precondition (and
		   (tile ?a) (xposition ?b) (yposition ?c) (xposition ?d)
		   (inc ?d ?b) (blank ?d ?c) (at ?a ?b ?c))
    :effect (and (not (blank ?d ?c)) (not (at ?a ?b ?c))
		 (blank ?b ?c) (at ?a ?d ?c)))
  )
