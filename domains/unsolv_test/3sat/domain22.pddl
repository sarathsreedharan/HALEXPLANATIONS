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
      (solved c9)
      (solved c12)
      (solved c22)
      (solved c31)
      (solved c32)
      (solved c54)
      (solved c60)
    )
  )

  (:action assign-v2-true
    :parameters ()
    :precondition (unassigned v2)
    :effect
    (and
      (not (unassigned v2))
      (solved c14)
      (solved c19)
      (solved c21)
      (solved c26)
      (solved c38)
    )
  )

  (:action assign-v3-true
    :parameters ()
    :precondition (unassigned v3)
    :effect
    (and
      (not (unassigned v3))
      (solved c0)
      (solved c13)
      (solved c27)
      (solved c29)
      (solved c37)
      (solved c39)
      (solved c44)
      (solved c48)
      (solved c53)
      (solved c59)
      (solved c62)
    )
  )

  (:action assign-v4-true
    :parameters ()
    :precondition (unassigned v4)
    :effect
    (and
      (not (unassigned v4))
      (solved c11)
      (solved c24)
      (solved c25)
    )
  )

  (:action assign-v5-true
    :parameters ()
    :precondition (unassigned v5)
    :effect
    (and
      (not (unassigned v5))
      (solved c2)
      (solved c7)
      (solved c21)
      (solved c23)
      (solved c28)
      (solved c30)
      (solved c39)
      (solved c62)
    )
  )

  (:action assign-v6-true
    :parameters ()
    :precondition (unassigned v6)
    :effect
    (and
      (not (unassigned v6))
      (solved c1)
      (solved c5)
      (solved c28)
      (solved c30)
      (solved c32)
      (solved c46)
      (solved c47)
      (solved c53)
      (solved c59)
      (solved c64)
    )
  )

  (:action assign-v7-true
    :parameters ()
    :precondition (unassigned v7)
    :effect
    (and
      (not (unassigned v7))
      (solved c6)
      (solved c8)
      (solved c9)
      (solved c11)
      (solved c32)
      (solved c36)
      (solved c45)
      (solved c60)
      (solved c61)
    )
  )

  (:action assign-v8-true
    :parameters ()
    :precondition (unassigned v8)
    :effect
    (and
      (not (unassigned v8))
      (solved c3)
      (solved c4)
      (solved c7)
      (solved c21)
      (solved c27)
      (solved c34)
      (solved c56)
    )
  )

  (:action assign-v9-true
    :parameters ()
    :precondition (unassigned v9)
    :effect
    (and
      (not (unassigned v9))
      (solved c1)
      (solved c8)
      (solved c20)
      (solved c35)
      (solved c39)
      (solved c61)
      (solved c63)
    )
  )

  (:action assign-v10-true
    :parameters ()
    :precondition (unassigned v10)
    :effect
    (and
      (not (unassigned v10))
      (solved c6)
      (solved c25)
      (solved c31)
      (solved c57)
      (solved c60)
    )
  )

  (:action assign-v11-true
    :parameters ()
    :precondition (unassigned v11)
    :effect
    (and
      (not (unassigned v11))
      (solved c0)
      (solved c3)
      (solved c6)
      (solved c12)
      (solved c18)
      (solved c25)
      (solved c37)
      (solved c49)
      (solved c62)
    )
  )

  (:action assign-v12-true
    :parameters ()
    :precondition (unassigned v12)
    :effect
    (and
      (not (unassigned v12))
      (solved c33)
      (solved c37)
      (solved c50)
      (solved c54)
      (solved c57)
      (solved c58)
    )
  )

  (:action assign-v13-true
    :parameters ()
    :precondition (unassigned v13)
    :effect
    (and
      (not (unassigned v13))
      (solved c2)
      (solved c49)
      (solved c64)
    )
  )

  (:action assign-v14-true
    :parameters ()
    :precondition (unassigned v14)
    :effect
    (and
      (not (unassigned v14))
      (solved c29)
      (solved c42)
      (solved c46)
      (solved c50)
      (solved c61)
    )
  )

  (:action assign-v15-true
    :parameters ()
    :precondition (unassigned v15)
    :effect
    (and
      (not (unassigned v15))
      (solved c0)
      (solved c7)
      (solved c11)
      (solved c23)
      (solved c28)
      (solved c33)
      (solved c64)
    )
  )

  (:action assign-v1-false
    :parameters ()
    :precondition (unassigned v1)
    :effect
    (and
      (not (unassigned v1))
      (solved c1)
      (solved c10)
      (solved c17)
      (solved c24)
      (solved c26)
      (solved c43)
      (solved c52)
    )
  )

  (:action assign-v2-false
    :parameters ()
    :precondition (unassigned v2)
    :effect
    (and
      (not (unassigned v2))
      (solved c23)
      (solved c34)
    )
  )

  (:action assign-v3-false
    :parameters ()
    :precondition (unassigned v3)
    :effect
    (and
      (not (unassigned v3))
      (solved c4)
      (solved c12)
      (solved c15)
      (solved c36)
      (solved c47)
    )
  )

  (:action assign-v4-false
    :parameters ()
    :precondition (unassigned v4)
    :effect
    (and
      (not (unassigned v4))
      (solved c5)
      (solved c8)
      (solved c30)
      (solved c40)
      (solved c41)
      (solved c45)
      (solved c47)
      (solved c51)
      (solved c52)
    )
  )

  (:action assign-v5-false
    :parameters ()
    :precondition (unassigned v5)
    :effect
    (and
      (not (unassigned v5))
      (solved c17)
      (solved c19)
      (solved c24)
      (solved c36)
      (solved c40)
      (solved c43)
      (solved c44)
      (solved c54)
      (solved c56)
    )
  )

  (:action assign-v6-false
    :parameters ()
    :precondition (unassigned v6)
    :effect
    (and
      (not (unassigned v6))
      (solved c9)
      (solved c14)
      (solved c31)
      (solved c33)
      (solved c50)
      (solved c58)
    )
  )

  (:action assign-v7-false
    :parameters ()
    :precondition (unassigned v7)
    :effect
    (and
      (not (unassigned v7))
      (solved c10)
      (solved c22)
      (solved c35)
      (solved c38)
      (solved c41)
      (solved c51)
    )
  )

  (:action assign-v8-false
    :parameters ()
    :precondition (unassigned v8)
    :effect
    (and
      (not (unassigned v8))
      (solved c2)
      (solved c16)
      (solved c42)
      (solved c49)
      (solved c51)
    )
  )

  (:action assign-v9-false
    :parameters ()
    :precondition (unassigned v9)
    :effect
    (and
      (not (unassigned v9))
      (solved c13)
      (solved c14)
      (solved c15)
      (solved c17)
      (solved c19)
      (solved c22)
      (solved c29)
      (solved c44)
      (solved c45)
      (solved c48)
      (solved c53)
    )
  )

  (:action assign-v10-false
    :parameters ()
    :precondition (unassigned v10)
    :effect
    (and
      (not (unassigned v10))
      (solved c5)
      (solved c20)
      (solved c41)
      (solved c43)
      (solved c48)
      (solved c55)
      (solved c56)
      (solved c58)
    )
  )

  (:action assign-v11-false
    :parameters ()
    :precondition (unassigned v11)
    :effect
    (and
      (not (unassigned v11))
      (solved c10)
      (solved c63)
    )
  )

  (:action assign-v12-false
    :parameters ()
    :precondition (unassigned v12)
    :effect
    (and
      (not (unassigned v12))
      (solved c3)
      (solved c26)
      (solved c35)
      (solved c63)
    )
  )

  (:action assign-v13-false
    :parameters ()
    :precondition (unassigned v13)
    :effect
    (and
      (not (unassigned v13))
      (solved c15)
      (solved c18)
      (solved c27)
      (solved c38)
      (solved c46)
      (solved c57)
    )
  )

  (:action assign-v14-false
    :parameters ()
    :precondition (unassigned v14)
    :effect
    (and
      (not (unassigned v14))
      (solved c4)
      (solved c16)
      (solved c20)
      (solved c55)
    )
  )

  (:action assign-v15-false
    :parameters ()
    :precondition (unassigned v15)
    :effect
    (and
      (not (unassigned v15))
      (solved c13)
      (solved c16)
      (solved c18)
      (solved c34)
      (solved c40)
      (solved c42)
      (solved c52)
      (solved c55)
      (solved c59)
    )
  )

)
