"""
Examples Module for Default Theory

This module provides a collection of test cases for the unified semantics,
including both countermodels showing invalidity and theorems showing validity.

Usage:
------
This module can be run in two ways:

1. Command Line:
   ```bash
   model-checker path/to/this/examples.py
   ```

2. IDE (VSCodium/VSCode):
   - Open this file in VSCodium/VSCode
   - Use the "Run Python File" play button in the top-right corner
   - Or right-click in the editor and select "Run Python File"

Configuration:
-------------
The examples and theories to be run can be configured by:

1. Modifying which examples are run:
   - Edit the example_range dictionary
   - Comment/uncomment specific examples
   - Modify semantic_theories to change which theories to compare

2. To add new examples:
   - Define premises, conclusions, and settings
   - Follow the naming conventions:
     - Countermodels: CF_CM_*, ML_CM_*, CL_CM_*
     - Theorems: CF_TH_*, ML_TH_*, CL_TH_*
   - Add to example_range dictionary

Module Structure:
----------------
1. Imports:
   - System utilities (os, sys)
   - Local semantic definitions (Semantics, Proposition, ModelStructure)
   - Local operator definitions (default_operators)

2. Semantic Theory:
   - default_theory: Default semantic framework with components:
     * semantics: Core semantic class
     * proposition: Proposition handling
     * model: Model structure implementation
     * operators: Logical operators

3. Example Categories:
   a) Counterfactual Countermodels (CF_CM_*):
      - Tests for invalid counterfactual arguments
      - Includes antecedent strengthening, transitivity, contraposition
      - Complex examples like Sobel sequences
   
   b) Constitutive Logic Countermodels (CL_CM_*):
      - Tests for invalid constitutive arguments
      - Ground/essence operators and identity relations
   
   c) Counterfactual Theorems (CF_TH_*):
      - Tests for valid counterfactual arguments
      - Basic properties like identity and modus ponens
      - Modal interactions with necessity
   
   d) Constitutive Logic Theorems (CL_TH_*):
      - Tests for valid constitutive arguments
      - Relationships between ground, essence and identity

Example Format:
--------------
Each example is structured as a list: [premises, conclusions, settings]
- premises: List of formulas that serve as assumptions
- conclusions: List of formulas to be tested
- settings: Dictionary of specific settings for this example

Settings Options:
----------------
- N: Number of atomic propositions (default: 3)
- contingent: Whether to use contingent valuations
- disjoint: Whether to enforce disjoint valuations
- non_empty: Whether to enforce non-empty valuations
- non_null: Whether to enforce non-null valuations
- max_time: Maximum computation time in seconds
- iterate: Number of iterations for modal operators
- expectation: Expected result (True for countermodel found)

Notes:
------
- At least one semantic theory must be included in semantic_theories
- At least one example must be included in example_range
- Some examples may require adjusting the settings to produce good models

Help:
-----
More information can be found in the README.md for the default theory.
"""

##########################
### DEFINE THE IMPORTS ###
##########################

# Standard imports
import sys
import os

# Add current directory to path before importing modules
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from semantic import (
    Semantics,
    Proposition,
    ModelStructure,
)
from operators import default_operators

__all__ = [
    'general_settings',
    'default_theory',
    'semantic_theories',
    'example_range',
]

########################
### DEFAULT SETTINGS ###
########################

general_settings = {
    "print_constraints": False,
    "print_impossible": False,
    "print_z3": False,
    "save_output": False,
    "maximize": False,
}



####################################
### DEFINE THE SEMANTIC THEORIES ###
####################################

default_theory = {
    "semantics": Semantics,
    "proposition": Proposition,
    "model": ModelStructure,
    "operators": default_operators,
    # default theory does not require a translation dictionary for comparison
    # since the examples are stated in the language of the default theory
}

"""
INFO: With respect to adding semantic theories to compare.

The semantic.py module will have to be expanded to include definitions of the
following or else importing definitions from the theory_lib:
- AlternativeSemantics
- AlternativeProposition
- AlternativeStructure

The operators.py module will have to be expanded to include:
- alternative_operators

The translation between theories may then be specified here as indicated below:
- translation_dictionary


NOTE: Uncommnent below to add another theory to compare, changing names as desired.
"""

# translation_dictionary = {
#     "\\operatorA" : "\\operatorB",
# }
#
# imposition_theory = {
#     "semantics": AlternativeSemantics,
#     "proposition": AlternativeProposition,
#     "model": AlternativeStructure,
#     "operators": alternative_operators,
#     "dictionary": translation_dictionary,
# }


#####################
### COUNTERMODELS ###
#####################

# # CF_CM_0: COUNTERFACTUAL IMPORTATION
# CF_CM_0_premises = ['(A \\boxright (B \\boxright C))']
# CF_CM_0_conclusions = ['((A \\wedge B) \\boxright C)']
# CF_CM_0_settings = {
#     'N' : 6,
#     'contingent' : True,
#     'non_null' : True,
#     'non_empty' : True,
#     'disjoint' : False,
#     'max_time' : 10,
#     'iterate' : 1,
#     'expectation' : True,
# }
# CF_CM_0_example = [
#     CF_CM_0_premises,
#     CF_CM_0_conclusions,
#     CF_CM_0_settings,
# ]

# CF_CM_1: COUNTERFACTUAL ANTECEDENT STRENGTHENING
CF_CM_1_premises = ['\\neg A', '(A \\boxright C)']
CF_CM_1_conclusions = ['((A \\wedge B) \\boxright C)']
CF_CM_1_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_1_example = [
    CF_CM_1_premises,
    CF_CM_1_conclusions,
    CF_CM_1_settings,
]

# CF_CM_2: MIGHT COUNTERFACTUAL ANTECEDENT STRENGTHENING
CF_CM_2_premises = ['\\neg A', '(A \\diamondright C)']
CF_CM_2_conclusions = ['((A \\wedge B) \\diamondright C)']
CF_CM_2_settings = {
    'N' : 3,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 1,
    'iterate' : 5,
    'expectation' : True,
}
CF_CM_2_example = [
    CF_CM_2_premises,
    CF_CM_2_conclusions,
    CF_CM_2_settings,
]

