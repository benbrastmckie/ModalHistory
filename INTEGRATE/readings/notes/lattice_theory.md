# A Brief Guide to Lattice Theory

## Introduction to Order Theory

Order theory provides the conceptual foundation for lattice theory by studying mathematical structures that capture the intuitive notion of ordering or arrangement. This field explores how elements can be compared and organized according to specific relations.

### Partially Ordered Sets (Posets)

At the heart of order theory is the **partially ordered set** or **poset**. This fundamental structure consists of a set P together with a binary relation ≤ that satisfies three essential properties:

1. **Reflexivity**: Every element is related to itself; a ≤ a for all a ∈ P
2. **Antisymmetry**: If a ≤ b and b ≤ a, then a = b (mutual ordering implies equality)
3. **Transitivity**: If a ≤ b and b ≤ c, then a ≤ c (the relation extends along chains)

The term "partially" indicates that not all elements need be comparable—there may exist elements a, b where neither a ≤ b nor b ≤ a holds.

#### Illustrative Examples of Posets

- **Natural numbers with standard ordering**: (ℕ, ≤) where 1 ≤ 2 ≤ 3 and so on
- **Power set ordered by inclusion**: (P(S), ⊆) where A ⊆ B means every element of A is also in B
- **Divisibility relation on integers**: (ℕ, |) where a | b means a divides b evenly
- **Logical propositions with implication**: Propositions ordered by logical entailment

#### Key Concepts in Posets

- **Comparable elements**: Elements a, b where either a ≤ b or b ≤ a
- **Incomparable elements**: Elements a, b where neither a ≤ b nor b ≤ a holds
- **Minimal element**: An element with no strictly smaller elements
- **Maximal element**: An element with no strictly larger elements
- **Least/greatest element**: An element that is smaller/greater than all other elements
- **Chain**: A subset where every pair of elements is comparable (totally ordered)
- **Antichain**: A subset where no two distinct elements are comparable

### Upper and Lower Bounds

For understanding lattices, the concepts of bounds are crucial:

- **Upper bound** of a subset S: An element u where s ≤ u for all s ∈ S
- **Lower bound** of a subset S: An element l where l ≤ s for all s ∈ S
- **Least upper bound (supremum)** of S: The smallest among all upper bounds of S
- **Greatest lower bound (infimum)** of S: The largest among all lower bounds of S

Not all subsets in a poset will have suprema or infima. When these exist for every pair of elements, we arrive at the notion of a lattice.

## From Posets to Lattices

### Lattice Definition (Order-Theoretic)

A **lattice** is a poset (L, ≤) with the special property that every pair of elements has both:
1. A least upper bound (also called supremum or join)
2. A greatest lower bound (also called infimum or meet)

For any elements a, b in a lattice:
- Their join (a ∨ b) is the smallest element greater than or equal to both a and b
- Their meet (a ∧ b) is the largest element less than or equal to both a and b

The existence of these operations for every pair of elements distinguishes lattices from general posets.

### Fundamental Properties of Lattices

The order-theoretic definition of lattices naturally leads to several important properties:

1. **Commutativity**:
   - a ∨ b = b ∨ a
   - a ∧ b = b ∧ a

2. **Associativity**:
   - a ∨ (b ∨ c) = (a ∨ b) ∨ c
   - a ∧ (b ∧ c) = (a ∧ b) ∧ c

3. **Idempotence**:
   - a ∨ a = a
   - a ∧ a = a

4. **Absorption Laws**:
   - a ∨ (a ∧ b) = a
   - a ∧ (a ∨ b) = a

These properties emerge naturally from the definitions of meet and join as infimum and supremum.

## Semilattices: Building Blocks for Lattices

Before exploring advanced lattice concepts, it's helpful to understand semilattices, which capture part of the structure of full lattices.

### Join-Semilattices

A **join-semilattice** is a poset where every pair of elements has a join (least upper bound). Formally, for any a, b in the poset, the element a ∨ b exists with properties:
- a ≤ a ∨ b and b ≤ a ∨ b (upper bound property)
- If a ≤ c and b ≤ c for any c, then a ∨ b ≤ c (least property)

### Meet-Semilattices

A **meet-semilattice** is a poset where every pair of elements has a meet (greatest lower bound). Formally, for any a, b in the poset, the element a ∧ b exists with properties:
- a ∧ b ≤ a and a ∧ b ≤ b (lower bound property)
- If c ≤ a and c ≤ b for any c, then c ≤ a ∧ b (greatest property)

## The Algebraic Perspective on Lattices

In parallel with the order-theoretic definition, lattices can be defined algebraically without explicit reference to the underlying order.

### Lattices as Algebraic Structures

A **lattice** is a set L with two binary operations ∨ (join) and ∧ (meet) satisfying:

