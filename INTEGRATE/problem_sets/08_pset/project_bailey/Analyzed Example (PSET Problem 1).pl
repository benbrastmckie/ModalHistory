PS C:\Users\userx\ModalHistoryPrivate-1\problem_sets\08_pset\project_bailey> model-checker examples.py
========================================

EXAMPLE CF_CM_4: there is a countermodel.

Atomic States: 4

Semantic Theory: Brast-McKie

Premises:
1. \neg A
2. (A \boxright C)

Conclusion:
3. ((A \wedge B) \boxright C)

Z3 Run Time: 0.0252 seconds

========================================
State Space:
  #b0000 = □
  #b0001 = a
  #b0010 = b
  #b0011 = a.b (world)
  #b0100 = c
  #b0101 = a.c (world)
  #b1000 = d
  #b1010 = b.d (world)
  #b1100 = c.d (world)

The evaluation world is: a.b

INTERPRETED PREMISES:

1.  |\neg A| = < {a, a.b}, {d} >  (True in a.b)
      |A| = < {d}, {a, a.b} >  (False in a.b)

2.  |(A \boxright C)| = < {□}, ∅ >  (True in a.b)
      |A| = < {d}, {a, a.b} >  (False in a.b)
      |A|-alternatives to a.b = {b.d}
        |C| = < {b.d}, {a.b, a.c, c.d} >  (True in b.d)

INTERPRETED CONCLUSION:

3.  |((A \wedge B) \boxright C)| = < ∅, {□} >  (False in a.b)
      |(A \wedge B)| = < {b.d, c.d}, {a, a.b} >  (False in a.b)
        |A| = < {d}, {a, a.b} >  (False in a.b)
        |B| = < {b.d, c, c.d}, {a.b} >  (False in a.b)
      |(A \wedge B)|-alternatives to a.b = {b.d, c.d}
        |C| = < {b.d}, {a.b, a.c, c.d} >  (True in b.d)
        |C| = < {b.d}, {a.b, a.c, c.d} >  (False in c.d)

Total Run Time: 1.2849 seconds


##The above is an output for a countermodel of the formula \neg(A) , <\A \boxright B, \MLModels \(A \wedge)B \boxright C.
##Formally, we can see that (A \wedge B) \boxright C is a logical falsehood on this model (its verifier is the empty state and the falsifier is the null state).
## The verifiers for \neg A  are a and a.b. A \boxright C also has a verifier. Even though the world is evaluated at a.b, all we need to show that the verifeir for a (d) 
##can transition to the verifier for C (b.d.). So evaluation at a.b. will validate\neg A and A \boxright C. By contrast, while A \wedge B will transition to C, the initial evaluation 
##world A \wedge B will be false, because C will also need to hodl in C, which it does not. 


##Concrete Example: Suppose Kathy will not go to a party and, if she goes, it would be fund. Does it follow that it Kathy and John both go to the party, it will be fun? 
##Not necessarily, maybe Kathy and John are vicious exes. So the countermodel maps on to natural language intuitions. 