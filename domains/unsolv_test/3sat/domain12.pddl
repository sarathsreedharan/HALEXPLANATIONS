(define (domain satdom)
  (:requirements :typing :strips)
  (:types var clause)

  (:predicates
    (solved ?c - clause)
    (unassigned ?v - var)
  )

  (:action assign-v1-true
    :parameters ()
    :precondition (unassigned v1)
    :effect
    (and
      (not (unassigned v1))
      (solved c2)
      (solved c9)
      (solved c13)
      (solved c14)
      (solved c17)
    )
  )

  (:action assign-v2-true
    :parameters ()
    :precondition (unassigned v2)
    :effect
    (and
      (not (unassigned v2))
      (solved c0)
      (solved c3)
      (solved c11)
      (solved c20)
    )
  )

  (:action assign-v3-true
    :parameters ()
    :precondition (unassigned v3)
    :effect
    (and
      (not (unassigned v3))
      (solved c2)
      (solved c3)
      (solved c4)
      (solved c5)
      (solved c6)
      (solved c8)
      (solved c11)
      (solved c17)
    )
  )

  (:action assign-v4-true
    :parameters ()
    :precondition (unassigned v4)
    :effect
    (and
      (not (unassigned v4))
      (solved c0)
      (solved c4)
      (solved c7)
      (solved c14)
      (solved c19)
      (solved c21)
    )
  )

  (:action assign-v5-true
    :parameters ()
    :precondition (unassigned v5)
    :effect
    (and
      (not (unassigned v5))
      (solved c0)
      (solved c11)
      (solved c12)
      (solved c13)
      (solved c17)
      (solved c19)
      (solved c21)
    )
  )

  (:action assign-v1-false
    :parameters ()
    :precondition (unassigned v1)
    :effect
    (and
      (not (unassigned v1))
      (solved c4)
      (solved c6)
      (solved c7)
      (solved c15)
      (solved c18)
      (solved c19)
      (solved c21)
    )
  )

  (:action assign-v2-false
    :parameters ()
    :precondition (unassigned v2)
    :effect
    (and
      (not (unassigned v2))
      (solved c1)
      (solved c7)
      (solved c8)
      (solved c9)
      (solved c10)
      (solved c12)
      (solved c18)
    )
  )

  (:action assign-v3-false
    :parameters ()
    :precondition (unassigned v3)
    :effect
    (and
      (not (unassigned v3))
      (solved c1)
      (solved c10)
      (solved c13)
      (solved c14)
      (solved c15)
      (solved c16)
      (solved c18)
      (solved c20)
    )
  )

  (:action assign-v4-false
    :parameters ()
    :precondition (unassigned v4)
    :effect
    (and
      (not (unassigned v4))
      (solved c3)
      (solved c5)
      (solved c8)
      (solved c9)
      (solved c12)
      (solved c16)
      (solved c20)
    )
  )

  (:action assign-v5-false
    :parameters ()
    :precondition (unassigned v5)
    :effect
    (and
      (not (unassigned v5))
      (solved c1)
      (solved c2)
      (solved c5)
      (solved c6)
      (solved c10)
      (solved c15)
      (solved c16)
    )
  )

)
