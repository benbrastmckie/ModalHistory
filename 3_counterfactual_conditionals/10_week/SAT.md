# The Evolution of SAT Solving Algorithms

## Historical Context

The field of Boolean satisfiability (SAT) solving has evolved significantly since the 1960s:

- The original **Davis-Putnam (DP) algorithm** was published in 1960 by Martin Davis and Hilary Putnam.
- The **DPLL algorithm** was presented in 1962 by Martin Davis, Hilary Putnam, George Logemann, and Donald Loveland as an improvement to address memory issues in the original approach.
- **Conflict-Driven Clause Learning (CDCL)** emerged in the 1990s as a significant advancement over DPLL.

## The Original Davis-Putnam Algorithm (1960)

The Davis-Putnam algorithm was the first complete procedure for deciding the satisfiability of propositional logic formulas in conjunctive normal form (CNF).

### Key Characteristics

- **Resolution Principle**: Primarily relies on variable elimination through resolution
- For a variable v, it computes all possible resolvents between clauses containing v and clauses containing ¬v, then removes all clauses with v or ¬v
- Resolution can cause exponential growth in formula size

```
To eliminate variable v from a CNF formula:
  R = {}  // Initialize an empty set to store resolvents
  
  // Resolution step:
  For each clause C₁ containing the positive literal v:
    For each clause C₂ containing the negative literal ¬v:
      // Compute the resolvent of C₁ and C₂ on variable v:
      resolvent = (C₁ ∪ C₂) \ {v, ¬v}
      
      if resolvent is not a tautology:
        R = R ∪ {resolvent}
  
  // Replacement step:
  Remove all clauses containing v or ¬v from the formula
  Add all clauses in R to the formula
```

- **Unit Propagation**: Applied as a simplification rule before variable elimination
- **Variable Selection**: Uses a fixed order of variable elimination
- **Memory Usage**: Can generate an exponential number of clauses, leading to memory explosion

## The DPLL Algorithm (1962)

The Davis-Putnam-Logemann-Loveland (DPLL) algorithm represents a significant refinement of the original DP procedure, addressing its memory limitations.

### Algorithm Definition

```
function DPLL(φ, assignment):
    # Apply unit propagation
    (φ', assignment') = UnitPropagate(φ, assignment)
    
    # Check termination conditions
    if φ' contains an empty clause:
        return "Unsatisfiable"
    if φ' has no clauses:
        return "Satisfiable", assignment'
    
    # Choose a variable to branch on
    v = ChooseVariable(φ')
    
    # Try v = true
    if DPLL(φ' ∧ v, assignment' ∪ {v ↦ true}) returns "Satisfiable", m:
        return "Satisfiable", m
    
    # Try v = false
    return DPLL(φ' ∧ ¬v, assignment' ∪ {v ↦ false})
```

### Key Components

1. **Backtracking Search**: Replaces resolution with a recursive, depth-first tree search approach
   - Makes tentative assignments to variables and explores consequences
   - Explores one branch completely before backtracking
   - Avoids the memory explosion problem of DP

2. **Unit Propagation**:
   - When a clause contains only one literal, that literal must be true
   - Integrated directly into the search procedure
   - Applied immediately after each variable assignment

3. **Pure Literal Elimination** (optional extension):
   - If a variable appears only positively or only negatively, it can be assigned to make those literals true

4. **Variable Selection Heuristics**:
   - Can use various heuristics to select the next variable for branching
   - This selection significantly impacts performance

### Memory Efficiency

- Uses constant space per recursive call
- Total space complexity is O(n) where n is the number of variables
- More practical for large problem instances

### Complexity

- Worst-case time complexity: O(2ⁿ) where n is the number of variables
- Space complexity: O(n + m) where m is the number of clauses

### Example: Tracing DPLL Execution

Let's trace through the DPLL algorithm on a concrete CNF formula:

φ = (x₁ ∨ x₂) ∧ (¬x₁ ∨ x₃) ∧ (¬x₂ ∨ ¬x₃) ∧ (x₂ ∨ ¬x₃)

We'll represent this as a set of clauses:
- C₁ = {x₁, x₂}
- C₂ = {¬x₁, x₃}
- C₃ = {¬x₂, ¬x₃}
- C₄ = {x₂, ¬x₃}

**Initial call**: DPLL(φ, {})

**Step 1**: Apply unit propagation
- No unit clauses exist, so φ' = φ and assignment' = {}

**Step 2**: Check termination conditions
- φ' has no empty clauses and still contains clauses, so continue

**Step 3**: Choose a variable
- Let's select x₁

**Step 4**: Try x₁ = true
- Call DPLL(φ ∧ x₁, {x₁ ↦ true})
- After assigning x₁ = true:
  - C₁ is satisfied, so remove it: {C₂, C₃, C₄}
  - In C₂, ¬x₁ is false, so remove it: C₂ becomes {x₃}
  - C₂ is now a unit clause

- Apply unit propagation on {x₃} ∧ (¬x₂ ∨ ¬x₃) ∧ (x₂ ∨ ¬x₃):
  - Set x₃ = true
  - C₂ is satisfied, so remove it
  - In C₃, ¬x₃ is false, so remove it: C₃ becomes {¬x₂}
  - In C₄, ¬x₃ is false, so remove it: C₄ becomes {x₂}
  - We now have unit clauses {¬x₂} and {x₂}

- Further unit propagation:
  - From {¬x₂}, set x₂ = false
  - From {x₂}, set x₂ = true
  - This creates a contradiction!

