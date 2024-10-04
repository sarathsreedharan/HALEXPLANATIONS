;; Unsolvable instance of the (3x3)-Puzzle.
;;
;; Initial state:     Goal state:
;; 1 2 5  ||  0 1 2
;; 6 4 7  ||  3 4 5
;; 0 8 3  ||  6 7 8
;;
(define (problem curr_prob)
  (:domain strips-sliding-tile)
  (:objects
    t1 t2 t3 t4 t5 t6 t7 t8 - obj
    p1 p2 p3 - obj
  )

  (:init
    {}
  )
  (:goal
    (and
        {}
    )
  )
)