# CF_CM_3: COUNTERFACTUAL ANTECEDENT STRENGTHENING WITH POSSIBILITY
CF_CM_3_premises = ['\\neg A', '(A \\boxright C)', '\\Diamond (A \\wedge B)']
CF_CM_3_conclusions = ['((A \\wedge B) \\boxright C)']
CF_CM_3_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_3_example = [
    CF_CM_3_premises,
    CF_CM_3_conclusions,
    CF_CM_3_settings,
]

# CF_CM_4: COUNTERFACTUAL ANTECEDENT STRENGTHENING WITH NEGATION
CF_CM_4_premises = ['\\neg A','(A \\boxright C)']
CF_CM_4_conclusions = ['((A \\wedge B) \\boxright C)']
CF_CM_4_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_4_example = [
    CF_CM_4_premises,
    CF_CM_4_conclusions,
    CF_CM_4_settings,
]

# CF_CM_5: COUNTERFACTUAL DOUBLE ANTECEDENT STRENGTHENING
CF_CM_5_premises = ['(A \\boxright C)','(B \\boxright C)']
CF_CM_5_conclusions = ['((A \\wedge B) \\boxright C)']
CF_CM_5_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_5_example = [
    CF_CM_5_premises,
    CF_CM_5_conclusions,
    CF_CM_5_settings,
]

# CF_CM_6: WEAKENED MONOTONICITY
CF_CM_6_premises = ['\\neg A', '(A \\boxright B)','(A \\boxright C)']
CF_CM_6_conclusions = ['((A \\wedge B) \\boxright C)']
CF_CM_6_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 300,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_6_example = [
    CF_CM_6_premises,
    CF_CM_6_conclusions,
    CF_CM_6_settings,
]
"""
Only finds a countermodel if A and B are not disjoint. I'm not sure how I feel about this. On the Lewis semantics, it is clearly a theorem. Also, for up to (at least) N=6, 'disjoint' must be True in order for it to find a countermodel (al other settings are True). So clearly something funky with ground is going on. 

Here is the countermodel for N=4. Below is an interpretation. The interpretation is relatively buyable. I'm less skeptical than when I originally saw that this was an inference for which there was a countermodel. 
========================================
State Space:
  #b0000 = □
  #b0001 = a
  #b0010 = b
  #b0100 = c
  #b0101 = a.c (world)
  #b1000 = d
  #b1001 = a.d (world)
  #b1010 = b.d (world)

The evaluation world is: a.c

INTERPRETED PREMISES:

1.  |\neg A| = < {c}, {d} >  (True in a.c)
      |A| = < {d}, {c} >  (False in a.c)

2.  |(A \boxright B)| = < {□}, ∅ >  (True in a.c)
      |A| = < {d}, {c} >  (False in a.c)
      |A|-alternatives to a.c = {a.d}
        |B| = < {b, b.d, d}, {a.c} >  (True in a.d)

3.  |(A \boxright C)| = < {□}, ∅ >  (True in a.c)
      |A| = < {d}, {c} >  (False in a.c)
      |A|-alternatives to a.c = {a.d}
        |C| = < {a.c, a.d}, {b.d} >  (True in a.d)

INTERPRETED CONCLUSION:

4.  |((A \wedge B) \boxright C)| = < ∅, {□} >  (False in a.c)
      |(A \wedge B)| = < {b.d, d}, {a.c, c} >  (False in a.c)
        |A| = < {d}, {c} >  (False in a.c)
        |B| = < {b, b.d, d}, {a.c} >  (False in a.c)
      |(A \wedge B)|-alternatives to a.c = {a.d, b.d}
        |C| = < {a.c, a.d}, {b.d} >  (True in a.d)
        |C| = < {a.c, a.d}, {b.d} >  (False in b.d)

Also, I provide an interpretation here (inspired by an abnormally sunny April day with a great view from Hayden of Memorial Dr. and Boston): 
a = state of it being sunny
b = state of it raining
c = state of the ground being dry
d = state of the ground being wet
A = The ground is wet
B = The weather is typical April weather
C = The weather is nice
In the actual world is is sunny and the ground is dry (a.c). (That is not typical April weather—normally it's raining or the ground is wet in April—and accordingly B is false at a.c.) We have alternative worlds where the ground is wet and it is sunny (a.d) and where the ground is wet and the it is raining (b.d). It is intuitively true that if the ground were wet, the weather would be nice—that's the world minimally different from this one where the ground is wet and it is sunny, which is all in all nice weather. So A \\boxright B is true. It is also true that if the ground were wet it would be April weather, since that is a hallmark of April weather—that it just rained and now is sunny. So A \\boxright C is true. However it is not as clearly true that if the ground were wet and it were typical April weather, it would be nice weather. Since by putting in ``typical April weather'' into the antecedent, we feel more forced to consider worlds where it rains. 

The disjointness is crucial, as in the uninterpreted countermodel: what grounds the ground being wet is a subset of what grounds it being April weather. So (A \\wedge B) is basically just B. And looking for a countermodel to B \\boxright C is much easier than for the conjunction. 

Lewis has nothing to say about this! (Besides maybe some pragmatic thing.) Or he could argue that the closest raining world is just as close as the closest non-raining world. But then A \\boxright C would be false. So yeah, nothing. 

Unsure of how a dynamic account based on a Lewis semantics would explain this. I'm not sure it can. 


It found a model for N=7! (139 seconds) It is below. Have not interpreted it. 
========================================
State Space:
  #b0000000 = □
  #b0000001 = a
  #b0000010 = b
  #b0000011 = a.b
  #b0000100 = c
  #b0001000 = d
  #b0001001 = a.d
  #b0001010 = b.d
  #b0001011 = a.b.d
  #b0001100 = c.d
  #b0010000 = e
  #b0010001 = a.e
  #b0010010 = b.e
  #b0010011 = a.b.e
  #b0011000 = d.e
  #b0011010 = b.d.e
  #b0100000 = f
  #b0100100 = c.f
  #b0101000 = d.f
  #b0101100 = c.d.f (world)
  #b1000000 = g
  #b1000001 = a.g
  #b1000010 = b.g
  #b1000011 = a.b.g
  #b1001000 = d.g
  #b1001001 = a.d.g
  #b1001010 = b.d.g
  #b1001011 = a.b.d.g (world)
  #b1010000 = e.g
  #b1010001 = a.e.g
  #b1010010 = b.e.g
  #b1010011 = a.b.e.g (world)
  #b1011000 = d.e.g
  #b1011010 = b.d.e.g (world)
  #b1100000 = f.g
  #b1101000 = d.f.g (world)

The evaluation world is: c.d.f

INTERPRETED PREMISES:

1.  |\neg A| = < {c}, {g} >  (True in c.d.f)
      |A| = < {g}, {c} >  (False in c.d.f)

2.  |(A \boxright B)| = < {□}, ∅ >  (True in c.d.f)
      |A| = < {g}, {c} >  (False in c.d.f)
      |A|-alternatives to c.d.f = {d.f.g}
        |B| = < {a.d, d, d.e}, {a.e} >  (True in d.f.g)

3.  |(A \boxright C)| = < {□}, ∅ >  (True in c.d.f)
      |A| = < {g}, {c} >  (False in c.d.f)
      |A|-alternatives to c.d.f = {d.f.g}
        |C| = < {f}, {b} >  (True in d.f.g)

INTERPRETED CONCLUSION:

4.  |((A \wedge B) \boxright C)| = < ∅, {□} >  (False in c.d.f)
      |(A \wedge B)| = < {a.d.g, d.e.g, d.g}, {a.e, c} >  (False in c.d.f)
        |A| = < {g}, {c} >  (False in c.d.f)
        |B| = < {a.d, d, d.e}, {a.e} >  (True in c.d.f)
      |(A \wedge B)|-alternatives to c.d.f = {a.b.d.g, b.d.e.g, d.f.g}
        |C| = < {f}, {b} >  (True in d.f.g)
        |C| = < {f}, {b} >  (False in a.b.d.g)
        |C| = < {f}, {b} >  (False in b.d.e.g)
"""

