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
      (solved c11)
      (solved c13)
      (solved c30)
      (solved c63)
      (solved c68)
      (solved c69)
      (solved c78)
    )
  )

  (:action assign-v2-true
    :parameters ()
    :precondition (unassigned v2)
    :effect
    (and
      (not (unassigned v2))
      (solved c19)
      (solved c36)
      (solved c48)
      (solved c61)
      (solved c74)
      (solved c107)
    )
  )

  (:action assign-v3-true
    :parameters ()
    :precondition (unassigned v3)
    :effect
    (and
      (not (unassigned v3))
      (solved c5)
      (solved c9)
      (solved c14)
      (solved c22)
      (solved c33)
      (solved c68)
      (solved c71)
      (solved c100)
      (solved c102)
    )
  )

  (:action assign-v4-true
    :parameters ()
    :precondition (unassigned v4)
    :effect
    (and
      (not (unassigned v4))
      (solved c21)
      (solved c28)
      (solved c33)
      (solved c35)
      (solved c53)
      (solved c65)
      (solved c104)
    )
  )

  (:action assign-v5-true
    :parameters ()
    :precondition (unassigned v5)
    :effect
    (and
      (not (unassigned v5))
      (solved c12)
      (solved c29)
      (solved c31)
      (solved c39)
      (solved c40)
      (solved c77)
      (solved c98)
      (solved c103)
    )
  )

  (:action assign-v6-true
    :parameters ()
    :precondition (unassigned v6)
    :effect
    (and
      (not (unassigned v6))
      (solved c5)
      (solved c37)
      (solved c45)
      (solved c60)
      (solved c66)
      (solved c80)
    )
  )

  (:action assign-v7-true
    :parameters ()
    :precondition (unassigned v7)
    :effect
    (and
      (not (unassigned v7))
      (solved c6)
      (solved c30)
      (solved c38)
      (solved c52)
      (solved c68)
      (solved c74)
    )
  )

  (:action assign-v8-true
    :parameters ()
    :precondition (unassigned v8)
    :effect
    (and
      (not (unassigned v8))
      (solved c4)
      (solved c7)
      (solved c16)
      (solved c41)
      (solved c95)
    )
  )

  (:action assign-v9-true
    :parameters ()
    :precondition (unassigned v9)
    :effect
    (and
      (not (unassigned v9))
      (solved c16)
      (solved c61)
      (solved c79)
      (solved c83)
      (solved c91)
    )
  )

  (:action assign-v10-true
    :parameters ()
    :precondition (unassigned v10)
    :effect
    (and
      (not (unassigned v10))
      (solved c1)
      (solved c15)
      (solved c19)
      (solved c25)
      (solved c27)
      (solved c29)
      (solved c43)
      (solved c49)
      (solved c81)
    )
  )

  (:action assign-v11-true
    :parameters ()
    :precondition (unassigned v11)
    :effect
    (and
      (not (unassigned v11))
      (solved c11)
      (solved c42)
      (solved c54)
      (solved c59)
      (solved c67)
      (solved c94)
    )
  )

  (:action assign-v12-true
    :parameters ()
    :precondition (unassigned v12)
    :effect
    (and
      (not (unassigned v12))
      (solved c14)
      (solved c51)
      (solved c52)
      (solved c66)
      (solved c86)
      (solved c101)
    )
  )

  (:action assign-v13-true
    :parameters ()
    :precondition (unassigned v13)
    :effect
    (and
      (not (unassigned v13))
      (solved c0)
      (solved c51)
      (solved c58)
      (solved c64)
    )
  )

  (:action assign-v14-true
    :parameters ()
    :precondition (unassigned v14)
    :effect
    (and
      (not (unassigned v14))
      (solved c15)
      (solved c78)
      (solved c85)
    )
  )

  (:action assign-v15-true
    :parameters ()
    :precondition (unassigned v15)
    :effect
    (and
      (not (unassigned v15))
      (solved c27)
      (solved c57)
      (solved c66)
      (solved c76)
      (solved c107)
    )
  )

  (:action assign-v16-true
    :parameters ()
    :precondition (unassigned v16)
    :effect
    (and
      (not (unassigned v16))
      (solved c37)
      (solved c38)
      (solved c70)
      (solved c99)
    )
  )

  (:action assign-v17-true
    :parameters ()
    :precondition (unassigned v17)
    :effect
    (and
      (not (unassigned v17))
      (solved c2)
      (solved c7)
      (solved c17)
      (solved c20)
      (solved c24)
      (solved c52)
      (solved c53)
      (solved c88)
      (solved c95)
    )
  )

  (:action assign-v18-true
    :parameters ()
    :precondition (unassigned v18)
    :effect
    (and
      (not (unassigned v18))
      (solved c33)
      (solved c34)
      (solved c43)
      (solved c45)
      (solved c63)
      (solved c70)
      (solved c83)
    )
  )

  (:action assign-v19-true
    :parameters ()
    :precondition (unassigned v19)
    :effect
    (and
      (not (unassigned v19))
      (solved c7)
      (solved c20)
      (solved c31)
      (solved c58)
      (solved c61)
      (solved c69)
      (solved c84)
      (solved c97)
    )
  )

  (:action assign-v20-true
    :parameters ()
    :precondition (unassigned v20)
    :effect
    (and
      (not (unassigned v20))
      (solved c3)
      (solved c17)
      (solved c41)
      (solved c93)
      (solved c101)
    )
  )

  (:action assign-v21-true
    :parameters ()
    :precondition (unassigned v21)
    :effect
    (and
      (not (unassigned v21))
      (solved c39)
    )
  )

  (:action assign-v22-true
    :parameters ()
    :precondition (unassigned v22)
    :effect
    (and
      (not (unassigned v22))
      (solved c13)
      (solved c30)
      (solved c44)
      (solved c65)
      (solved c80)
      (solved c91)
      (solved c99)
      (solved c106)
    )
  )

  (:action assign-v23-true
    :parameters ()
    :precondition (unassigned v23)
    :effect
    (and
      (not (unassigned v23))
      (solved c4)
      (solved c23)
      (solved c28)
      (solved c34)
      (solved c98)
    )
  )

  (:action assign-v24-true
    :parameters ()
    :precondition (unassigned v24)
    :effect
    (and
      (not (unassigned v24))
      (solved c14)
      (solved c16)
      (solved c39)
      (solved c43)
      (solved c50)
      (solved c76)
      (solved c89)
      (solved c91)
      (solved c105)
    )
  )

  (:action assign-v25-true
    :parameters ()
    :precondition (unassigned v25)
    :effect
    (and
      (not (unassigned v25))
      (solved c48)
      (solved c59)
      (solved c72)
      (solved c105)
    )
  )

  (:action assign-v1-false
    :parameters ()
    :precondition (unassigned v1)
    :effect
    (and
      (not (unassigned v1))
      (solved c0)
      (solved c50)
      (solved c71)
      (solved c75)
      (solved c90)
      (solved c97)
    )
  )

  (:action assign-v2-false
    :parameters ()
    :precondition (unassigned v2)
    :effect
    (and
      (not (unassigned v2))
      (solved c1)
      (solved c15)
      (solved c32)
      (solved c35)
      (solved c54)
      (solved c65)
      (solved c85)
      (solved c97)
    )
  )

  (:action assign-v3-false
    :parameters ()
    :precondition (unassigned v3)
    :effect
    (and
      (not (unassigned v3))
      (solved c20)
      (solved c57)
      (solved c74)
      (solved c98)
    )
  )

  (:action assign-v4-false
    :parameters ()
    :precondition (unassigned v4)
    :effect
    (and
      (not (unassigned v4))
      (solved c26)
      (solved c32)
      (solved c36)
      (solved c45)
      (solved c47)
      (solved c55)
      (solved c56)
      (solved c92)
      (solved c96)
    )
  )

  (:action assign-v5-false
    :parameters ()
    :precondition (unassigned v5)
    :effect
    (and
      (not (unassigned v5))
      (solved c2)
      (solved c10)
      (solved c36)
      (solved c37)
      (solved c44)
      (solved c73)
      (solved c82)
      (solved c83)
      (solved c88)
      (solved c89)
    )
  )

  (:action assign-v6-false
    :parameters ()
    :precondition (unassigned v6)
    :effect
    (and
      (not (unassigned v6))
      (solved c8)
      (solved c42)
      (solved c49)
      (solved c56)
      (solved c57)
      (solved c77)
      (solved c93)
      (solved c100)
      (solved c103)
      (solved c105)
    )
  )

  (:action assign-v7-false
    :parameters ()
    :precondition (unassigned v7)
    :effect
    (and
      (not (unassigned v7))
      (solved c4)
      (solved c18)
      (solved c28)
      (solved c29)
      (solved c48)
      (solved c80)
      (solved c84)
    )
  )

  (:action assign-v8-false
    :parameters ()
    :precondition (unassigned v8)
    :effect
    (and
      (not (unassigned v8))
      (solved c9)
      (solved c23)
      (solved c40)
      (solved c42)
      (solved c46)
      (solved c55)
      (solved c60)
      (solved c100)
    )
  )

  (:action assign-v9-false
    :parameters ()
    :precondition (unassigned v9)
    :effect
    (and
      (not (unassigned v9))
      (solved c8)
      (solved c10)
      (solved c87)
      (solved c94)
    )
  )

  (:action assign-v10-false
    :parameters ()
    :precondition (unassigned v10)
    :effect
    (and
      (not (unassigned v10))
      (solved c104)
    )
  )

  (:action assign-v11-false
    :parameters ()
    :precondition (unassigned v11)
    :effect
    (and
      (not (unassigned v11))
      (solved c24)
      (solved c73)
      (solved c77)
      (solved c81)
      (solved c90)
      (solved c101)
      (solved c107)
    )
  )

  (:action assign-v12-false
    :parameters ()
    :precondition (unassigned v12)
    :effect
    (and
      (not (unassigned v12))
      (solved c6)
      (solved c12)
      (solved c17)
      (solved c18)
      (solved c76)
      (solved c81)
      (solved c82)
      (solved c96)
    )
  )

  (:action assign-v13-false
    :parameters ()
    :precondition (unassigned v13)
    :effect
    (and
      (not (unassigned v13))
      (solved c21)
      (solved c27)
      (solved c49)
      (solved c59)
      (solved c67)
      (solved c86)
      (solved c104)
    )
  )

  (:action assign-v14-false
    :parameters ()
    :precondition (unassigned v14)
    :effect
    (and
      (not (unassigned v14))
      (solved c31)
      (solved c44)
      (solved c46)
      (solved c47)
      (solved c56)
      (solved c69)
    )
  )

  (:action assign-v15-false
    :parameters ()
    :precondition (unassigned v15)
    :effect
    (and
      (not (unassigned v15))
      (solved c3)
      (solved c11)
      (solved c22)
      (solved c60)
      (solved c67)
      (solved c72)
      (solved c87)
      (solved c92)
      (solved c94)
      (solved c99)
    )
  )

  (:action assign-v16-false
    :parameters ()
    :precondition (unassigned v16)
    :effect
    (and
      (not (unassigned v16))
      (solved c0)
      (solved c5)
      (solved c13)
      (solved c26)
      (solved c41)
      (solved c50)
      (solved c75)
      (solved c79)
      (solved c103)
    )
  )

  (:action assign-v17-false
    :parameters ()
    :precondition (unassigned v17)
    :effect
    (and
      (not (unassigned v17))
      (solved c47)
      (solved c58)
      (solved c78)
    )
  )

  (:action assign-v18-false
    :parameters ()
    :precondition (unassigned v18)
    :effect
    (and
      (not (unassigned v18))
      (solved c3)
      (solved c21)
      (solved c24)
      (solved c53)
      (solved c64)
      (solved c102)
    )
  )

  (:action assign-v19-false
    :parameters ()
    :precondition (unassigned v19)
    :effect
    (and
      (not (unassigned v19))
      (solved c9)
      (solved c19)
      (solved c22)
      (solved c32)
      (solved c82)
      (solved c86)
      (solved c95)
      (solved c106)
    )
  )

  (:action assign-v20-false
    :parameters ()
    :precondition (unassigned v20)
    :effect
    (and
      (not (unassigned v20))
      (solved c25)
      (solved c62)
      (solved c64)
      (solved c92)
      (solved c96)
      (solved c106)
    )
  )

  (:action assign-v21-false
    :parameters ()
    :precondition (unassigned v21)
    :effect
    (and
      (not (unassigned v21))
      (solved c1)
      (solved c62)
      (solved c87)
      (solved c93)
    )
  )

  (:action assign-v22-false
    :parameters ()
    :precondition (unassigned v22)
    :effect
    (and
      (not (unassigned v22))
      (solved c2)
      (solved c8)
      (solved c10)
      (solved c35)
      (solved c40)
      (solved c51)
      (solved c54)
      (solved c73)
      (solved c79)
      (solved c89)
    )
  )

  (:action assign-v23-false
    :parameters ()
    :precondition (unassigned v23)
    :effect
    (and
      (not (unassigned v23))
      (solved c55)
      (solved c72)
      (solved c75)
      (solved c85)
      (solved c90)
    )
  )

  (:action assign-v24-false
    :parameters ()
    :precondition (unassigned v24)
    :effect
    (and
      (not (unassigned v24))
      (solved c6)
      (solved c23)
      (solved c25)
      (solved c26)
      (solved c34)
      (solved c38)
      (solved c46)
      (solved c62)
      (solved c71)
      (solved c84)
      (solved c88)
    )
  )

  (:action assign-v25-false
    :parameters ()
    :precondition (unassigned v25)
    :effect
    (and
      (not (unassigned v25))
      (solved c12)
      (solved c18)
      (solved c63)
      (solved c70)
      (solved c102)
    )
  )

)
