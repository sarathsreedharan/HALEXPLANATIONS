;; Unsolvable instance of the (3x3)-Puzzle.
;;
;; Initial state:     Goal state:
;; 7 8 3  ||  0 1 2
;; 5 1 0  ||  3 4 5
;; 6 2 4  ||  6 7 8
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