# CF_CM_7: COUNTERFACTUAL CONTRAPOSITION
CF_CM_7_premises = ['(A \\boxright B)']
CF_CM_7_conclusions = ['(\\neg B \\boxright \\neg A)']
CF_CM_7_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_7_example = [
    CF_CM_7_premises,
    CF_CM_7_conclusions,
    CF_CM_7_settings,
]

# CF_CM_8: COUNTERFACTUAL CONTRAPOSITION WITH NEGATION
CF_CM_8_premises = ['\\neg B','(A \\boxright B)']
CF_CM_8_conclusions = ['(\\neg B \\boxright \\neg A)']
CF_CM_8_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_8_example = [
    CF_CM_8_premises,
    CF_CM_8_conclusions,
    CF_CM_8_settings,
]

# CF_CM_9: COUNTERFACTUAL CONTRAPOSITION WITH TWO NEGATIONS
CF_CM_9_premises = ['\\neg A','\\neg B','(A \\boxright B)']
CF_CM_9_conclusions = ['(\\neg B \\boxright \\neg A)']
CF_CM_9_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_9_example = [
    CF_CM_9_premises,
    CF_CM_9_conclusions,
    CF_CM_9_settings,
]

# CF_CM_10: TRANSITIVITY
CF_CM_10_premises = ['(A \\boxright B)','(B \\boxright C)']
CF_CM_10_conclusions = ['(A \\boxright C)']
CF_CM_10_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_10_example = [
    CF_CM_10_premises,
    CF_CM_10_conclusions,
    CF_CM_10_settings,
]

# CF_CM_11: COUNTERFACTUAL TRANSITIVITY WITH NEGATION
CF_CM_11_premises = ['\\neg A','(A \\boxright B)','(B \\boxright C)']
CF_CM_11_conclusions = ['(A \\boxright C)']
CF_CM_11_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_11_example = [
    CF_CM_11_premises,
    CF_CM_11_conclusions,
    CF_CM_11_settings,
]

# CF_CM_12: COUNTERFACTUAL TRANSITIVITY WITH TWO NEGATIONS
CF_CM_12_premises = ['\\neg A','\\neg B','(A \\boxright B)','(B \\boxright C)']
CF_CM_12_conclusions = ['(A \\boxright C)']
CF_CM_12_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_12_example = [
    CF_CM_12_premises,
    CF_CM_12_conclusions,
    CF_CM_12_settings,
]

# CF_CM_13: SOBEL SEQUENCE
CF_CM_13_premises = [
    '(A \\boxright X)',
    '\\neg ((A \\wedge B) \\boxright X)',
    '(((A \\wedge B) \\wedge C) \\boxright X)',
    '\\neg ((((A \\wedge B) \\wedge C) \\wedge D) \\boxright X)',
    '(((((A \\wedge B) \\wedge C) \\wedge D) \\wedge E) \\boxright X)',
    '\\neg ((((((A \\wedge B) \\wedge C) \\wedge D) \\wedge E) \\wedge F) \\boxright X)',
    '(((((((A \\wedge B) \\wedge C) \\wedge D) \\wedge E) \\wedge F) \\wedge G) \\boxright X)',
]
CF_CM_13_conclusions = []
CF_CM_13_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 2,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_13_example = [
    CF_CM_13_premises,
    CF_CM_13_conclusions,
    CF_CM_13_settings,
]

# CF_CM_14: SOBEL SEQUENCE WITH POSSIBILITY
CF_CM_14_premises = [
    '\\Diamond A',
    '(A \\boxright X)',
    '\\Diamond (A \\wedge B)',
    '\\neg ((A \\wedge B) \\boxright X)',
    '\\Diamond ((A \\wedge B) \\wedge C)',
    '(((A \\wedge B) \\wedge C) \\boxright X)',
    '\\Diamond (((A \\wedge B) \\wedge C) \\wedge D)',
    '\\neg ((((A \\wedge B) \\wedge C) \\wedge D) \\boxright X)',
    '\\Diamond ((((A \\wedge B) \\wedge C) \\wedge D) \\wedge E)',
    '(((((A \\wedge B) \\wedge C) \\wedge D) \\wedge E) \\boxright X)',
    '\\Diamond (((((A \\wedge B) \\wedge C) \\wedge D) \\wedge E) \\wedge F)',
    '\\neg ((((((A \\wedge B) \\wedge C) \\wedge D) \\wedge E) \\wedge F) \\boxright X)',
    '\\Diamond ((((((A \\wedge B) \\wedge C) \\wedge D) \\wedge E) \\wedge F) \\wedge G)',
    '(((((((A \\wedge B) \\wedge C) \\wedge D) \\wedge E) \\wedge F) \\wedge G) \\boxright X)',
]
CF_CM_14_conclusions = []
CF_CM_14_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 2,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_14_example = [
    CF_CM_14_premises,
    CF_CM_14_conclusions,
    CF_CM_14_settings,
]

