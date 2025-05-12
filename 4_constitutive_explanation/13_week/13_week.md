# [Week 13](https://github.com/benbrastmckie/ModalHistoryPrivate?tab=readme-ov-file#module-4-constitutive-explanation)

## Disjunctive and Conjunctive Parthood

- Lattice Theory
  - Order theory: poset with meet and joins for any two elements
  - Algebra: meet and join satisfy commutativity, associativity, idempotence, and absorption
    - Derive absorption:
      1. a ≤ a ∨ (a ∧ b)
      2. a ≤ a
      3. a ∧ b ≤ a
      4. By the definition of join, a ∨ (a ∧ b) ≤ a
      5. By antisymmetry, a ∨ (a ∧ b) = a
  - Lattice Properties
    - Bounded
    - Complemented = bounded + complements exist (but need not be unique)
    - Distributive
    - Boolean = distributive + complemented (complements may be shown to be unique)
    - Complete
- Essence and Ground
  - Give definitions in terms of identity
  - Interderivable given de Morgan's and negations transparency
  - Both are reflexive, anti-symmetric, and transitive `CL_TH_16 - CL_TH_19`
  - Give the derived semantic clauses for conjunctive-part and disjunctive-part
  - Use the model-checker to confirm this with `CL_TH_3 - CL_TH_6`
  - Check that essence and ground are duals with `CL_TH_1 - CL_TH_2`
  - Essence and ground are also both complete
  - Given that `\neg \neg A \equiv A` holds, the space of propositions forms a bilattice
- Reduction
  - In place of equivalences, we now get reductions for both absorption and distribution `CL_TH_10 - CL_TH_13`
  - Ground entails strict implication and essence entails the converse `CL_TH_14 - CL_TH_15`
  - Given intensionalism, this explains why these seem like identities
  - But in this setting they are directed, accommodating a direction of explanation
- Identity
  - Everything is definable in terms of propositional identity, conjunction, distribution, and negation
  - Could eliminate either conjunction or disjunction, but kept for clarity
  - We may then provide the rules for the first-degree fragment

## Subject-Matter  

- Convex Semantics
  - Convex semantics for subject-matter validates analytic equivalence for distribution
  - Also validates an idempotence axiom S8 `\sigma \sigma A = \sigma A`
  - Yields a derived semantics for analytic equivalence that is the same as what Fine provides
  - But does not make the distribution laws preserve subject-matter in nonvacuous models (p. 1495)
  - Also fails to validate S1 and S2 on account of separating treatment of verifiers and falsifiers
- Undirected and Partial
  - Close under all parts of either the verifiers or falsifiers
  - Makes negation eliminate and commute
  - But fails to validate S2 over the normal models given vacuous annihilation
- Dual Semantics
  - Positive subject-matter includes all parts of the verifiers for a sentence and its dual 
  - Same for the negative subject-matter, though this is defined
  - Putting these together we get all parts of the verifiers or falsifiers for a sentence and its dual
  - Intuitive reading is "It is partly the case that A or it is partly not the case that A"
  - Makes subject-matter distribute over conjunction and distribution

## Relevance  

- Partial Subject-Matter
  - Can define relevance as partial-subject-matter using either essence or ground
  - Can also define relevance as disjunctive-conjunctive-part or conjunctive-disjunctive-part
  - These turn out to be equivalent given the absorption identity
  - Relevance points in the same direction as strict implication in ground
  - Relevance points in the opposite direction as strict implication in essence
  - Relevant implication looks to me like the converse of essence
  - But rather ground should make for a better theoretical target in this connection
- Propositional Ground
  - Compare to ontological dependence
  - Objects don't explain each other
- Propositional Essence
  - Compare to objectual essence

## BitVectors  

- A Z3 Data Type
  - The bitwise operators
  - Bit blasting + bag of tricks
  - Atomic Boolean algebra
- BitVectors and States
  - The or operator `|` is fusion
  - Defining parthood
  - Primitive for possible states
  - Defining world-states, etc.

## Programmatic Semantics

- Semantics class
  - Z3 sorts
  - Introducing primitives
  - Defining methods
  - Frame constraints
- Proposition class
  - Identity conditions
  - Representation
  - Constraints
- Structure class
  - Store and print
  - Model differences

# Language of Thought

- Intro
  - Towards a unified theory 
  - Renaming the default theory
  - Metaphysical, epistemic, and normative
- Tensed Counterfactuals
  - Bimodal semantics defined worlds to be functions from times to world-states
  - Counterfactual semantics defined world-states from states, parthood, and tasks
  - These can be put together in two different, but equivalent ways
- Indicatives
  - Semantics via updating with antecedent
  - Define 'A compatible part of B'
  - Define 'Maximal A compatible part of B'
  - Define 'Update B with A'
- Hyperintensional Causation
- Logical Subtraction and Belief Revision