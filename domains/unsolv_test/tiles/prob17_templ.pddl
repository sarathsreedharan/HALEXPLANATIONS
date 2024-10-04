;; Unsolvable instance of the (3x4)-Puzzle.
;;
;; Initial state:     Goal state:
;;  7  4  3  ||   0  1  2
;;  5  1  2  ||   3  4  5
;;  0 10  9  ||   6  7  8
;;  6 11  8  ||   9 10 11
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
