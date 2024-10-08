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
      (solved c3)
      (solved c5)
      (solved c13)
      (solved c26)
      (solved c31)
      (solved c35)
      (solved c39)
      (solved c40)
    )
  )

  (:action assign-v2-true
    :parameters ()
    :precondition (unassigned v2)
    :effect
    (and
      (not (unassigned v2))
      (solved c4)
      (solved c12)
      (solved c23)
      (solved c27)
      (solved c36)
      (solved c37)
    )
  )

  (:action assign-v3-true
    :parameters ()
    :precondition (unassigned v3)
    :effect
    (and
      (not (unassigned v3))
      (solved c20)
      (solved c32)
      (solved c37)
      (solved c41)
      (solved c42)
    )
  )

  (:action assign-v4-true
    :parameters ()
    :precondition (unassigned v4)
    :effect
    (and
      (not (unassigned v4))
      (solved c4)
      (solved c11)
      (solved c13)
      (solved c30)
      (solved c31)
      (solved c38)
    )
  )

  (:action assign-v5-true
    :parameters ()
    :precondition (unassigned v5)
    :effect
    (and
      (not (unassigned v5))
      (solved c4)
      (solved c15)
      (solved c18)
      (solved c21)
      (solved c25)
      (solved c34)
      (solved c37)
      (solved c42)
    )
  )

  (:action assign-v6-true
    :parameters ()
    :precondition (unassigned v6)
    :effect
    (and
      (not (unassigned v6))
      (solved c8)
      (solved c23)
    )
  )

  (:action assign-v7-true
    :parameters ()
    :precondition (unassigned v7)
    :effect
    (and
      (not (unassigned v7))
      (solved c1)
      (solved c6)
      (solved c12)
      (solved c16)
    )
  )

  (:action assign-v8-true
    :parameters ()
    :precondition (unassigned v8)
    :effect
    (and
      (not (unassigned v8))
      (solved c5)
      (solved c10)
      (solved c14)
      (solved c17)
      (solved c24)
    )
  )

  (:action assign-v9-true
    :parameters ()
    :precondition (unassigned v9)
    :effect
    (and
      (not (unassigned v9))
      (solved c10)
      (solved c12)
      (solved c13)
      (solved c15)
      (solved c21)
      (solved c29)
      (solved c33)
      (solved c34)
      (solved c38)
    )
  )

  (:action assign-v10-true
    :parameters ()
    :precondition (unassigned v10)
    :effect
    (and
      (not (unassigned v10))
      (solved c1)
      (solved c6)
      (solved c8)
      (solved c31)
      (solved c32)
    )
  )

  (:action assign-v1-false
    :parameters ()
    :precondition (unassigned v1)
    :effect
    (and
      (not (unassigned v1))
      (solved c0)
      (solved c2)
      (solved c6)
      (solved c7)
      (solved c9)
      (solved c15)
      (solved c17)
      (solved c22)
      (solved c25)
      (solved c32)
    )
  )

  (:action assign-v2-false
    :parameters ()
    :precondition (unassigned v2)
    :effect
    (and
      (not (unassigned v2))
      (solved c16)
      (solved c18)
      (solved c26)
      (solved c30)
      (solved c33)
      (solved c40)
    )
  )

  (:action assign-v3-false
    :parameters ()
    :precondition (unassigned v3)
    :effect
    (and
      (not (unassigned v3))
      (solved c18)
      (solved c24)
      (solved c38)
    )
  )

  (:action assign-v4-false
    :parameters ()
    :precondition (unassigned v4)
    :effect
    (and
      (not (unassigned v4))
      (solved c0)
      (solved c9)
      (solved c14)
      (solved c16)
      (solved c17)
      (solved c26)
      (solved c39)
    )
  )

  (:action assign-v5-false
    :parameters ()
    :precondition (unassigned v5)
    :effect
    (and
      (not (unassigned v5))
      (solved c2)
      (solved c19)
      (solved c20)
      (solved c22)
      (solved c28)
      (solved c29)
      (solved c30)
    )
  )

  (:action assign-v6-false
    :parameters ()
    :precondition (unassigned v6)
    :effect
    (and
      (not (unassigned v6))
      (solved c0)
      (solved c10)
      (solved c11)
      (solved c22)
      (solved c24)
      (solved c28)
      (solved c34)
    )
  )

  (:action assign-v7-false
    :parameters ()
    :precondition (unassigned v7)
    :effect
    (and
      (not (unassigned v7))
      (solved c2)
      (solved c3)
      (solved c5)
      (solved c7)
      (solved c19)
      (solved c20)
      (solved c21)
      (solved c23)
      (solved c27)
      (solved c35)
      (solved c40)
      (solved c41)
    )
  )

  (:action assign-v8-false
    :parameters ()
    :precondition (unassigned v8)
    :effect
    (and
      (not (unassigned v8))
      (solved c7)
      (solved c9)
      (solved c25)
      (solved c35)
    )
  )

  (:action assign-v9-false
    :parameters ()
    :precondition (unassigned v9)
    :effect
    (and
      (not (unassigned v9))
      (solved c1)
      (solved c8)
      (solved c11)
      (solved c27)
      (solved c28)
      (solved c36)
      (solved c41)
    )
  )

  (:action assign-v10-false
    :parameters ()
    :precondition (unassigned v10)
    :effect
    (and
      (not (unassigned v10))
      (solved c3)
      (solved c14)
      (solved c19)
      (solved c29)
      (solved c33)
      (solved c36)
      (solved c39)
      (solved c42)
    )
  )

)