- Since we have a contradiction, return "Unsatisfiable" for this branch

**Step 5**: Try x₁ = false
- Call DPLL(φ ∧ ¬x₁, {x₁ ↦ false})
- After assigning x₁ = false:
  - In C₁, x₁ is false, so remove it: C₁ becomes {x₂}
  - C₂ is satisfied, so remove it
  - We now have: {x₂} ∧ (¬x₂ ∨ ¬x₃) ∧ (x₂ ∨ ¬x₃)

- Apply unit propagation on {x₂} ∧ (¬x₂ ∨ ¬x₃) ∧ (x₂ ∨ ¬x₃):
  - Set x₂ = true
  - C₁ is satisfied, so remove it
  - In C₃, ¬x₂ is false, so remove it: C₃ becomes {¬x₃}
  - C₄ is satisfied (since x₂ is true), so remove it
  - We now have just one clause: {¬x₃}

- Further unit propagation:
  - From {¬x₃}, set x₃ = false
  - All clauses are now satisfied

- Since no clauses remain, return "Satisfiable" with assignment {x₁ ↦ false, x₂ ↦ true, x₃ ↦ false}

**Final result**: The formula is satisfiable with the assignment:
- x₁ = false
- x₂ = true
- x₃ = false

## Conflict-Driven Clause Learning (CDCL) (1990s)

CDCL represents a significant advancement in SAT solving technology, building upon the foundation of the DPLL algorithm by incorporating powerful learning mechanisms.

### Algorithm Definition

```
function CDCL(φ):
    assignment = {}
    decision_level = 0
    
    while true:
        // Unit propagation (BCP)
        status = UnitPropagate(φ, assignment)
        
        if status is CONFLICT:
            // Handle conflict
            if decision_level == 0:
                return UNSATISFIABLE
            
            // Analyze conflict, learn new clause
            backtrack_level, learned_clause = AnalyzeConflict()
            
            // Add the learned clause to formula
            φ = φ ∧ learned_clause
            
            // Backtrack to appropriate level
            Backtrack(backtrack_level)
        
        else if IsComplete(assignment):
            return SATISFIABLE, assignment
        
        else:
            // Make a new decision
            decision_level++
            variable = SelectVariable(φ, assignment)
            value = SelectValue(variable)
            assignment = assignment ∪ {variable ↦ value}
            // Record this as a decision (not from propagation)
            RecordDecision(variable, decision_level)
```

### Key Components

1. **Implication Graph**:
   - A directed graph where nodes represent variable assignments
   - Edges represent implications from unit propagation
   - Decision variables have no incoming edges

2. **Conflict Analysis**:
   - Identifies the conflict clause (a clause falsified by current assignment)
   - Derives a "reason" for the conflict by analyzing the implication graph
   - Constructs a conflict clause that captures this reason
   - Determines an appropriate backtracking level

3. **Non-Chronological Backtracking**:
   - Jumps back to the level determined by conflict analysis
   - May backtrack multiple levels at once
   - Backtracks to the second highest decision level in the learned clause

4. **Clause Learning**:
   - The learned clause prevents the same conflict from recurring
   - It becomes unit after backtracking

### Relationship to DPLL

#### Similarities
- Both perform a backtracking search over variable assignments
- Both use unit propagation as a core simplification procedure
- Both are complete algorithms for SAT

#### Critical Differences

1. **Conflict Handling**:
   - **DPLL**: Simply backtracks to the most recent decision and tries the opposite value
   - **CDCL**: Analyzes the conflict to learn a new clause, then backtracks to an appropriate level

2. **Backtracking Strategy**:
   - **DPLL**: Chronological backtracking (always to the most recent decision)
   - **CDCL**: Non-chronological backtracking (can jump back multiple levels)

3. **Learning**:
   - **DPLL**: No learning; repeats the same mistakes in different contexts
   - **CDCL**: Learns from conflicts; adds new clauses to avoid similar conflicts

4. **Implementation Focus**:
   - **DPLL**: Conceptually simpler, recursive implementation
   - **CDCL**: Typically iterative, with complex data structures for efficient clause management

## Modern SAT Solving Techniques

Modern SAT solvers extend the CDCL framework with additional optimizations:

1. **Watched Literals**:
   - Efficient mechanism for detecting unit clauses and conflicts

2. **Advanced Variable Selection Heuristics**:
   - VSIDS (Variable State Independent Decaying Sum)
   - Activity-based heuristics that favor variables involved in recent conflicts

3. **Restart Strategies**:
   - Periodically abandon the current search tree while keeping learned clauses
   - Helps escape from unfruitful regions of the search space

4. **Efficient Data Structures**:
   - Optimized representations of clauses, variables, and assignments

5. **Proof Generation**:
   - CDCL can efficiently generate resolution proofs based on learned clauses

## Impact and Applications

The evolution from DP to DPLL to CDCL has transformed SAT solving from a theoretical concern to a practical technology:

- Modern CDCL-based SAT solvers can handle industrial instances with hundreds of thousands of variables and millions of clauses
- These problems would be completely intractable for pure DPLL implementations
- SAT solving has become a core technology in formal verification, AI planning, and many other domains

The key insight of CDCL is that conflicts aren't just dead ends to backtrack from, but opportunities to learn new constraints that can prune large portions of the search space. This learning mechanism transforms the nature of the search from a blind tree exploration to an intelligent navigation guided by past experience.
