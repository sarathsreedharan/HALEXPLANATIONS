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
      (solved c12)
      (solved c17)
      (solved c21)
      (solved c39)
      (solved c48)
      (solved c55)
      (solved c61)
      (solved c74)
      (solved c80)
      (solved c81)
    )
  )

  (:action assign-v2-true
    :parameters ()
    :precondition (unassigned v2)
    :effect
    (and
      (not (unassigned v2))
      (solved c28)
      (solved c37)
      (solved c45)
      (solved c46)
      (solved c61)
      (solved c63)
      (solved c80)
    )
  )

  (:action assign-v3-true
    :parameters ()
    :precondition (unassigned v3)
    :effect
    (and
      (not (unassigned v3))
      (solved c6)
      (solved c9)
      (solved c34)
      (solved c44)
    )
  )

  (:action assign-v4-true
    :parameters ()
    :precondition (unassigned v4)
    :effect
    (and
      (not (unassigned v4))
      (solved c28)
      (solved c42)
      (solved c43)
      (solved c45)
      (solved c54)
      (solved c65)
    )
  )

  (:action assign-v5-true
    :parameters ()
    :precondition (unassigned v5)
    :effect
    (and
      (not (unassigned v5))
      (solved c0)
      (solved c18)
      (solved c28)
      (solved c43)
      (solved c73)
      (solved c82)
    )
  )

  (:action assign-v6-true
    :parameters ()
    :precondition (unassigned v6)
    :effect
    (and
      (not (unassigned v6))
      (solved c2)
      (solved c5)
      (solved c15)
      (solved c26)
      (solved c29)
      (solved c67)
      (solved c73)
      (solved c84)
    )
  )

  (:action assign-v7-true
    :parameters ()
    :precondition (unassigned v7)
    :effect
    (and
      (not (unassigned v7))
      (solved c1)
      (solved c15)
      (solved c16)
      (solved c19)
      (solved c57)
      (solved c59)
      (solved c63)
      (solved c64)
      (solved c65)
      (solved c68)
      (solved c85)
    )
  )

  (:action assign-v8-true
    :parameters ()
    :precondition (unassigned v8)
    :effect
    (and
      (not (unassigned v8))
      (solved c35)
      (solved c43)
      (solved c76)
      (solved c83)
    )
  )

  (:action assign-v9-true
    :parameters ()
    :precondition (unassigned v9)
    :effect
    (and
      (not (unassigned v9))
      (solved c24)
      (solved c40)
      (solved c66)
      (solved c81)
    )
  )

  (:action assign-v10-true
    :parameters ()
    :precondition (unassigned v10)
    :effect
    (and
      (not (unassigned v10))
      (solved c5)
      (solved c14)
      (solved c25)
      (solved c38)
      (solved c49)
      (solved c62)
      (solved c71)
    )
  )

  (:action assign-v11-true
    :parameters ()
    :precondition (unassigned v11)
    :effect
    (and
      (not (unassigned v11))
      (solved c18)
      (solved c31)
      (solved c41)
      (solved c54)
      (solved c71)
      (solved c85)
    )
  )

  (:action assign-v12-true
    :parameters ()
    :precondition (unassigned v12)
    :effect
    (and
      (not (unassigned v12))
      (solved c9)
      (solved c16)
      (solved c37)
      (solved c40)
      (solved c46)
      (solved c49)
      (solved c58)
    )
  )

  (:action assign-v13-true
    :parameters ()
    :precondition (unassigned v13)
    :effect
    (and
      (not (unassigned v13))
      (solved c6)
      (solved c19)
      (solved c23)
      (solved c39)
      (solved c47)
      (solved c79)
    )
  )

  (:action assign-v14-true
    :parameters ()
    :precondition (unassigned v14)
    :effect
    (and
      (not (unassigned v14))
      (solved c22)
      (solved c24)
      (solved c35)
      (solved c47)
      (solved c54)
      (solved c60)
      (solved c75)
      (solved c78)
    )
  )

  (:action assign-v15-true
    :parameters ()
    :precondition (unassigned v15)
    :effect
    (and
      (not (unassigned v15))
      (solved c4)
      (solved c29)
      (solved c31)
      (solved c68)
      (solved c70)
      (solved c75)
    )
  )

  (:action assign-v16-true
    :parameters ()
    :precondition (unassigned v16)
    :effect
    (and
      (not (unassigned v16))
      (solved c27)
      (solved c50)
      (solved c55)
      (solved c58)
    )
  )

  (:action assign-v17-true
    :parameters ()
    :precondition (unassigned v17)
    :effect
    (and
      (not (unassigned v17))
      (solved c2)
      (solved c5)
      (solved c9)
      (solved c42)
      (solved c75)
      (solved c76)
    )
  )

  (:action assign-v18-true
    :parameters ()
    :precondition (unassigned v18)
    :effect
    (and
      (not (unassigned v18))
      (solved c40)
      (solved c50)
      (solved c52)
      (solved c74)
      (solved c76)
    )
  )

  (:action assign-v19-true
    :parameters ()
    :precondition (unassigned v19)
    :effect
    (and
      (not (unassigned v19))
      (solved c10)
      (solved c30)
      (solved c44)
      (solved c60)
      (solved c84)
    )
  )

  (:action assign-v20-true
    :parameters ()
    :precondition (unassigned v20)
    :effect
    (and
      (not (unassigned v20))
      (solved c14)
      (solved c18)
      (solved c34)
      (solved c41)
      (solved c44)
      (solved c56)
      (solved c61)
      (solved c72)
      (solved c73)
    )
  )

  (:action assign-v1-false
    :parameters ()
    :precondition (unassigned v1)
    :effect
    (and
      (not (unassigned v1))
      (solved c22)
      (solved c23)
      (solved c24)
      (solved c27)
      (solved c31)
      (solved c68)
    )
  )

  (:action assign-v2-false
    :parameters ()
    :precondition (unassigned v2)
    :effect
    (and
      (not (unassigned v2))
      (solved c17)
      (solved c23)
      (solved c25)
      (solved c38)
      (solved c39)
      (solved c52)
      (solved c78)
      (solved c79)
      (solved c82)
    )
  )

  (:action assign-v3-false
    :parameters ()
    :precondition (unassigned v3)
    :effect
    (and
      (not (unassigned v3))
      (solved c1)
      (solved c14)
      (solved c17)
      (solved c22)
      (solved c26)
      (solved c27)
      (solved c48)
      (solved c53)
      (solved c77)
      (solved c80)
    )
  )

  (:action assign-v4-false
    :parameters ()
    :precondition (unassigned v4)
    :effect
    (and
      (not (unassigned v4))
      (solved c51)
      (solved c57)
      (solved c69)
      (solved c77)
    )
  )

  (:action assign-v5-false
    :parameters ()
    :precondition (unassigned v5)
    :effect
    (and
      (not (unassigned v5))
      (solved c3)
      (solved c8)
      (solved c11)
      (solved c62)
      (solved c84)
    )
  )

  (:action assign-v6-false
    :parameters ()
    :precondition (unassigned v6)
    :effect
    (and
      (not (unassigned v6))
      (solved c51)
      (solved c56)
      (solved c70)
    )
  )

  (:action assign-v7-false
    :parameters ()
    :precondition (unassigned v7)
    :effect
    (and
      (not (unassigned v7))
      (solved c11)
      (solved c30)
      (solved c34)
      (solved c45)
      (solved c53)
      (solved c71)
    )
  )

  (:action assign-v8-false
    :parameters ()
    :precondition (unassigned v8)
    :effect
    (and
      (not (unassigned v8))
      (solved c29)
      (solved c32)
      (solved c46)
      (solved c52)
      (solved c55)
    )
  )

  (:action assign-v9-false
    :parameters ()
    :precondition (unassigned v9)
    :effect
    (and
      (not (unassigned v9))
      (solved c0)
      (solved c3)
      (solved c12)
      (solved c16)
      (solved c20)
      (solved c36)
      (solved c42)
      (solved c49)
      (solved c53)
      (solved c74)
    )
  )

  (:action assign-v10-false
    :parameters ()
    :precondition (unassigned v10)
    :effect
    (and
      (not (unassigned v10))
      (solved c6)
      (solved c11)
      (solved c79)
      (solved c85)
    )
  )

  (:action assign-v11-false
    :parameters ()
    :precondition (unassigned v11)
    :effect
    (and
      (not (unassigned v11))
      (solved c7)
      (solved c8)
      (solved c36)
      (solved c56)
      (solved c57)
      (solved c65)
      (solved c69)
      (solved c78)
      (solved c83)
    )
  )

  (:action assign-v12-false
    :parameters ()
    :precondition (unassigned v12)
    :effect
    (and
      (not (unassigned v12))
      (solved c2)
      (solved c13)
      (solved c33)
      (solved c50)
    )
  )

  (:action assign-v13-false
    :parameters ()
    :precondition (unassigned v13)
    :effect
    (and
      (not (unassigned v13))
      (solved c8)
      (solved c10)
      (solved c12)
      (solved c30)
      (solved c33)
      (solved c59)
      (solved c66)
      (solved c72)
    )
  )

  (:action assign-v14-false
    :parameters ()
    :precondition (unassigned v14)
    :effect
    (and
      (not (unassigned v14))
      (solved c4)
      (solved c13)
      (solved c25)
      (solved c26)
      (solved c70)
    )
  )

  (:action assign-v15-false
    :parameters ()
    :precondition (unassigned v15)
    :effect
    (and
      (not (unassigned v15))
      (solved c3)
      (solved c10)
      (solved c20)
      (solved c32)
      (solved c33)
      (solved c35)
      (solved c41)
      (solved c62)
      (solved c64)
      (solved c67)
      (solved c69)
      (solved c72)
      (solved c83)
    )
  )

  (:action assign-v16-false
    :parameters ()
    :precondition (unassigned v16)
    :effect
    (and
      (not (unassigned v16))
      (solved c15)
      (solved c20)
      (solved c21)
      (solved c59)
    )
  )

  (:action assign-v17-false
    :parameters ()
    :precondition (unassigned v17)
    :effect
    (and
      (not (unassigned v17))
      (solved c4)
      (solved c13)
      (solved c37)
      (solved c38)
      (solved c48)
      (solved c60)
    )
  )

  (:action assign-v18-false
    :parameters ()
    :precondition (unassigned v18)
    :effect
    (and
      (not (unassigned v18))
      (solved c7)
      (solved c47)
      (solved c51)
      (solved c58)
    )
  )

  (:action assign-v19-false
    :parameters ()
    :precondition (unassigned v19)
    :effect
    (and
      (not (unassigned v19))
      (solved c1)
      (solved c7)
      (solved c36)
      (solved c63)
      (solved c67)
      (solved c81)
      (solved c82)
    )
  )

  (:action assign-v20-false
    :parameters ()
    :precondition (unassigned v20)
    :effect
    (and
      (not (unassigned v20))
      (solved c0)
      (solved c19)
      (solved c21)
      (solved c32)
      (solved c64)
      (solved c66)
      (solved c77)
    )
  )

)