1. **Commutativity**: 
   - a ∨ b = b ∨ a
   - a ∧ b = b ∧ a

2. **Associativity**: 
   - a ∨ (b ∨ c) = (a ∨ b) ∨ c
   - a ∧ (b ∧ c) = (a ∧ b) ∧ c

3. **Absorption Laws**: 
   - a ∨ (a ∧ b) = a
   - a ∧ (a ∨ b) = a

4. **Idempotence**: 
   - a ∨ a = a
   - a ∧ a = a

This algebraic definition is equivalent to the order-theoretic one. Given an algebraically defined lattice, we can recover the partial order by defining:
- a ≤ b if and only if a ∨ b = b
- Equivalently, a ≤ b if and only if a ∧ b = a

This equivalence demonstrates how lattices bridge order theory and abstract algebra.

### Deriving Absorption Laws from the Order-Theoretic Definition

The absorption laws are not arbitrary but follow naturally from the order-theoretic definition of a lattice. Here's how we can derive the first absorption law, a ∨ (a ∧ b) = a:

1. From the definition of meet, a ∧ b ≤ a
2. By the properties of join as a least upper bound:
   - a ≤ a ∨ (a ∧ b) (since a ∨ x ≥ a for any x)
   - a ∨ (a ∧ b) ≤ a (since if y ≥ a and y ≥ a ∧ b, then y ≥ a ∨ (a ∧ b), and we know that both a ≥ a and a ≥ a ∧ b)
3. By antisymmetry, a ∨ (a ∧ b) = a

The second absorption law, a ∧ (a ∨ b) = a, follows similarly:

1. From the definition of join, a ≤ a ∨ b
2. By the properties of meet as a greatest lower bound:
   - a ∧ (a ∨ b) ≤ a (since a ∧ x ≤ a for any x)
   - a ≤ a ∧ (a ∨ b) (since if y ≤ a and y ≤ a ∨ b, then y ≤ a ∧ (a ∨ b), and we know that both a ≤ a and a ≤ a ∨ b)
3. By antisymmetry, a ∧ (a ∨ b) = a

## Illustrative Examples of Lattices

Lattices appear naturally in many mathematical contexts:

### Power Set Lattice

For any set S, the collection of all subsets P(S) forms a lattice when ordered by inclusion (⊆):
- The join A ∨ B is the union A ∪ B
- The meet A ∧ B is the intersection A ∩ B
- The bottom element is the empty set ∅
- The top element is the entire set S

### Divisibility Lattice

The set of positive integers forms a lattice under the divisibility relation (where a ≤ b means a divides b):
- The join a ∨ b is the least common multiple lcm(a,b)
- The meet a ∧ b is the greatest common divisor gcd(a,b)
- The bottom element is 1 (which divides everything)
- If we include 0, it serves as the top element (everything divides 0)

### Chains (Totally Ordered Sets)

Any totally ordered set automatically forms a lattice:
- The join a ∨ b is max(a,b)
- The meet a ∧ b is min(a,b)
- Examples include the real numbers, integers, or any subset of these with the usual ordering

### Partition Lattice

The set of all partitions of a set forms a lattice when ordered by refinement (where P₁ ≤ P₂ means P₁ is a refinement of P₂):
- The join is the least common coarsening
- The meet is the greatest common refinement
- The bottom element is the partition into singletons
- The top element is the partition with a single block containing all elements

## Special Types of Lattices

### Bounded Lattices

A **bounded lattice** has both a greatest element (top, denoted ⊤) and a least element (bottom, denoted ⊥). In a bounded lattice:
- ⊤ ≥ a for all elements a
- ⊥ ≤ a for all elements a

Many naturally occurring lattices are bounded, such as power set lattices and finite divisibility lattices.

### Distributive Lattices

A lattice is **distributive** if the following distributive laws hold:
- a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c)
- a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c)

In fact, if one of these laws holds, the other follows. Distributivity is an important property that rules out certain "anomalous" lattice structures.

Examples of distributive lattices include:
- Power set lattices (subsets with set operations)
- Chains (totally ordered sets)
- Divisibility lattices

An example of a non-distributive lattice is the "diamond lattice" M₃, which has a top element, a bottom element, and three incomparable elements between them.

### Complete Lattices

A **complete lattice** is a poset where every subset (not just pairs) has both a supremum and an infimum. This generalizes the pairwise meet and join operations to arbitrary collections of elements:
- For any subset S, the supremum ⋁S exists
- For any subset S, the infimum ⋀S exists

Every complete lattice is automatically bounded because:
- The supremum of the empty set is the bottom element ⊥
- The infimum of the empty set is the top element ⊤

Examples of complete lattices include:
- Finite lattices (all lattices with finitely many elements)
- Power set lattices
- The closed intervals of real numbers

