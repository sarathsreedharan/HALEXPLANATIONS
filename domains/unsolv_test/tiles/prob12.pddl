;; Unsolvable instance of the (3x4)-Puzzle.
;;
;; Initial state:     Goal state:
;;  6  2  3  ||   0  1  2
;;  7  8  5  ||   3  4  5
;;  1  0 10  ||   6  7  8
;;  9 11  4  ||   9 10 11
;;
(define (problem curr_prob)
  (:domain strips-sliding-tile)
  (:objects 
    t1 t2 t3 t4 t5 t6 t7 t8 t9 t10 t11 - obj
    p1 p2 p3 p4 - obj
  )

  (:init
    (tile t1)
    (tile t2)
    (tile t3)
    (tile t4)
    (tile t5)
    (tile t6)
    (tile t7)
    (tile t8)
    (tile t9)
    (tile t10)
    (tile t11)

    (xposition p1)
    (xposition p2)
    (xposition p3)

    (yposition p1)
    (yposition p2)
    (yposition p3)
    (yposition p4)

    (inc p1 p2) (inc p2 p3) (inc p3 p4)
    (dec p2 p1) (dec p3 p2) (dec p4 p3)

    (at t6 p1 p1)
    (at t2 p2 p1)
    (at t3 p3 p1)
    (at t7 p1 p2)
    (at t8 p2 p2)
    (at t5 p3 p2)
    (at t1 p1 p3)
    (blank p2 p3)
    (at t10 p3 p3)
    (at t9 p1 p4)
    (at t11 p2 p4)
    (at t4 p3 p4)
  )

  (:goal
    (and
      (at t1 p2 p1)
      (at t2 p3 p1)
      (at t3 p1 p2)
      (at t4 p2 p2)
      (at t5 p3 p2)
      (at t6 p1 p3)
      (at t7 p2 p3)
      (at t8 p3 p3)
      (at t9 p1 p4)
      (at t10 p2 p4)
      (at t11 p3 p4)
    )
  )
)
