;; Unsolvable instance of the (3x4)-Puzzle.
;;
;; Initial state:     Goal state:
;;  7  1  3  ||   0  1  2
;; 10  4  6  ||   3  4  5
;; 11  9  0  ||   6  7  8
;;  8  2  5  ||   9 10 11
;;
(define (problem curr_prob)
  (:domain strips-sliding-tile)
  (:objects
    t1 t2 t3 t4 t5 t6 t7 t8 t9 t10 t11 - obj
    p1 p2 p3 p4 - obj
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
