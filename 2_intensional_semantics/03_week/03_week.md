# [Week 03](https://github.com/benbrastmckie/ModalHistory/tree/master?tab=readme-ov-file#week-03-carnap-and-kripke-feb-24)

## Overview

- Use a first-order language to provide the semantics of a first-order modal language
- Not really model theory since we are given a single canonical model
  - Defines what it is for modal claims to be true relative only to the language
  - Non-modal sentences are only true relative to a state-description
- L-truth as a semantical analysis of 'Nec'
- Aim to interpret logical calculi (proof systems) by these means
- Overcome the problem that analyticity is not applicable to open sentences
- Provide a decision procedure for evaluating L-truth and C-truth
- Provide a theory of logical consequence

## State Descriptions (1946)

### Introduction

- Aims to relate semantics and logic
  - Semantic systems: PL, FL, MPL, MFL
  - Proof systems: PC, FC, MPC, MFC
  - [p. 1] Sound "MPC and MFC are adequate, i.e., that every sentence provable in them is L-true (analytic)."
  - [p. 1] Complete "MPC is complete in the sense that every sentence which is L-true in MPL is provable in MPC."
  - Provides a decision procedure for MPC but not for MFC.
  - Shows soundness for MFC but not completeness.
- L-truth as explicatum for logical truth
  - L-truth provides a semantic analysis of 'Nec'
  - [p. 2] "[A] proposition p is logically necessary if and only if a sentence expressing p is logically true. That is to say, the modal concept of the logical necessity of a proposition and the semantical concept of the logical truth or analyticity of a sentence correspond to each other."
  - [p. 2] "C1-1... ‘N(...)’ is to be taken as true if and only if ‘...’ is L-true in S."
- Object language and metalanguage
  - [p. 2] 'This convention determines our interpretation of ‘N’, but it is not a definition for ‘N’. The sentence ‘N(...)’ cannot be transformed by definition into the sentence “ ‘...’ is L-true in S,” because the first sentence belongs to the object-language S, the second to the metalanguage M; but the first sentence holds, according to the convention, if and only if the second holds.'

### L-Concepts

- State-descriptions
  - [p. 17] "Every individual is denoted by an individual constant, and different individual constants denote different individuals."
  - "Therefore the semantical rules (D7-5f) are framed in such a way that 'a1 = a2', for example, is L-false."
  - [p. 18] "A state-description is a class of sentences which represents a possible specific state of affairs by giving a complete description of the universe of individuals with respect to all properties and relations designated by predicates in the system."
  - "D7-4. A class of sentences Ki is a state-description in FL = Df Ki contains for every atomic sentence Si either Si itself or ~Si, but not both, and no other sentences."
  - The class of all state-descriptions is called the universal range and denoted by 'Vs'; the null class (of the same type) is called the null range and denoted by 'Λs'.
- Range for each sentence
  - [p. 18] "We shall now lay down rules which determine for every sentence Si of FL, in which state-descriptions Si holds; in other words, what is the range of Si i.e., the class of those state descriptions in which Si holds. We shall write briefly 'R(Si)' for 'the range of Si'. That Si holds in a given state-description means, in non-technical terms, that this state-description entails C; in other words, that Si would be true if this state-description were the description of the actual state of the universe."
  - Range rules:
    - Negation is complement
    - Disjunction is union
    - Conjunction is intersection
    - Identity is "ridged"
    - Universal quantification is understood substitutionally
      - But what about small languages
      - Makes sense for the logical reading of the modals only
      - But Carnap does appeal at points to a worldly reading of quantification and modality
    - [p. 22] "The range of N(Si) is Vs if the range of Si is Vs, and otherwise Λs."
      - Yields an S5 Logic given there is no restriction
- Examples
  - $\exists x \Box Fx$ is true in a state-description S iff some closed formula $\Box Fa$ is true in S
    - iff $Fa$ is true in every state-description
    - But Fa is false in some state description
    - So $\exists x \Box Fx$ is false in all state-descriptions
  - Barcan formula is also L-true
  - Logical not metaphysical
    - "Gold has 79 protons"
    - "a = a" is L-true
    - "a = b" is L-false
- Reflections
  - Range of state-descriptions does not vary with state-descriptions
  - Substitution of constants for variables does not vary with the state-description
  - Thus we get BF and it's converse
  - Might be what one expects for logical necessity
- Definitions
  - [p. 19] D7-6. Defines L-true, L-false, L-implies, L-equivalence
    - Si is L-true (in FL) =Df R(Si) is Vs.
    - Si is L-false =Df R(Si) is Λs.
    - Si L-implies Si =Df R(Si) is included in R(Si).
    - Si is L-equivalent to Si =Df Si and Si have the same range.
  - [p. 22] Theorems
    - N Si is L-true if and only if Si is L-true.
    - N Si is L-false if and only if Si is not L-true.
    - N Si is L-true or L-false. (From D9-5i.)
    - T9-2. N( )[(ik)N(Mi) ≡ N(ik)(Mi)].
