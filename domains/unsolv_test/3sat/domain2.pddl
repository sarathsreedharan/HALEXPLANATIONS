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
      (solved c31)
      (solved c74)
      (solved c86)
    )
  )

  (:action assign-v2-true
    :parameters ()
    :precondition (unassigned v2)
    :effect
    (and
      (not (unassigned v2))
      (solved c4)
      (solved c28)
      (solved c30)
      (solved c36)
      (solved c58)
      (solved c102)
    )
  )

  (:action assign-v3-true
    :parameters ()
    :precondition (unassigned v3)
    :effect
    (and
      (not (unassigned v3))
      (solved c2)
      (solved c11)
      (solved c12)
      (solved c15)
      (solved c34)
      (solved c46)
      (solved c60)
      (solved c93)
    )
  )

  (:action assign-v4-true
    :parameters ()
    :precondition (unassigned v4)
    :effect
    (and
      (not (unassigned v4))
      (solved c5)
      (solved c47)
      (solved c56)
      (solved c102)
    )
  )

  (:action assign-v5-true
    :parameters ()
    :precondition (unassigned v5)
    :effect
    (and
      (not (unassigned v5))
      (solved c13)
      (solved c51)
      (solved c79)
      (solved c103)
    )
  )

  (:action assign-v6-true
    :parameters ()
    :precondition (unassigned v6)
    :effect
    (and
      (not (unassigned v6))
      (solved c12)
      (solved c37)
      (solved c54)
      (solved c58)
      (solved c59)
      (solved c80)
      (solved c95)
      (solved c99)
    )
  )

  (:action assign-v7-true
    :parameters ()
    :precondition (unassigned v7)
    :effect
    (and
      (not (unassigned v7))
      (solved c8)
      (solved c26)
      (solved c34)
      (solved c93)
      (solved c94)
    )
  )

  (:action assign-v8-true
    :parameters ()
    :precondition (unassigned v8)
    :effect
    (and
      (not (unassigned v8))
      (solved c3)
      (solved c11)
      (solved c13)
      (solved c29)
      (solved c38)
      (solved c40)
      (solved c56)
      (solved c63)
      (solved c74)
      (solved c90)
      (solved c101)
    )
  )

  (:action assign-v9-true
    :parameters ()
    :precondition (unassigned v9)
    :effect
    (and
      (not (unassigned v9))
      (solved c3)
      (solved c16)
      (solved c31)
      (solved c45)
      (solved c50)
      (solved c65)
      (solved c92)
      (solved c93)
      (solved c101)
    )
  )

  (:action assign-v10-true
    :parameters ()
    :precondition (unassigned v10)
    :effect
    (and
      (not (unassigned v10))
      (solved c7)
      (solved c15)
      (solved c23)
      (solved c32)
      (solved c36)
      (solved c55)
      (solved c64)
      (solved c65)
      (solved c72)
      (solved c95)
      (solved c97)
      (solved c106)
    )
  )

  (:action assign-v11-true
    :parameters ()
    :precondition (unassigned v11)
    :effect
    (and
      (not (unassigned v11))
      (solved c17)
      (solved c21)
      (solved c38)
      (solved c53)
      (solved c77)
    )
  )

  (:action assign-v12-true
    :parameters ()
    :precondition (unassigned v12)
    :effect
    (and
      (not (unassigned v12))
      (solved c0)
      (solved c20)
      (solved c61)
      (solved c86)
    )
  )

  (:action assign-v13-true
    :parameters ()
    :precondition (unassigned v13)
    :effect
    (and
      (not (unassigned v13))
      (solved c7)
      (solved c10)
      (solved c13)
      (solved c42)
      (solved c70)
    )
  )

  (:action assign-v14-true
    :parameters ()
    :precondition (unassigned v14)
    :effect
    (and
      (not (unassigned v14))
      (solved c16)
      (solved c23)
      (solved c57)
      (solved c63)
      (solved c78)
      (solved c96)
      (solved c101)
    )
  )

  (:action assign-v15-true
    :parameters ()
    :precondition (unassigned v15)
    :effect
    (and
      (not (unassigned v15))
      (solved c55)
      (solved c91)
      (solved c94)
      (solved c98)
    )
  )

  (:action assign-v16-true
    :parameters ()
    :precondition (unassigned v16)
    :effect
    (and
      (not (unassigned v16))
      (solved c18)
      (solved c51)
      (solved c71)
      (solved c100)
    )
  )

  (:action assign-v17-true
    :parameters ()
    :precondition (unassigned v17)
    :effect
    (and
      (not (unassigned v17))
      (solved c0)
      (solved c10)
      (solved c22)
      (solved c40)
      (solved c52)
      (solved c61)
      (solved c66)
      (solved c70)
      (solved c73)
      (solved c74)
      (solved c89)
    )
  )

  (:action assign-v18-true
    :parameters ()
    :precondition (unassigned v18)
    :effect
    (and
      (not (unassigned v18))
      (solved c23)
      (solved c47)
      (solved c50)
      (solved c58)
      (solved c68)
      (solved c80)
      (solved c84)
      (solved c85)
    )
  )

  (:action assign-v19-true
    :parameters ()
    :precondition (unassigned v19)
    :effect
    (and
      (not (unassigned v19))
      (solved c28)
      (solved c37)
      (solved c42)
      (solved c53)
      (solved c70)
    )
  )

  (:action assign-v20-true
    :parameters ()
    :precondition (unassigned v20)
    :effect
    (and
      (not (unassigned v20))
      (solved c18)
      (solved c24)
      (solved c35)
      (solved c36)
      (solved c46)
      (solved c66)
      (solved c81)
      (solved c82)
    )
  )

  (:action assign-v21-true
    :parameters ()
    :precondition (unassigned v21)
    :effect
    (and
      (not (unassigned v21))
      (solved c33)
      (solved c43)
      (solved c59)
      (solved c88)
      (solved c107)
    )
  )

  (:action assign-v22-true
    :parameters ()
    :precondition (unassigned v22)
    :effect
    (and
      (not (unassigned v22))
      (solved c21)
      (solved c39)
      (solved c62)
      (solved c63)
      (solved c75)
      (solved c103)
    )
  )

  (:action assign-v23-true
    :parameters ()
    :precondition (unassigned v23)
    :effect
    (and
      (not (unassigned v23))
      (solved c71)
      (solved c81)
      (solved c85)
      (solved c92)
    )
  )

  (:action assign-v24-true
    :parameters ()
    :precondition (unassigned v24)
    :effect
    (and
      (not (unassigned v24))
      (solved c2)
      (solved c38)
      (solved c47)
      (solved c53)
      (solved c65)
      (solved c73)
      (solved c83)
    )
  )

  (:action assign-v25-true
    :parameters ()
    :precondition (unassigned v25)
    :effect
    (and
      (not (unassigned v25))
      (solved c1)
      (solved c48)
      (solved c51)
      (solved c54)
      (solved c66)
      (solved c79)
      (solved c97)
      (solved c99)
    )
  )

  (:action assign-v1-false
    :parameters ()
    :precondition (unassigned v1)
    :effect
    (and
      (not (unassigned v1))
      (solved c14)
      (solved c22)
      (solved c33)
      (solved c55)
      (solved c75)
      (solved c94)
    )
  )

  (:action assign-v2-false
    :parameters ()
    :precondition (unassigned v2)
    :effect
    (and
      (not (unassigned v2))
      (solved c8)
      (solved c39)
      (solved c48)
      (solved c91)
      (solved c105)
    )
  )

  (:action assign-v3-false
    :parameters ()
    :precondition (unassigned v3)
    :effect
    (and
      (not (unassigned v3))
      (solved c18)
      (solved c19)
      (solved c33)
      (solved c67)
      (solved c100)
    )
  )

  (:action assign-v4-false
    :parameters ()
    :precondition (unassigned v4)
    :effect
    (and
      (not (unassigned v4))
      (solved c4)
      (solved c27)
      (solved c31)
      (solved c32)
      (solved c35)
      (solved c49)
      (solved c57)
      (solved c76)
    )
  )

  (:action assign-v5-false
    :parameters ()
    :precondition (unassigned v5)
    :effect
    (and
      (not (unassigned v5))
      (solved c12)
      (solved c17)
      (solved c27)
      (solved c43)
      (solved c45)
      (solved c68)
      (solved c80)
      (solved c104)
    )
  )

  (:action assign-v6-false
    :parameters ()
    :precondition (unassigned v6)
    :effect
    (and
      (not (unassigned v6))
      (solved c3)
      (solved c14)
      (solved c21)
      (solved c35)
      (solved c42)
      (solved c43)
      (solved c52)
      (solved c62)
      (solved c64)
      (solved c69)
      (solved c78)
      (solved c82)
      (solved c91)
      (solved c96)
      (solved c104)
    )
  )

  (:action assign-v7-false
    :parameters ()
    :precondition (unassigned v7)
    :effect
    (and
      (not (unassigned v7))
      (solved c20)
      (solved c29)
      (solved c44)
      (solved c61)
      (solved c72)
      (solved c84)
    )
  )

  (:action assign-v8-false
    :parameters ()
    :precondition (unassigned v8)
    :effect
    (and
      (not (unassigned v8))
      (solved c2)
      (solved c24)
      (solved c25)
      (solved c54)
      (solved c71)
      (solved c82)
      (solved c89)
      (solved c102)
      (solved c106)
    )
  )

  (:action assign-v9-false
    :parameters ()
    :precondition (unassigned v9)
    :effect
    (and
      (not (unassigned v9))
      (solved c5)
      (solved c9)
      (solved c30)
      (solved c44)
      (solved c89)
    )
  )

  (:action assign-v10-false
    :parameters ()
    :precondition (unassigned v10)
    :effect
    (and
      (not (unassigned v10))
      (solved c69)
      (solved c81)
      (solved c87)
      (solved c98)
      (solved c105)
    )
  )

  (:action assign-v11-false
    :parameters ()
    :precondition (unassigned v11)
    :effect
    (and
      (not (unassigned v11))
      (solved c0)
      (solved c1)
      (solved c7)
      (solved c24)
      (solved c75)
      (solved c78)
      (solved c90)
    )
  )

  (:action assign-v12-false
    :parameters ()
    :precondition (unassigned v12)
    :effect
    (and
      (not (unassigned v12))
      (solved c27)
      (solved c40)
      (solved c44)
      (solved c59)
      (solved c76)
      (solved c85)
      (solved c105)
    )
  )

  (:action assign-v13-false
    :parameters ()
    :precondition (unassigned v13)
    :effect
    (and
      (not (unassigned v13))
      (solved c1)
      (solved c11)
      (solved c39)
      (solved c45)
      (solved c90)
    )
  )

  (:action assign-v14-false
    :parameters ()
    :precondition (unassigned v14)
    :effect
    (and
      (not (unassigned v14))
      (solved c9)
      (solved c19)
      (solved c49)
      (solved c92)
      (solved c97)
    )
  )

  (:action assign-v15-false
    :parameters ()
    :precondition (unassigned v15)
    :effect
    (and
      (not (unassigned v15))
      (solved c19)
      (solved c26)
      (solved c64)
      (solved c76)
      (solved c77)
      (solved c86)
    )
  )

  (:action assign-v16-false
    :parameters ()
    :precondition (unassigned v16)
    :effect
    (and
      (not (unassigned v16))
      (solved c4)
      (solved c6)
      (solved c10)
      (solved c25)
      (solved c28)
      (solved c52)
      (solved c57)
      (solved c88)
      (solved c106)
    )
  )

  (:action assign-v17-false
    :parameters ()
    :precondition (unassigned v17)
    :effect
    (and
      (not (unassigned v17))
      (solved c9)
      (solved c60)
      (solved c62)
      (solved c68)
      (solved c72)
      (solved c98)
    )
  )

  (:action assign-v18-false
    :parameters ()
    :precondition (unassigned v18)
    :effect
    (and
      (not (unassigned v18))
      (solved c6)
      (solved c41)
      (solved c49)
      (solved c79)
    )
  )

  (:action assign-v19-false
    :parameters ()
    :precondition (unassigned v19)
    :effect
    (and
      (not (unassigned v19))
      (solved c8)
      (solved c34)
      (solved c73)
    )
  )

  (:action assign-v20-false
    :parameters ()
    :precondition (unassigned v20)
    :effect
    (and
      (not (unassigned v20))
      (solved c6)
      (solved c29)
      (solved c37)
      (solved c48)
      (solved c83)
      (solved c87)
    )
  )

  (:action assign-v21-false
    :parameters ()
    :precondition (unassigned v21)
    :effect
    (and
      (not (unassigned v21))
      (solved c14)
      (solved c17)
      (solved c41)
      (solved c67)
      (solved c83)
      (solved c96)
      (solved c104)
    )
  )

  (:action assign-v22-false
    :parameters ()
    :precondition (unassigned v22)
    :effect
    (and
      (not (unassigned v22))
      (solved c5)
      (solved c25)
      (solved c26)
      (solved c50)
      (solved c88)
      (solved c107)
    )
  )

  (:action assign-v23-false
    :parameters ()
    :precondition (unassigned v23)
    :effect
    (and
      (not (unassigned v23))
      (solved c15)
      (solved c46)
      (solved c60)
      (solved c67)
      (solved c69)
      (solved c84)
      (solved c100)
      (solved c103)
      (solved c107)
    )
  )

  (:action assign-v24-false
    :parameters ()
    :precondition (unassigned v24)
    :effect
    (and
      (not (unassigned v24))
      (solved c16)
      (solved c22)
      (solved c56)
      (solved c87)
      (solved c99)
    )
  )

  (:action assign-v25-false
    :parameters ()
    :precondition (unassigned v25)
    :effect
    (and
      (not (unassigned v25))
      (solved c20)
      (solved c30)
      (solved c32)
      (solved c41)
      (solved c77)
      (solved c95)
    )
  )

)