# CF_CM_15: COUNTERFACTUAL EXCLUDED MIDDLE
CF_CM_15_premises = ['\\neg A']
CF_CM_15_conclusions = ['(A \\boxright B)','(A \\boxright \\neg B)']
CF_CM_15_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 2,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_15_example = [
    CF_CM_15_premises,
    CF_CM_15_conclusions,
    CF_CM_15_settings,
]

# CF_CM_16: SIMPLIFICATION OF DISJUNCTIVE CONSEQUENT
CF_CM_16_premises = ['\\neg A','(A \\boxright (B \\vee C))']
CF_CM_16_conclusions = ['(A \\boxright B)','(A \\boxright C)']
CF_CM_16_settings = {
    'N' : 3,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 2,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_16_example = [
    CF_CM_16_premises,
    CF_CM_16_conclusions,
    CF_CM_16_settings,
]

# CF_CM_17: INTRODUCTION OF DISJUNCTIVE ANTECEDENT
CF_CM_17_premises = ['(A \\boxright C)','(B \\boxright C)']
CF_CM_17_conclusions = ['((A \\vee B) \\boxright C)']
CF_CM_17_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 2,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_17_example = [
    CF_CM_17_premises,
    CF_CM_17_conclusions,
    CF_CM_17_settings,
]
"""
This countermodel boils down to the semantics of \\vee in the hyperintensional semantics. Consider a world where one and exactly one of two switches, Left and Right, must be flipped on for a light to turn on. It is equally likely that Left turns on and Right doesn't, that Right does and Left doesn't, or that both do. If both do, then the light does not go on. Thus we have a countermodel with A = Left is flipped on, B = Right is flipped on, and C = the light turns on, while it is true that if A then C and if B then C, it is not true that if A or B then C, since if A and B are both true then C would not be true. 

REVISION: I think this inference is also invalid on a Lewis-Stalnaker semantics of CFs. This would make sense, given that the locus of the countermodel in the hyperintensional semantics is in the semantics for \\vee, which mirror those of \\vee in classical logic. The point below about natural language "or" stands (a question independent of any semantics of CFs) but I leave the rest just for reference. 

I believe this inference is valid in a Lewis-Stalnaker semantics of counterfactuals. I'm not really sure how I feel about this example. Since the only way to get this counterexample on the hyperintensional semantics is through some sneaky disjunction facts like this, I feel like whatever qualms I have about it boil down to whatever qualms I have about natural language "or" being regimented as \\vee. If we say instead that if Left were flipped and/or if Right were flipped then the light would go on (explicitly saying the inclusive aspect of \\vee), a countermodel like this is desirable. I think Lewis-Stalnaker would be forced to have some pragmatic account for it ("well, now that you said 'and', you got me thinking about A \\wedge B worlds, and now it doesn't hold, but of course \\vee entails these A \\wedge B worlds so any reason for the invalidity of inference has to be on pragmatic grounds"), which is a point in favor of the hyperintensional account, since such a pragmatic excuse feels a bit lame because the and aspect of or is implied by or f you're committed to "or" being \\vee. 
========================================
State Space:
  #b0000 = □
  #b0001 = a
  #b0010 = b
  #b0011 = a.b (world)
  #b0100 = c
  #b0101 = a.c (world)
  #b0110 = b.c (world)
  #b1000 = d
  #b1001 = a.d (world)
  #b1010 = b.d (world)

The evaluation world is: a.c

INTERPRETED PREMISES:

1.  |(A \boxright C)| = < {□}, ∅ >  (True in a.c)
      |A| = < {a.b, a.d, b, b.c}, {a.c} >  (False in a.c)
      |A|-alternatives to a.c = {a.b, a.d, b.c}
        |C| = < {a.b, a.c, a.d, c}, {b.d} >  (True in a.d)
        |C| = < {a.b, a.c, a.d, c}, {b.d} >  (True in b.c)
        |C| = < {a.b, a.c, a.d, c}, {b.d} >  (True in a.b)

2.  |(B \boxright C)| = < {□}, ∅ >  (True in a.c)
      |B| = < {a, a.b, a.c, a.d, d}, {b.c} >  (True in a.c)
      |B|-alternatives to a.c = {a.b, a.c, a.d}
        |C| = < {a.b, a.c, a.d, c}, {b.d} >  (True in a.d)
        |C| = < {a.b, a.c, a.d, c}, {b.d} >  (True in a.b)
        |C| = < {a.b, a.c, a.d, c}, {b.d} >  (True in a.c)

INTERPRETED CONCLUSION:

3.  |((A \vee B) \boxright C)| = < ∅, {□} >  (False in a.c)
      |(A \vee B)| = < {a, a.b, a.c, a.d, b, b.c, b.d, d}, ∅ >  (True in a.c)
        |A| = < {a.b, a.d, b, b.c}, {a.c} >  (False in a.c)
        |B| = < {a, a.b, a.c, a.d, d}, {b.c} >  (True in a.c)
      |(A \vee B)| = < {a, a.b, a.c, a.d, b, b.c, b.d, d}, ∅ >  (True in a.c)
        |A| = < {a.b, a.d, b, b.c}, {a.c} >  (False in a.c)
        |B| = < {a, a.b, a.c, a.d, d}, {b.c} >  (True in a.c)
      |(A \vee B)|-alternatives to a.c = {a.b, a.c, a.d, b.c, b.d}
        |C| = < {a.b, a.c, a.d, c}, {b.d} >  (True in a.d)
        |C| = < {a.b, a.c, a.d, c}, {b.d} >  (True in b.c)
        |C| = < {a.b, a.c, a.d, c}, {b.d} >  (False in b.d)
        |C| = < {a.b, a.c, a.d, c}, {b.d} >  (True in a.b)
        |C| = < {a.b, a.c, a.d, c}, {b.d} >  (True in a.c)
"""

# CF_CM_18: MUST FACTIVITY
CF_CM_18_premises = ['A','B']
CF_CM_18_conclusions = ['(A \\boxright B)']
CF_CM_18_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 2,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_18_example = [
    CF_CM_18_premises,
    CF_CM_18_conclusions,
    CF_CM_18_settings,
]

# CF_CM_19: COUNTERFACTUAL EXPORTATION
CF_CM_19_premises = ['((A \\wedge B) \\boxright C)']
CF_CM_19_conclusions = ['(A \\boxright (B \\boxright C))']
CF_CM_19_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 3,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_19_example = [
    CF_CM_19_premises,
    CF_CM_19_conclusions,
    CF_CM_19_settings,
]

# CF_CM_20: COUNTERFACTUAL EXPORTATION WITH POSSIBILITY
CF_CM_20_premises = ['((A \\wedge B) \\boxright C)','\\Diamond (A \\wedge B)']
CF_CM_20_conclusions = ['(A \\boxright (B \\boxright C))']
CF_CM_20_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 3,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_20_example = [
    CF_CM_20_premises,
    CF_CM_20_conclusions,
    CF_CM_20_settings,
]

# CF_CM_21:
CF_CM_21_premises = ['\\neg A','\\neg (A \\boxright B)']
CF_CM_21_conclusions = ['(A \\boxright \\neg B)']
CF_CM_21_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 2,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_21_example = [
    CF_CM_21_premises,
    CF_CM_21_conclusions,
    CF_CM_21_settings,
]



##############################
### CONSTITUTIVE OPERATORS ###
##############################

# ML_CM_1: 
ML_CM_1_premises = ['\\Box (A \\vee B)']
ML_CM_1_conclusions = ['\\Box A \\vee \\Box B']
ML_CM_1_settings = {
    'N' : 3,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : True,
}
ML_CM_1_example = [
    ML_CM_1_premises,
    ML_CM_1_conclusions,
    ML_CM_1_settings,
]



##############################
### CONSTITUTIVE OPERATORS ###
##############################

# CL_CM_3: GROUND CONJUNCTION SUPPLEMENTATION
CL_CM_3_premises = ['(A \\leq B)','(C \\leq D)']
CL_CM_3_conclusions = ['((A \\wedge C) \\leq (B \\wedge D))']
CL_CM_3_settings = {
    'N' : 3,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : True,
}
CL_CM_3_example = [
    CL_CM_3_premises,
    CL_CM_3_conclusions,
    CL_CM_3_settings,
]

# CL_CM_4: ESSENCE DISJUNCTION SUPPLEMENTATION
CL_CM_4_premises = ['(A \\sqsubseteq B)','(C \\sqsubseteq D)']
CL_CM_4_conclusions = ['((A \\vee C) \\sqsubseteq (B \\vee D))']
CL_CM_4_settings = {
    'N' : 3,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : True,
}
CL_CM_4_example = [
    CL_CM_4_premises,
    CL_CM_4_conclusions,
    CL_CM_4_settings,
]

# CL_CM_5: IDENTITY ABSORPTION: DISJUNCTION OVER CONJUNCTION
CL_CM_5_premises = []
CL_CM_5_conclusions = ['(A \\equiv (A \\vee (A \\wedge B)))']
CL_CM_5_settings = {
    'N' : 3,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : True,
}
CL_CM_5_example = [
    CL_CM_5_premises,
    CL_CM_5_conclusions,
    CL_CM_5_settings,
]

# CL_CM_6: IDENTITY ABSORPTION: DISJUNCTION OVER CONJUNCTION
CL_CM_6_premises = []
CL_CM_6_conclusions = ['(A \\equiv (A \\wedge (A \\vee B)))']
CL_CM_6_settings = {
    'N' : 3,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : True,
}
CL_CM_6_example = [
    CL_CM_6_premises,
    CL_CM_6_conclusions,
    CL_CM_6_settings,
]

# CL_CM_10: IDENTITY DISTRIBUTION
CL_CM_10_premises = []
CL_CM_10_conclusions = ['((A \\vee (B \\wedge C)) \\equiv ((A \\vee B) \\wedge (A \\vee C)))']
CL_CM_10_settings = {
    'N' : 3,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : True,
}
CL_CM_10_example = [
    CL_CM_10_premises,
    CL_CM_10_conclusions,
    CL_CM_10_settings,
]



############################
### LOGICAL CONSEQUENCES ###
############################

# CF_TH_1: COUNTERFACTUAL IDENTITY
CF_TH_1_premises = []
CF_TH_1_conclusions = ['(A \\boxright A)']
CF_TH_1_settings = {
    'N' : 2,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CF_TH_1_example = [
    CF_TH_1_premises,
    CF_TH_1_conclusions,
    CF_TH_1_settings,
]

# CF_TH_2: COUNTERFACTUAL MODUS PONENS
CF_TH_2_premises = ['A','(A \\boxright B)']
CF_TH_2_conclusions = ['B']
CF_TH_2_settings = {
    'N' : 4,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CF_TH_2_example = [
    CF_TH_2_premises,
    CF_TH_2_conclusions,
    CF_TH_2_settings,
]

# CF_TH_3: WEAKENED TRANSITIVITY
CF_TH_3_premises = ['(A \\boxright B)','((A \\wedge B) \\boxright C)']
CF_TH_3_conclusions = ['(A \\boxright C)']
CF_TH_3_settings = {
    'N' : 4,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CF_TH_3_example = [
    CF_TH_3_premises,
    CF_TH_3_conclusions,
    CF_TH_3_settings,
]

# CF_TH_4: ANTECEDENT DISJUNCTION TO CONJUNCTION
CF_TH_4_premises = ['((A \\vee B) \\boxright C)']
CF_TH_4_conclusions = ['((A \\wedge B) \\boxright C)']
CF_TH_4_settings = {
    'N' : 4,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CF_TH_4_example = [
    CF_TH_4_premises,
    CF_TH_4_conclusions,
    CF_TH_4_settings,
]

# CF_TH_5: SIMPLIFICATION OF DISJUNCTIVE ANTECEDENT
CF_TH_5_premises = ['((A \\vee B) \\boxright C)']
CF_TH_5_conclusions = ['(A \\boxright C)']
CF_TH_5_settings = {
    'N' : 4,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CF_TH_5_example = [
    CF_TH_5_premises,
    CF_TH_5_conclusions,
    CF_TH_5_settings,
]

# CF_TH_6: DOUBLE SIMPLIFICATION OF DISJUNCTIVE ANTECEDENT
CF_TH_6_premises = ['((A \\vee B) \\boxright C)']
CF_TH_6_conclusions = ['((A \\boxright C) \\wedge (B \\boxright C))']
CF_TH_6_settings = {
    'N' : 4,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CF_TH_6_example = [
    CF_TH_6_premises,
    CF_TH_6_conclusions,
    CF_TH_6_settings,
]

# CF_TH_7:
CF_TH_7_premises = [
    '(A \\boxright C)',
    '(B \\boxright C)',
    '((A \\wedge B) \\boxright C)',
]
CF_TH_7_conclusions = ['((A \\vee B) \\boxright C)']
CF_TH_7_settings = {
    'N' : 4,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CF_TH_7_example = [
    CF_TH_7_premises,
    CF_TH_7_conclusions,
    CF_TH_7_settings,
]

# CF_TH_8:
CF_TH_8_premises = ['(A \\boxright (B \\wedge C))']
CF_TH_8_conclusions = ['(A \\boxright B)']
CF_TH_8_settings = {
    'N' : 4,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CF_TH_8_example = [
    CF_TH_8_premises,
    CF_TH_8_conclusions,
    CF_TH_8_settings,
]

# CF_TH_9:
CF_TH_9_premises = ['(A \\boxright B)','(A \\boxright C)']
CF_TH_9_conclusions = ['(A \\boxright (B \\wedge C))']
CF_TH_9_settings = {
    'N' : 4,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CF_TH_9_example = [
    CF_TH_9_premises,
    CF_TH_9_conclusions,
    CF_TH_9_settings,
]

# CF_TH_10: MIGHT FACTIVITY
CF_TH_10_premises = ['A','B']
CF_TH_10_conclusions = ['(A \\diamondright B)']
CF_TH_10_settings = {
    'N' : 4,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CF_TH_10_example = [
    CF_TH_10_premises,
    CF_TH_10_conclusions,
    CF_TH_10_settings,
]

# CF_TH_11: DEFINITION OF NEC
CF_TH_11_premises = ['\\Box A']
CF_TH_11_conclusions = ['(\\top \\boxright A)']
CF_TH_11_settings = {
    'N' : 3,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : True,
    'non_null' : True,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CF_TH_11_example = [
    CF_TH_11_premises,
    CF_TH_11_conclusions,
    CF_TH_11_settings,
]

# CF_TH_12: DEFINITION OF NEC
CF_TH_12_premises = ['(\\neg A \\boxright \\bot)']
CF_TH_12_conclusions = ['(\\top \\boxright A)']
CF_TH_12_settings = {
    'N' : 3,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CF_TH_12_example = [
    CF_TH_12_premises,
    CF_TH_12_conclusions,
    CF_TH_12_settings,
]



### CONSTITUTIVE OPERATORS ###

# CL_TH_1: GROUND TO ESSENCE
CL_TH_1_premises = ['(A \\leq B)']
CL_TH_1_conclusions = ['(\\neg A \\sqsubseteq \\neg B)']
CL_TH_1_settings = {
    'N' : 4,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CL_TH_1_example = [
    CL_TH_1_premises,
    CL_TH_1_conclusions,
    CL_TH_1_settings,
]

# CL_TH_2: ESSENCE TO GROUND 
CL_TH_2_premises = ['(A \\sqsubseteq B)']
CL_TH_2_conclusions = ['(\\neg A \\leq \\neg B)']
CL_TH_2_settings = {
    'N' : 4,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CL_TH_2_example = [
    CL_TH_2_premises,
    CL_TH_2_conclusions,
    CL_TH_2_settings,
]

# CL_TH_3: ESSENCE TO IDENTITY
CL_TH_3_premises = ['(A \\sqsubseteq B)']
CL_TH_3_conclusions = ['((A \\wedge B) \\equiv B)']
CL_TH_3_settings = {
    'N' : 4,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CL_TH_3_example = [
    CL_TH_3_premises,
    CL_TH_3_conclusions,
    CL_TH_3_settings,
]

# CL_TH_4: IDENTITY TO ESSENCE 
CL_TH_4_premises = ['((A \\wedge B) \\equiv B)']
CL_TH_4_conclusions = ['(A \\sqsubseteq B)']
CL_TH_4_settings = {
    'N' : 4,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CL_TH_4_example = [
    CL_TH_4_premises,
    CL_TH_4_conclusions,
    CL_TH_4_settings,
]

# CL_TH_5: GROUND TO IDENTITY
CL_TH_5_premises = ['(A \\leq B)']
CL_TH_5_conclusions = ['((A \\vee B) \\equiv B)']
CL_TH_5_settings = {
    'N' : 4,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CL_TH_5_example = [
    CL_TH_5_premises,
    CL_TH_5_conclusions,
    CL_TH_5_settings,
]

# CL_TH_6: IDENTITY TO GROUND 
CL_TH_6_premises = ['((A \\vee B) \\equiv B)']
CL_TH_6_conclusions = ['(A \\leq B)']
CL_TH_6_settings = {
    'N' : 4,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CL_TH_6_example = [
    CL_TH_6_premises,
    CL_TH_6_conclusions,
    CL_TH_6_settings,
]

# CL_TH_7: NEGATION TRANSPARENCY
CL_TH_7_premises = ['(A \\equiv B)']
CL_TH_7_conclusions = ['(\\neg A \\equiv \\neg B)']
CL_TH_7_settings = {
    'N' : 4,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CL_TH_7_example = [
    CL_TH_7_premises,
    CL_TH_7_conclusions,
    CL_TH_7_settings,
]

# CL_TH_8: REVERSE NEGATION TRANSPARENCY
CL_TH_8_premises = ['(\\neg A \\equiv \\neg B)']
CL_TH_8_conclusions = ['(A \\equiv B)']
CL_TH_8_settings = {
    'N' : 4,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
CL_TH_8_example = [
    CL_TH_8_premises,
    CL_TH_8_conclusions,
    CL_TH_8_settings,
]


##########################################
############## NEW EXAMPLES ##############
##########################################



# CF_CM_19: COUNTERFACTUAL EXPORTATION WITH POSSILIBITY
CF_CM_19_B_premises = ['((A \\wedge B) \\boxright C)', '\\Diamond (A \\wedge B)']
CF_CM_19_B_conclusions = ['(A \\boxright (B \\boxright C))']
CF_CM_19_B_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 3,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_19_B_example = [
    CF_CM_19_B_premises,
    CF_CM_19_B_conclusions,
    CF_CM_19_B_settings,
]
"""
This example is motivated by the fact that the model provided for CF_CM_19 originally has A \\wedge B as necessarily false, so the premise is quite trivially fulfilled. The model-checker finds a countermodel, thus showing interesting countermodels (where A \\wedge B is possible) exist to CF Exportation. 

Context: Suppose Mary is very smart and good at test taking; John unforunately not. In the actual world, Mary finishes the test and John does not. 

Interpretation: A = John finishes the test, B = Mary finishes the test, C = the professor is happy. 
If John and Mary finish the test, the professor would be happy—of course this is true. However it is not true that if John were to finish the test, then if Mary were to finish the test the professor would be happy, because—from the point of view of a world where John does finish the test—it is equally a minimal departure from (that relative) actuality that John does not finish the test (and thus the professor is not happy) than if he does (i.e. we stay in the embedded world of evaluation). 

I think this entailment is valid under a classical Lewis-Stalnaker semantics of counterfactuals, but is invalid (because this countermodel also exists for it) for a dynamic semantics of counterfactuals (e.g. von Fintel 2001). A proper next question to ask would be whether this is a logically invalid inference (as this semantics holds it to be) or a dynamically (Strawson-)invalid inference (as von Fintel's semantics would hold it to be). In my intuition, the clearest immediate justification (for this particular countermodel where we bounce back to the actual world) for it is that it is dynamically invalid, since the salience of the actual world (and thus the conclusion's falsity) is due to our being in the actual world, not due to the actual world being an alternative for the embedded CF in the conclusion. This may mean that I need to look for a better interpretation of this countermodel (I think all interps will have this issue though), or look for another countermodel. 
========================================
State Space:
  #b0000 = □
  #b0001 = a
  #b0010 = b (world)
  #b0100 = c (world)
  #b1000 = d
  #b1001 = a.d (world)

The evaluation world is: b

INTERPRETED PREMISES:

1.  |((A \wedge B) \boxright C)| = < {□}, ∅ >  (True in b)
      |(A \wedge B)| = < {a.d}, {b, c} >  (False in b)
        |A| = < {a, a.d}, {b, c} >  (False in b)
        |B| = < {b, d}, {c} >  (True in b)
      |(A \wedge B)|-alternatives to b = {a.d}
        |C| = < {a, c}, {b} >  (True in a.d)

2.  |\Diamond (A \wedge B)| = < {□}, ∅ >  (True in b)
      |(A \wedge B)| = < {a.d}, {b, c} >  (False in b)
        |A| = < {a, a.d}, {b, c} >  (False in b)
        |B| = < {b, d}, {c} >  (True in b)
      |(A \wedge B)| = < {a.d}, {b, c} >  (False in c)
        |A| = < {a, a.d}, {b, c} >  (False in c)
        |B| = < {b, d}, {c} >  (False in c)
      |(A \wedge B)| = < {a.d}, {b, c} >  (True in a.d)
        |A| = < {a, a.d}, {b, c} >  (True in a.d)
        |B| = < {b, d}, {c} >  (True in a.d)

INTERPRETED CONCLUSION:

3.  |(A \boxright (B \boxright C))| = < ∅, {□} >  (False in b)
      |A| = < {a, a.d}, {b, c} >  (False in b)
      |A|-alternatives to b = {a.d}
        |(B \boxright C)| = < ∅, {□} >  (False in a.d)
          |B| = < {b, d}, {c} >  (True in a.d)
            |B|-alternatives to a.d = {a.d, b}
              |C| = < {a, c}, {b} >  (True in a.d)
              |C| = < {a, c}, {b} >  (False in b)

Total Run Time: 6.5011 seconds
"""


EQUIV_TEST_1_premises = ['(\\CFBox A \\leftrightarrow \\Box A)']
EQUIV_TEST_1_conclusions = []
EQUIV_TEST_1_settings = {
    'N' : 8,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 3,
    'iterate' : 1,
    'expectation' : True,
}
EQUIV_TEST_1_example = [
    EQUIV_TEST_1_premises,
    EQUIV_TEST_1_conclusions,
    EQUIV_TEST_1_settings,
]
"""
Max N: 7. Though I think the unit is not seconds (not even minutes—it timed out after like 10 mins)
"""


EQUIV_TEST_2_premises = ['(\\CFDiamond A \\leftrightarrow \\neg \\CFBox \\neg A)']
EQUIV_TEST_2_conclusions = []
EQUIV_TEST_2_settings = {
    'N' : 7,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 3,
    'iterate' : 1,
    'expectation' : True,
}
EQUIV_TEST_2_example = [
    EQUIV_TEST_2_premises,
    EQUIV_TEST_2_conclusions,
    EQUIV_TEST_2_settings,
]
"""
Max N: didn't time out
The significance of this being valid is that we can now define all of a classical S5 modal logic within this logic for counterfactuals. 
"""


#########################################
### SPECIFY EXAMPLES FOR UNIT TESTING ###
#########################################

# NOTE: these are provided here for unit testing in /test/test_default.py
test_example_range = {
    # Counterfactual Countermodels
    "CF_CM_1" : CF_CM_1_example,
    "CF_CM_2" : CF_CM_2_example,
    "CF_CM_3" : CF_CM_3_example,
    "CF_CM_4" : CF_CM_4_example,
    "CF_CM_5" : CF_CM_5_example,
    "CF_CM_6" : CF_CM_6_example,
    "CF_CM_7" : CF_CM_7_example,
    "CF_CM_8" : CF_CM_8_example,
    "CF_CM_9" : CF_CM_9_example,
    "CF_CM_10" : CF_CM_10_example,
    "CF_CM_11" : CF_CM_11_example,
    "CF_CM_12" : CF_CM_12_example,
    "CF_CM_13" : CF_CM_13_example,
    "CF_CM_14" : CF_CM_14_example,
    "CF_CM_15" : CF_CM_15_example,
    "CF_CM_16" : CF_CM_16_example,
    "CF_CM_17" : CF_CM_17_example,
    "CF_CM_18" : CF_CM_18_example,
    "CF_CM_19" : CF_CM_19_example,
    "CF_CM_20" : CF_CM_20_example,
    "CF_CM_21" : CF_CM_21_example,

    # Modal Countermodels
    "ML_CM_1" : ML_CM_1_example,

    # Counterfactual Theorems
    "CF_TH_1" : CF_TH_1_example,
    "CF_TH_2" : CF_TH_2_example,
    "CF_TH_3" : CF_TH_3_example,
    "CF_TH_4" : CF_TH_4_example,
    "CF_TH_5" : CF_TH_5_example,
    "CF_TH_6" : CF_TH_6_example,
    "CF_TH_7" : CF_TH_7_example,
    "CF_TH_8" : CF_TH_8_example,
    "CF_TH_9" : CF_TH_9_example,
    "CF_TH_10" : CF_TH_10_example,
    "CF_TH_11" : CF_TH_11_example,
    "CF_TH_12" : CF_TH_12_example,

    # Constitutive Theorems
    "CL_TH_1" : CL_TH_1_example,
    "CL_TH_2" : CL_TH_2_example,
    "CL_TH_3" : CL_TH_3_example,
    "CL_TH_4" : CL_TH_4_example,
    "CL_TH_5" : CL_TH_5_example,
    "CL_TH_6" : CL_TH_6_example,
    "CL_TH_7" : CL_TH_7_example,
    "CL_TH_8" : CL_TH_8_example,
}

# DA_TO_CA: DISJUNCTIVE TO CONJUNCTIVE ANTECEDENT
DA_TO_CA_premises = ['((A \\vee B) \\boxright C)', 
                        #  '\\neg ((A \\wedge B) \\boxright C)',
                        #  '\\Diamond (A \\wedge B)',
                         ]
DA_TO_CA_conclusions = [
                            # '((A \\boxright C) \\wedge (B \\boxright C))',
                            # '\\neg ((A \\wedge B) \\boxright C)',
                            '((A \\wedge B) \\boxright C)',
                            ]
DA_TO_CA_settings = {
    'N' : 6,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 300,
    'iterate' : 1,
    'expectation' : False,
}
DA_TO_CA_example = [
    DA_TO_CA_premises,
    DA_TO_CA_conclusions,
    DA_TO_CA_settings,
]
"""
There is no countermodel up to 6 states. Not sure how I feel about this. 
"""


###############################################
### DEFINE EXAMPLES AND THEORIES TO COMPUTE ###
###############################################

# NOTE: at least one theory is required, multiple are permitted for comparison
semantic_theories = {
    "Brast-McKie" : default_theory,
    # "Author" : alternative_theory,  # to be defined above (optional)
    # additional theories will require their own translation dictionaries
}

# NOTE: at least one example is required, multiple are permitted for comparison
example_range = {
    # Counterfactual Countermodels
    # "CF_CM_0" : CF_CM_0_example,
    # "CF_CM_1" : CF_CM_1_example,
    # "CF_CM_2" : CF_CM_2_example,
    # "CF_CM_3" : CF_CM_3_example,
    # "CF_CM_4" : CF_CM_4_example,
    # "CF_CM_5" : CF_CM_5_example,
    # "CF_CM_6" : CF_CM_6_example,
    # "CF_CM_7" : CF_CM_7_example,
    # "CF_CM_8" : CF_CM_8_example,
    # "CF_CM_9" : CF_CM_9_example,
    # "CF_CM_10" : CF_CM_10_example,
    # "CF_CM_11" : CF_CM_11_example,
    # "CF_CM_12" : CF_CM_12_example,
    # "CF_CM_13" : CF_CM_13_example,
    # "CF_CM_14" : CF_CM_14_example,
    # "CF_CM_15" : CF_CM_15_example,
    # "CF_CM_16" : CF_CM_16_example,
    # "CF_CM_17" : CF_CM_17_example,
    # "CF_CM_18" : CF_CM_18_example,
    # "CF_CM_19" : CF_CM_19_example,
    # "CF_CM_19_B": CF_CM_19_B_example,
    # "EQUIV_TEST_1_example": EQUIV_TEST_1_example,
    # "EQUIV_TEST_2_example": EQUIV_TEST_2_example,
    "DA_TO_CA": DA_TO_CA_example
    # "CF_CM_20" : CF_CM_20_example,
    # "CF_CM_21" : CF_CM_21_example,

    # Modal Countermodels
    # "ML_CM_1" : ML_CM_1_example,

    # Counterfactual Theorems
    # "CF_TH_1" : CF_TH_1_example,
    # "CF_TH_2" : CF_TH_2_example,
    # "CF_TH_3" : CF_TH_3_example,
    # "CF_TH_4" : CF_TH_4_example,
    # "CF_TH_5" : CF_TH_5_example,
    # "CF_TH_6" : CF_TH_6_example,
    # "CF_TH_7" : CF_TH_7_example,
    # "CF_TH_8" : CF_TH_8_example,
    # "CF_TH_9" : CF_TH_9_example,
    # "CF_TH_10" : CF_TH_10_example,
    # "CF_TH_11" : CF_TH_11_example,
    # "CF_TH_12" : CF_TH_12_example,

    # Constitutive Theorems
    # "CL_TH_1" : CL_TH_1_example,
    # "CL_TH_2" : CL_TH_2_example,
    # "CL_TH_3" : CL_TH_3_example,
    # "CL_TH_4" : CL_TH_4_example,
    # "CL_TH_5" : CL_TH_5_example,
    # "CL_TH_6" : CL_TH_6_example,
    # "CL_TH_7" : CL_TH_7_example,
    # "CL_TH_8" : CL_TH_8_example,
}


####################
### RUN EXAMPLES ###
####################

if __name__ == '__main__':
    import subprocess
    file_name = os.path.basename(__file__)
    subprocess.run(["model-checker", file_name], check=True, cwd=current_dir)