## Complemented Lattices

### Basic Definition and Properties

A **complemented lattice** is a bounded lattice where every element has at least one "complement"—an element that, when combined with it, spans the entire lattice and, when intersected with it, gives the bottom element.

Formally, in a bounded lattice L, an element b is a **complement** of a if:
- a ∧ b = ⊥ (meet is bottom)
- a ∨ b = ⊤ (join is top)

Key observations about complemented lattices:
1. Not all bounded lattices are complemented
2. In general complemented lattices, elements can have multiple complements
3. The complement relation is symmetric: if b is a complement of a, then a is a complement of b
4. The extremal elements have unique complements: the complement of ⊤ is ⊥, and vice versa

### Uniqueness of Complements in Distributive Lattices

An important property of distributive lattices is that complements, when they exist, are unique. We can prove this as follows:

If a has two complements b and c, then:
- b = b ∧ ⊤ = b ∧ (a ∨ c) = (b ∧ a) ∨ (b ∧ c) = ⊥ ∨ (b ∧ c) = b ∧ c
- Similarly, c = c ∧ b
- Therefore, b = c

This proof relies crucially on the distributive law.

### Challenges with Non-Distributive Lattices

In non-distributive lattices, elements can have multiple complements. Consider the classic example of M₃ (the "diamond lattice"):

```
      ⊤
     /|\ 
    a b c
     \|/
      ⊥
```

Here, both b and c are complements of a. Similarly, both a and c are complements of b, and both a and b are complements of c.

Ensuring unique complements in non-distributive lattices requires additional structure beyond standard order theory.

## Boolean Algebras: Distributive Complemented Lattices

A **Boolean algebra** is a distributive complemented lattice—it combines distributivity with the requirement that every element has a complement.

### Properties of Boolean Algebras

In a Boolean algebra, each element a has a unique complement, typically denoted a':
- a ∧ a' = ⊥
- a ∨ a' = ⊤
- (a')' = a (involution)

Additionally, Boolean algebras satisfy the De Morgan laws:
- (a ∧ b)' = a' ∨ b'
- (a ∨ b)' = a' ∧ b'

These properties make Boolean algebras ideal for modeling logical systems and set-theoretic operations.

### Atomic Boolean Lattices

An **atom** in a bounded lattice is an element a that is minimal among the non-bottom elements—there is no element x with ⊥ < x < a.

A Boolean lattice is **atomic** if every non-bottom element can be expressed as the join (supremum) of atoms. This property ensures that the algebra has a "building block" structure.

Key properties of atomic Boolean lattices:
1. Every finite Boolean lattice is atomic
2. A finite Boolean lattice with n atoms has exactly 2ⁿ elements
3. Any finite atomic Boolean lattice with n atoms is isomorphic to the power set of an n-element set

The classic example is the power set lattice P(X), where the atoms are precisely the singleton sets {x} for each x ∈ X.

## Bilattice Theory: A Double-Ordered Perspective

### Introduction to Bilattices

While standard lattice theory deals with a single ordering relation, **bilattice theory** extends this by considering structures with two distinct lattice orderings on the same set. This dual-ordered approach was introduced by Matthew Ginsberg in 1988 for reasoning with uncertainty and potentially conflicting information.

### Formal Definition

A **bilattice** is a structure B = (B, ≤, ⊑) where B is a nonempty set equipped with two complete lattices (B, ≤) and (B, ≤) where:

- A ≡ ~~A
- A ≤ B := ~A ⊑ ~B  
- A ⊑ B := ~A ≤ ~B  

### Constitutive Reading

1. The **sufficient-for ordering** ≤ represents degrees of sufficiency or logical strength. When x ≤ y, we intuitively understand that "x is sufficient for y".
2. The **necessary-for ordering** ⊑ represents degrees of necessity or modal requirement. When x ⊑ y, we understand that "x is necessary for x".

Each ordering gives rise to its own meet and join operations:

- Sufficiency lattice operations (≤):
  - ∨ (join with respect to ≤): combines sufficient conditions like logical OR
  - ⊕  (meet with respect to ≤): represents intersection of sufficient conditions

- Necessity lattice operations (⊑):
  - ∧ (join with respect to ⊑): combines necessary conditions like logical AND
  - ⊗ (meet with respect to ⊑): represents overlap of necessary conditions

### Properties of Bilattices

1. **Interlacing**: A bilattice is interlaced if each operation of one ordering (meet/join) is monotonic with respect to the other ordering.

2. **Distributivity**: A bilattice is distributive if all twelve possible distributive laws involving three operations hold.

3. **Negation**: Many bilattices include a negation operation that:
   - Inverts the truth ordering
   - Preserves the knowledge ordering
   - Is an involution (self-inverse)