- Informal interpretation is worldly
  - "A sentence Si is usually regarded as logically true or logically necessary if it is true in every possible case. Therefore we call Si L-true if it holds in every state-description, in other words, if its range is Vs. Analogously, we use 'L-false' as explicatum for logical falsity or impossibility and define it by the null range. Si follows logically from Si if in every possible case in which Si holds, Si also holds. Therefore we define the explicatum 'L-implication' by the inclusion of the ranges. L-equivalence is meant as mutual L-implication; therefore it is defined by the identity of ranges."

## Carnap 1942

- Worldly informal interpretation
  - [p. 23] Pure vs descriptive semantics
  - [p. 34] Truth-conditional semantics
  - [p. 95] "situation which is possible though not real"
  - [p. 95-6] "ranges overlap"
  - [p. 101] L-state is a "possible state of affairs"
  - [p. 102] The L-range of a sentence is a state-description
  - [p. 112] State-descriptions reformulated as L-semantical concepts
  - [p. 119] State descriptions replace L-states (propositions) 

## Carnap 1946

### Factual and Logical Truth and Falsity

- Two types of truth
  - "I. The meaning of 'C' is given, that is to say, the interpretation assigned to 'C' by the semantical rules."
  - "II. Information concerning the facts relevant for 'C' is given, that is to say, concerning the properties and relations of the individuals involved."
  - [p. 3] "If the answer to a given question is merely dependent upon data of the kind I but independent of those of kind II, we call it a logical question; if in addition, data of the kind II are required, we call it a factual question."
  - Compare $A \vee \neg A$, $A \wedge \neg A$, $Pa \wedge \neg Qb$ for L-truth and L-falsity.
- Shows how to iterate the modal.
  - [p. 2] "Cl-1 gives a sufficient and necessary condition for the truth of ‘N( ... )’. Now the following two questions remain: (1) if 'N( ... )' is true, is it L-true? If so, 'NN( ... )' is likewise true; in other words, 'Np ⊃ NNp' is always true. (2) If 'N( ... )' is false, is it L-false? ('L-false' is taken as the explicatum for 'logically false,' 'self-contradictory.') If so, '~N( ... )' is L-true and hence 'N~N( ... )' is true; in other words, '~Np ⊃ N~Np' is always true."
  - [p. 4] "Suppose that 'N(C)' is true. Then, according to C1-1, 'C' must be L-true. Hence the truth of 'C' is determined by certain semantical rules. Then these same rules together with the rule for 'N' determine the truth of 'N(C)'. Therefore, 'N(C)' is L-true, and hence 'NN(C)' is true. Thus our earlier question (1) is answered in the affirmative."
  - [p. 4] "Let us now suppose that 'C' is L-false and hence 'N(C)' is false. Then those semantical rules which determine the falsity of 'C' together with the rule for 'N' determine the falsity of 'N(C)'. Therefore, 'N(C)' is L-false, and '~N(C)' is L-true."
  - [p. 4] "We found that 'A' [i.e., 'Pa.~Qb'] is neither L-true nor L-false by merely using semantical rules, not using any factual knowledge concerning the individuals occurring in 'A'. Therefore we see that, according to C1-1, 'N(A)' is false and '~N(A)' is true. These results are based merely on the semantical rules for the signs occurring in 'A' and for 'N'. Therefore, 'N(A)' is L-false and '~N(A)' is L-true."
- Considers L-true, L-false, and L-indeterminate
  - [p. 4] "Finally, let us suppose that 'N(C)' is false but 'C' is not L-false. Then 'C' is neither L-true nor L-false. The decisive question here is this: is the result that 'C' is not L-true determined by data I alone or are data II, i.e., factual knowledge, required? Data II are certainly relevant for the truth-value of 'C', but they cannot be relevant for the character of 'C' being L- indeterminate, factual, contingent."
  - "C1-2. If '...' is L-true, 'N(...)' is L-true; otherwise 'N(...)' is L-false."

### Logical Consequence

- Informal concept to be clarified
  - [p. 4-5] "In the preceding analysis, I have repeatedly referred to a certain result as "following from" or "determined by" certain data. This is not meant in the sense that the result can be derived from the data with the help of deductive means which are systematized in a given metalanguage; still less is it implied that there is an effective method for this derivation. What I mean is rather that, if the data hold, the result cannot possibly fail to hold. This is the wide, non-systematized concept of logical implication which logicians have in mind before they construct their systems and of which only a part can be grasped in any one fixed system. This concept is necessarily inexact; but it is clear enough for practical purposes of pre-systematic discussions."
  - [p. 5] "C1-3. 'N' is to be interpreted in such a way that any sentence of the form '(x)[N(. . x . .)]' is regarded as L-equivalent to (i.e., meaning the same as) the corresponding sentence 'N[(x)(. . x . .)]'."
  - Quantifiers characterized in terms of conjunction and disjunction.

### Reduction

- Semantics S and calculus K
  - Both are built out of syntax but S is intended to provide an interpretation
  - K is an S5 system
- MP-reduction
  - [p. 14] "The reduction of such a formula leads to ‘t’ if and only if every sentence obtainable from the formula by substitutions is L-true by MPL and Ctrue by MPC. In the MP-reductum of any such formula, no ‘N’ occurs in the scope of another ‘N’."
