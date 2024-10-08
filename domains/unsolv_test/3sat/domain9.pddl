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
      (solved c18)
      (solved c32)
      (solved c41)
      (solved c106)
      (solved c122)
      (solved c123)
    )
  )

  (:action assign-v2-true
    :parameters ()
    :precondition (unassigned v2)
    :effect
    (and
      (not (unassigned v2))
      (solved c17)
      (solved c30)
      (solved c35)
    )
  )

  (:action assign-v3-true
    :parameters ()
    :precondition (unassigned v3)
    :effect
    (and
      (not (unassigned v3))
      (solved c18)
      (solved c21)
      (solved c31)
      (solved c53)
      (solved c119)
    )
  )

  (:action assign-v4-true
    :parameters ()
    :precondition (unassigned v4)
    :effect
    (and
      (not (unassigned v4))
      (solved c73)
      (solved c74)
      (solved c75)
      (solved c100)
      (solved c105)
      (solved c114)
      (solved c116)
    )
  )

  (:action assign-v5-true
    :parameters ()
    :precondition (unassigned v5)
    :effect
    (and
      (not (unassigned v5))
      (solved c29)
      (solved c38)
      (solved c62)
      (solved c68)
      (solved c87)
      (solved c93)
    )
  )

  (:action assign-v6-true
    :parameters ()
    :precondition (unassigned v6)
    :effect
    (and
      (not (unassigned v6))
      (solved c12)
      (solved c28)
      (solved c37)
      (solved c44)
      (solved c69)
      (solved c72)
      (solved c76)
      (solved c110)
      (solved c128)
    )
  )

  (:action assign-v7-true
    :parameters ()
    :precondition (unassigned v7)
    :effect
    (and
      (not (unassigned v7))
      (solved c3)
      (solved c6)
      (solved c15)
      (solved c27)
      (solved c33)
      (solved c71)
      (solved c73)
      (solved c85)
      (solved c112)
      (solved c118)
      (solved c121)
      (solved c126)
    )
  )

  (:action assign-v8-true
    :parameters ()
    :precondition (unassigned v8)
    :effect
    (and
      (not (unassigned v8))
      (solved c26)
      (solved c27)
      (solved c49)
      (solved c55)
      (solved c100)
      (solved c113)
      (solved c120)
    )
  )

  (:action assign-v9-true
    :parameters ()
    :precondition (unassigned v9)
    :effect
    (and
      (not (unassigned v9))
      (solved c11)
      (solved c22)
      (solved c60)
      (solved c114)
    )
  )

  (:action assign-v10-true
    :parameters ()
    :precondition (unassigned v10)
    :effect
    (and
      (not (unassigned v10))
      (solved c0)
      (solved c32)
      (solved c55)
      (solved c78)
      (solved c107)
    )
  )

  (:action assign-v11-true
    :parameters ()
    :precondition (unassigned v11)
    :effect
    (and
      (not (unassigned v11))
      (solved c2)
      (solved c3)
      (solved c44)
      (solved c67)
      (solved c68)
      (solved c80)
      (solved c83)
      (solved c113)
      (solved c123)
      (solved c124)
    )
  )

  (:action assign-v12-true
    :parameters ()
    :precondition (unassigned v12)
    :effect
    (and
      (not (unassigned v12))
      (solved c2)
      (solved c4)
      (solved c71)
      (solved c109)
      (solved c118)
      (solved c125)
    )
  )

  (:action assign-v13-true
    :parameters ()
    :precondition (unassigned v13)
    :effect
    (and
      (not (unassigned v13))
      (solved c25)
      (solved c93)
      (solved c96)
    )
  )

  (:action assign-v14-true
    :parameters ()
    :precondition (unassigned v14)
    :effect
    (and
      (not (unassigned v14))
      (solved c25)
      (solved c43)
      (solved c45)
      (solved c65)
      (solved c79)
      (solved c83)
      (solved c109)
      (solved c122)
    )
  )

  (:action assign-v15-true
    :parameters ()
    :precondition (unassigned v15)
    :effect
    (and
      (not (unassigned v15))
      (solved c38)
      (solved c39)
      (solved c107)
    )
  )

  (:action assign-v16-true
    :parameters ()
    :precondition (unassigned v16)
    :effect
    (and
      (not (unassigned v16))
      (solved c1)
      (solved c5)
      (solved c30)
      (solved c33)
      (solved c66)
      (solved c76)
      (solved c80)
      (solved c85)
    )
  )

  (:action assign-v17-true
    :parameters ()
    :precondition (unassigned v17)
    :effect
    (and
      (not (unassigned v17))
      (solved c92)
      (solved c100)
      (solved c112)
      (solved c118)
    )
  )

  (:action assign-v18-true
    :parameters ()
    :precondition (unassigned v18)
    :effect
    (and
      (not (unassigned v18))
      (solved c10)
      (solved c80)
      (solved c87)
      (solved c106)
    )
  )

  (:action assign-v19-true
    :parameters ()
    :precondition (unassigned v19)
    :effect
    (and
      (not (unassigned v19))
      (solved c5)
      (solved c57)
      (solved c60)
      (solved c104)
      (solved c108)
      (solved c123)
    )
  )

  (:action assign-v20-true
    :parameters ()
    :precondition (unassigned v20)
    :effect
    (and
      (not (unassigned v20))
      (solved c3)
      (solved c8)
      (solved c26)
      (solved c34)
      (solved c56)
      (solved c62)
      (solved c72)
      (solved c101)
    )
  )

  (:action assign-v21-true
    :parameters ()
    :precondition (unassigned v21)
    :effect
    (and
      (not (unassigned v21))
      (solved c14)
      (solved c27)
      (solved c28)
      (solved c111)
    )
  )

  (:action assign-v22-true
    :parameters ()
    :precondition (unassigned v22)
    :effect
    (and
      (not (unassigned v22))
      (solved c34)
      (solved c43)
      (solved c45)
      (solved c48)
      (solved c116)
    )
  )

  (:action assign-v23-true
    :parameters ()
    :precondition (unassigned v23)
    :effect
    (and
      (not (unassigned v23))
      (solved c52)
      (solved c54)
      (solved c75)
      (solved c78)
      (solved c84)
      (solved c85)
      (solved c86)
      (solved c99)
    )
  )

  (:action assign-v24-true
    :parameters ()
    :precondition (unassigned v24)
    :effect
    (and
      (not (unassigned v24))
      (solved c5)
      (solved c42)
      (solved c91)
      (solved c97)
      (solved c99)
      (solved c110)
    )
  )

  (:action assign-v25-true
    :parameters ()
    :precondition (unassigned v25)
    :effect
    (and
      (not (unassigned v25))
      (solved c16)
      (solved c37)
      (solved c56)
      (solved c86)
      (solved c90)
      (solved c96)
      (solved c98)
      (solved c117)
    )
  )

  (:action assign-v26-true
    :parameters ()
    :precondition (unassigned v26)
    :effect
    (and
      (not (unassigned v26))
      (solved c46)
    )
  )

  (:action assign-v27-true
    :parameters ()
    :precondition (unassigned v27)
    :effect
    (and
      (not (unassigned v27))
      (solved c7)
      (solved c65)
      (solved c73)
      (solved c88)
      (solved c89)
      (solved c124)
    )
  )

  (:action assign-v28-true
    :parameters ()
    :precondition (unassigned v28)
    :effect
    (and
      (not (unassigned v28))
      (solved c17)
      (solved c45)
      (solved c46)
      (solved c74)
      (solved c83)
      (solved c88)
      (solved c92)
      (solved c108)
      (solved c122)
    )
  )

  (:action assign-v29-true
    :parameters ()
    :precondition (unassigned v29)
    :effect
    (and
      (not (unassigned v29))
      (solved c0)
      (solved c2)
      (solved c22)
      (solved c59)
      (solved c98)
    )
  )

  (:action assign-v30-true
    :parameters ()
    :precondition (unassigned v30)
    :effect
    (and
      (not (unassigned v30))
      (solved c9)
      (solved c19)
      (solved c23)
      (solved c25)
      (solved c31)
      (solved c39)
      (solved c75)
      (solved c104)
      (solved c112)
    )
  )

  (:action assign-v1-false
    :parameters ()
    :precondition (unassigned v1)
    :effect
    (and
      (not (unassigned v1))
      (solved c13)
      (solved c30)
      (solved c55)
      (solved c64)
      (solved c92)
      (solved c99)
      (solved c117)
    )
  )

  (:action assign-v2-false
    :parameters ()
    :precondition (unassigned v2)
    :effect
    (and
      (not (unassigned v2))
      (solved c7)
      (solved c50)
      (solved c116)
      (solved c119)
    )
  )

  (:action assign-v3-false
    :parameters ()
    :precondition (unassigned v3)
    :effect
    (and
      (not (unassigned v3))
      (solved c7)
      (solved c12)
      (solved c40)
      (solved c57)
      (solved c67)
      (solved c89)
    )
  )

  (:action assign-v4-false
    :parameters ()
    :precondition (unassigned v4)
    :effect
    (and
      (not (unassigned v4))
      (solved c8)
      (solved c35)
      (solved c47)
      (solved c66)
      (solved c77)
      (solved c86)
    )
  )

  (:action assign-v5-false
    :parameters ()
    :precondition (unassigned v5)
    :effect
    (and
      (not (unassigned v5))
      (solved c4)
      (solved c9)
      (solved c24)
      (solved c90)
      (solved c98)
      (solved c101)
      (solved c126)
    )
  )

  (:action assign-v6-false
    :parameters ()
    :precondition (unassigned v6)
    :effect
    (and
      (not (unassigned v6))
      (solved c15)
      (solved c16)
      (solved c24)
      (solved c29)
      (solved c42)
      (solved c68)
      (solved c79)
      (solved c94)
      (solved c107)
      (solved c119)
    )
  )

  (:action assign-v7-false
    :parameters ()
    :precondition (unassigned v7)
    :effect
    (and
      (not (unassigned v7))
      (solved c37)
      (solved c40)
      (solved c52)
      (solved c54)
      (solved c58)
      (solved c60)
      (solved c77)
      (solved c84)
    )
  )

  (:action assign-v8-false
    :parameters ()
    :precondition (unassigned v8)
    :effect
    (and
      (not (unassigned v8))
      (solved c4)
      (solved c24)
      (solved c35)
      (solved c51)
      (solved c109)
      (solved c114)
    )
  )

  (:action assign-v9-false
    :parameters ()
    :precondition (unassigned v9)
    :effect
    (and
      (not (unassigned v9))
      (solved c12)
      (solved c32)
      (solved c39)
      (solved c51)
      (solved c56)
      (solved c58)
      (solved c61)
      (solved c82)
      (solved c105)
      (solved c125)
    )
  )

  (:action assign-v10-false
    :parameters ()
    :precondition (unassigned v10)
    :effect
    (and
      (not (unassigned v10))
      (solved c10)
      (solved c19)
      (solved c50)
      (solved c65)
      (solved c69)
      (solved c91)
      (solved c97)
      (solved c101)
      (solved c103)
    )
  )

  (:action assign-v11-false
    :parameters ()
    :precondition (unassigned v11)
    :effect
    (and
      (not (unassigned v11))
      (solved c10)
      (solved c11)
      (solved c14)
      (solved c18)
      (solved c53)
      (solved c58)
      (solved c59)
      (solved c61)
      (solved c76)
    )
  )

  (:action assign-v12-false
    :parameters ()
    :precondition (unassigned v12)
    :effect
    (and
      (not (unassigned v12))
      (solved c0)
      (solved c8)
      (solved c34)
      (solved c79)
      (solved c127)
    )
  )

  (:action assign-v13-false
    :parameters ()
    :precondition (unassigned v13)
    :effect
    (and
      (not (unassigned v13))
      (solved c17)
      (solved c48)
      (solved c66)
      (solved c71)
      (solved c87)
      (solved c104)
      (solved c125)
    )
  )

  (:action assign-v14-false
    :parameters ()
    :precondition (unassigned v14)
    :effect
    (and
      (not (unassigned v14))
      (solved c1)
      (solved c28)
      (solved c33)
      (solved c44)
      (solved c46)
      (solved c53)
      (solved c81)
      (solved c94)
    )
  )

  (:action assign-v15-false
    :parameters ()
    :precondition (unassigned v15)
    :effect
    (and
      (not (unassigned v15))
      (solved c20)
      (solved c36)
      (solved c50)
      (solved c69)
    )
  )

  (:action assign-v16-false
    :parameters ()
    :precondition (unassigned v16)
    :effect
    (and
      (not (unassigned v16))
      (solved c26)
      (solved c41)
      (solved c63)
      (solved c115)
      (solved c124)
    )
  )

  (:action assign-v17-false
    :parameters ()
    :precondition (unassigned v17)
    :effect
    (and
      (not (unassigned v17))
      (solved c1)
      (solved c36)
      (solved c74)
      (solved c105)
    )
  )

  (:action assign-v18-false
    :parameters ()
    :precondition (unassigned v18)
    :effect
    (and
      (not (unassigned v18))
      (solved c23)
      (solved c36)
      (solved c40)
      (solved c47)
      (solved c70)
      (solved c108)
      (solved c128)
    )
  )

  (:action assign-v19-false
    :parameters ()
    :precondition (unassigned v19)
    :effect
    (and
      (not (unassigned v19))
      (solved c13)
      (solved c41)
      (solved c49)
      (solved c54)
      (solved c59)
      (solved c63)
      (solved c95)
      (solved c111)
    )
  )

  (:action assign-v20-false
    :parameters ()
    :precondition (unassigned v20)
    :effect
    (and
      (not (unassigned v20))
      (solved c23)
      (solved c42)
      (solved c57)
      (solved c64)
      (solved c84)
      (solved c95)
      (solved c110)
      (solved c115)
      (solved c120)
      (solved c121)
      (solved c127)
    )
  )

  (:action assign-v21-false
    :parameters ()
    :precondition (unassigned v21)
    :effect
    (and
      (not (unassigned v21))
      (solved c6)
      (solved c21)
      (solved c72)
      (solved c81)
      (solved c94)
      (solved c102)
      (solved c120)
      (solved c126)
    )
  )

  (:action assign-v22-false
    :parameters ()
    :precondition (unassigned v22)
    :effect
    (and
      (not (unassigned v22))
      (solved c13)
      (solved c20)
      (solved c49)
      (solved c90)
      (solved c115)
      (solved c127)
    )
  )

  (:action assign-v23-false
    :parameters ()
    :precondition (unassigned v23)
    :effect
    (and
      (not (unassigned v23))
      (solved c6)
      (solved c62)
      (solved c70)
      (solved c106)
      (solved c111)
      (solved c113)
    )
  )

  (:action assign-v24-false
    :parameters ()
    :precondition (unassigned v24)
    :effect
    (and
      (not (unassigned v24))
      (solved c88)
    )
  )

  (:action assign-v25-false
    :parameters ()
    :precondition (unassigned v25)
    :effect
    (and
      (not (unassigned v25))
      (solved c29)
      (solved c61)
      (solved c82)
      (solved c89)
      (solved c102)
    )
  )

  (:action assign-v26-false
    :parameters ()
    :precondition (unassigned v26)
    :effect
    (and
      (not (unassigned v26))
      (solved c14)
      (solved c19)
      (solved c47)
      (solved c117)
      (solved c128)
    )
  )

  (:action assign-v27-false
    :parameters ()
    :precondition (unassigned v27)
    :effect
    (and
      (not (unassigned v27))
      (solved c15)
      (solved c16)
      (solved c21)
      (solved c22)
      (solved c38)
      (solved c48)
      (solved c63)
      (solved c77)
      (solved c81)
      (solved c103)
      (solved c121)
    )
  )

  (:action assign-v28-false
    :parameters ()
    :precondition (unassigned v28)
    :effect
    (and
      (not (unassigned v28))
      (solved c11)
      (solved c20)
      (solved c31)
      (solved c51)
      (solved c70)
      (solved c78)
      (solved c82)
      (solved c96)
    )
  )

  (:action assign-v29-false
    :parameters ()
    :precondition (unassigned v29)
    :effect
    (and
      (not (unassigned v29))
      (solved c9)
      (solved c64)
      (solved c95)
      (solved c97)
    )
  )

  (:action assign-v30-false
    :parameters ()
    :precondition (unassigned v30)
    :effect
    (and
      (not (unassigned v30))
      (solved c43)
      (solved c52)
      (solved c67)
      (solved c91)
      (solved c93)
      (solved c102)
      (solved c103)
    )
  )

)