- Advantages of S5
  - [p. 14-5] "The completeness of this system is a further advantage. On the basis of the interpretation given by MPL, all sentences C-true (provable) in MPC and MPCv are L-true, while those principles of other systems which go beyond Lewis’s S5 are L-false."
  - [p. 15] "My chief reason for preferring the interpretation given by MPL is the simple parallelism between the modalities in this system and the semantical L-concepts, in particular between necessity and L-truth. It is true that these semantical concepts could be defined in a different way so as to correspond to a different conception of the modalities."
  - "However, the definition of L-truth here chosen, which is based on Wittgenstein’s conception of the nature of logical truth, has the advantage of great simplicity, taking as criterion the universality of the range (D7-6a)."

### Proof Theory

- [p. 20] Specifies FC 
  - Sound [p. 21] "Every primitive sentence of FC is L-true in FL. Every C-true sentence in FC is L-true in FL."
  - Complete "It is not clear whether FC is complete in the sense that every sentence which is L-true in FL is C-true in FC."
  - "Gödel's theorem of the completeness of the ordinary functional calculus of first order cannot be directly applied to FC because [i]n ordinary functional logic, a sentence is regarded as L-true [...] if it is L-true not only in the infinite universe of individuals but, in addition, in every finite (non-null) universe. In FL, on the other hand, more sentences are regarded as L-true, viz. all those which are L-true in the infinite universe."
    - $\exists x \exists y (x \neq y)$ is "L-true in FL [...] but not L-true in the ordinary functional logic."
    - "T8-2. If Si is an L-true sentence in FL without '=' then Si is C-true, in FC."
- [p. 22] Specifies MFC
  - N( )(Mi), where Mi is any matrix whose P-reductum (D3-1) is 't'.
  - N( )[(Mi ⊇ Mi ) ⊃ (NMi ⊇ NMi)].
  - ( )[NMi ⊃ Mi ].
  - N( )[NMi ∨ N~NMi ].
  - N Si , where Si has one of the forms D8-1b to h, respectively (primitive sentences of FC).
  - N( )[(ik)N(Mi) ⊃ N(ik)(Mi)].
  - N( )[N(ik)(Mi) ⊃ (ik)N(Mi )].
  - N( )[ii = ik1 ∨ ii = ik2 ∨ ... ∨ ii = ikn ∨ ~NMi ∨ NMi]; here Mi does not contain ‘=’, ‘N’, any quantifier with ii
- [p. 24] Theorems
  - ( )[( ∃ ik)N(Mk) ⊇ N( ∃ ik)(Mk)]
  - ( )[◊( ik)(Mk) ⊇ (ik)◊(Mk)]
  - Mentions that the converses need not hold.
- MF-reduction
  - Not possible to provide an effective procedure
  - [p. 31] Provides something partial which, "makes it possible to apply partial solutions for FL, that is to say, decision methods for restricted classes of sentences in FL, to MFL in the following manner."
- [p.30] Soundness T12-1
  - "Every primitive sentence of MFC is L-true in MFL."
  - "Every C-true sentence in MFC is L-true in MFL."
  - (From (a); see T8-1b.) Whenever C-falsity in MFC holds, then L-falsity in MFL holds. Analogously with b. c. C-implication and L-implication, and with C-equivalence and L-equivalence. (From (b).) MFL is an L-true interpretation of MFC, (From (a) and (b); see T8-1c.) d. We shall now show that MFC is strong enough to cover the transformation by MF- reduction (T12-2b). However, the further question whether it is also strong enough to yield all L- true sentences remains open, as we shall see.
- Completeness of FC is unknown
  - It is known for standard first-order logic (Godel 1930)
  - [p. 31] "[I]t is not known whether FC is complete. Therefore, it is likewise an open question whether or not MFC is complete in the sense that every sentence which is L-true in MFL is C-true in MFC."
  - Gives a partial answer when identity and negated necessities are excluded.
- [p. 32] Plugs his 1947 book which he claims will, "overcome the difficulties which Quine has pointed out for sentences combining modalities and quantification. Without an elimination of these difficulties, no modal functional logic could be constructed."

## Carnap 1947

### Same basic setup

- [p. 9] State-descriptions as complete description of a possible state of the universe
  - Mentions Leibniz and Wittgenstein
- [p. 9-10] Rules of ranges provide interpretation
- [p. 10] L-truth defined
- [p. 174] Method by which to determine which axioms are to be included

### Quantified Modality

- [p. 178] Will interpret variables in terms of value-intensions
- [p. 181] Defines individual concepts (value-intensions)
- [p. 183-4] Interprets open sentences
  - substitutions do vary by state-description
  - $\exists x \Box (a = x)$ is not L-true
  - $\exists x (a = x \wedge \neg \Box (a = x)) is L-false
- [p. 195] Response to Quine

## Kripke (1959) "A Completeness Theorem in Modal Logic"

- Complete assignments: function from
  - variables to D
  - propositional variables to T/F
  - predicates to n-tuples in D
- Models are a complete assignment G and a set of complete assignments K
