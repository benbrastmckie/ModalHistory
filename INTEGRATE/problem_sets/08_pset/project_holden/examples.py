"""
Examples Module for the unified theory (Brast-McKie).

This module provides a collection of test cases for the unified semantics
including both countermodels showing invalidity and theorems showing validity.

Module Structure:
----------------
1. Imports:
   - System utilities (os, sys)
   - Local semantic definitions (Semantics, Proposition, ModelStructure)
   - Local operator definitions (default_operators)

2. Settings:
   - general_settings: Global settings for output and debugging
   - example_settings: Default parameters for test cases

3. Semantic Theory:
   - default_theory: Default semantic framework with components:
     * semantics: Core semantic class
     * proposition: Proposition handling
     * model: Model structure implementation
     * operators: Logical operators

4. Example Categories:
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
Each example is defined as [premises, conclusions, settings] where:
- premises: List of formulas serving as assumptions
- conclusions: List of formulas to test
- settings: Dictionary with parameters:
  * N: Number of atomic propositions
  * contingent: Use contingent valuations
  * disjoint: Enforce disjoint valuations
  * non_empty: Enforce non-empty valuations
  * non_null: Enforce non-null valuations
  * max_time: Maximum computation time (seconds)
  'iterate' : 1,
  * expectation: Expected result (True for countermodel found)

Configuration:
-------------
- semantic_theories: Dictionary mapping theory names to implementations
- example_range: Dictionary mapping example names to test cases

Notes:
------
- Additional semantic theories can be added by defining their components
  and translation dictionaries
- The example_range can be modified to run different subsets of tests
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
    'max_time' : 2,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_6_example = [
    CF_CM_6_premises,
    CF_CM_6_conclusions,
    CF_CM_6_settings,
]

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
    'iterate' : 5,
    'expectation' : True,
}
CF_CM_9_example = [
    CF_CM_9_premises,
    CF_CM_9_conclusions,
    CF_CM_9_settings,
]
"""
The model-checker provides a countermodel showing that (\\neg A), (\\neg B), and (A \\boxright B) do not ential (\\neg B \\boxright \\neg A).
This makes sense because we cannot conclude about the worlds in which A is false based only on knowing that B would be true in the closest worlds where A is true.
It is possible for the closest worlds where A is true to have B true, bu the cloest worlds that have B false to have A true, in particular, if, from the perspective of the cloesest worlds where A is true, the worlds where B is false are farther than the worlds where B is true.

The countermodel returned by the model checker is rather complicated. The following is my best attempt to create a real world example that matches it, but it is arguably rather convoluted.

Here is the countermodel returned by the model checker:

State Space:
  #b0000 = □
  #b0001 = a
  #b0010 = b
  #b0100 = c
  #b0101 = a.c (world)
  #b0110 = b.c (world)
  #b1000 = d
  #b1010 = b.d (world)

The evaluation world is: a.c

INTERPRETED PREMISES:

1.  |\neg A| = < {a.c}, {b} >  (True in a.c)
      |A| = < {b}, {a.c} >  (False in a.c)

2.  |\neg B| = < {a.c, b.d}, {b.c} >  (True in a.c)
      |B| = < {b.c}, {a.c, b.d} >  (False in a.c)

3.  |(A \boxright B)| = < {□}, ∅ >  (True in a.c)
      |A| = < {b}, {a.c} >  (False in a.c)
      |A|-alternatives to a.c = {b.c}
        |B| = < {b.c}, {a.c, b.d} >  (True in b.c)

INTERPRETED CONCLUSION:

4.  |(\neg B \boxright \neg A)| = < ∅, {□} >  (False in a.c)
      |\neg B| = < {a.c, b.d}, {b.c} >  (True in a.c)
        |B| = < {b.c}, {a.c, b.d} >  (False in a.c)
      |\neg B|-alternatives to a.c = {a.c, b.d}
        |\neg A| = < {a.c}, {b} >  (False in b.d)
          |A| = < {b}, {a.c} >  (True in b.d)
        |\neg A| = < {a.c}, {b} >  (True in a.c)
          |A| = < {b}, {a.c} >  (False in a.c)


Concrete example:

State space:
    #b0000 = □              Null state
    #b0001 = a              It is sunny
    #b0010 = b              It is raining
    #b0100 = c              I am inside
    #b1000 = d              I need a jacket
    #b0101 = a.c (world)    World where it is sunny and I am inside
    #b0110 = b.c (world)    World where it is raining and I am inside
    #b1010 = b.d (world)    World where it is raining and I need a jacket

Key interpretations:
    A = I can hear the weather
    B = It's wet outside but I'm not wet

The most similar world to world a.c in which A is true is world b.c. The most similar worlds to world a.c in which B is false are a.c and b.d

In the world a.c (where it is sunny and I am inside):
    The premises are true
        - I cannot hear the weather (~A is true)
        - It's not the case that it's wet outside and I'm not wet (~B is true)
        - If A were true, then B would be true. In particular, the A alternative to a.c is b.c, which verifies B
            - In English, if I could hear the whether, then the most likely situation is that it's raining, in which case It's wet outside, but I'm not wet (since I'm still inside).
    The conclusion is false
        - The ~B alternatives to a.c are a.c and b.d, and in b.d, A is true, so ~A is false
        - In English, this says that if it were wet outside but I'm not wet, the most likely situations are that it's sunny and I'm inside or that it's raining and I need a jacket, and if it's raining and I need a jacket, then I can hear the weather.

As I said, this example is somewhat counterintuitive. In particular, the alternative worlds are questionable. If a.c is the current world, it's very strange to suggest that b.d is tied for similarity with a.c. Moreover, in general, this argument seems to me to be intuitively true in English.
    For starters, it seems like the stronger argument with premises ~A and ~B and conclusion (~B \\boxright ~A) is relatively intuitive in English.
    If we already have that ~B is true, surely the most similar world in which ~B is true is the current one, and any different world would be strictly less similar, and in the current world, ~A follows.
    Furthermore, if we add (A \\boxright B) to the set of premises, then the argument seems even more counterintuitive.
    To reject it, it must be the case that for some world that is tied as the most similar to the current world, A is true and B is false.
    But we know that the worlds that are most similar to the current world with A true have B true as well.
    Hence, this world that has A true and B false is not one of the most similar to the current world with A true.
    The particularly strange thing is that this world is both as similar to the current world as possible when looking at worlds that have B false, but not tied for the most similar when looking at worlds that have A true.
    This may be possible technically, but it doesn't match any of my intuitive understandings of most similar.
"""

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

# Problem 2
EX_2_premises = ['(A \\boxright B)', '\\neg A']
EX_2_conclusions = ['(\\neg B \\diamondright \\neg A)']
EX_2_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : True,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : True,
}
EX_2_example = [
    EX_2_premises,
    EX_2_conclusions,
    EX_2_settings,
]
"""
The model-checker provides a countermodel showing that (A \\boxright B) and \\neg A do not entail (\\neg B \\diamondright \\neg A).
This makes sense because it is possible that \\neg A and \\neg B are incompatible, in which case (\\neg B \diamondright \\neg A) could not possibly follow from the premises.

Here is the countermodel returned by the model-checker:

State Space:
  #b0000 = □
  #b0001 = a
  #b0010 = b
  #b0011 = a.b (world)
  #b0100 = c
  #b0110 = b.c (world)
  #b1000 = d
  #b1100 = c.d (world)

The evaluation world is: c.d

INTERPRETED PREMISES:

1.  |(A \boxright B)| = < {□}, ∅ >  (True in c.d)
      |A| = < {b}, {d} >  (False in c.d)
      |A|-alternatives to c.d = {b.c}
        |B| = < {c}, {a} >  (True in b.c)

2.  |\neg A| = < {d}, {b} >  (True in c.d)
      |A| = < {b}, {d} >  (False in c.d)

INTERPRETED CONCLUSION:

3.  |(\neg B \diamondright \neg A)| = < ∅, {□} >  (False in c.d)
      |\neg B| = < {a}, {c} >  (False in c.d)
        |B| = < {c}, {a} >  (True in c.d)
      |\neg B|-alternatives to c.d = {a.b}
        |\neg A| = < {d}, {b} >  (False in a.b)
          |A| = < {b}, {d} >  (True in a.b)


Concrete example in English:
    A: 'It is not raining'
    B: 'It is not snowing'

    Assume we're in a state where it is raining.
    Then 'It is not raining' is false, and 'If it were not raining it would not be snowing' is true
    Intuitively, it makes sense that if it were not raining, it would not be snowing because the change from rain to snow is (at least in my mind) larger than the change from rain to no rain.
    At the same time, 'If it were snowing, it might be raining' is clearly false, because it can't be raining and snowing at the same time.

Attempting to match this counterexmaple to the format given by the model checker might go as follows:

    State Space:
        #b0000 = □              null state
        #b0001 = a              it is snowing
        #b0010 = b              it is not raining
        #b0100 = c              it is not snowing
        #b1000 = d              it is raining
        #b0011 = a.b (world)    world where it is snowing and not raining
        #b0110 = b.c (world)    world where it is not snowing and not raining
        #b1100 = c.d (world)    world where it is raining and not snowing

    Key interpretations:
        A = 'It is not raining' (verified by b and falsified by d)
        B = 'It is not snowing' (verified by c and falsified by a)

    Evaluation world: c.d (world where it is raining and not snowing)

    Let the |A|-alternatives to c.d be {b.c} (the closest world to the world where it is raining and not snowing where it's not raining is the world where it is not raining or snowing)
    Let the |\\neg B|-alternatives to c.d be {a.b} (the closest world to the world where it is raining and snowing where it's snowing is the world where it's snowing and not raining)

    In the evaluation world, we have d, which falsifies A, and verifies ~A.
    The only |A|-alternative to the evaluation world is b.c.
    In this world, we have c, which verifies B.
    Hence, (A \\boxright B).

    The only |\\neg B|-alternative to the evaluation world is a.b.
    In this world, we have b, which verifies A.
    Hence, we do not have (\\neg B \\diamondright \\neg A)

Of note is the fact that if we add the single premise '\\neg B', then the argument becomes valid.
We trivially have the conclusion '(\\neg B \\diamondright \\neg A)' from the fact that '\\neg B' and '\\neg A' are both true to start with.
On the other hand, the stronger conclusion '(\\neg B \boxright \\neg A)' is false, as is shown in example CF_CM_9_example
"""

# Problem 3a
EX_3a_premises = []
EX_3a_conclusions = [r'(\CFBox A \leftrightarrow \Box A)']
EX_3a_settings = {
    'N' : 5,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
EX_3a_example = [
    EX_3a_premises,
    EX_3a_conclusions,
    EX_3a_settings,
]
"""
Running with 5 states, I can complete the search for a countermodel in 0.1585 seconds.
Running with 6 states, it takes 3.8196 seconds.
Running with 7 or more states, it takes longer than 5 seconds, and I did not complete any searches of that length.

This is notable because CFBox is not simply defined in terms of \Box.
It is defined in terms of the counterfactual operator, which is a premitive.
Hence, this is a meaningful result.
"""

# Problem 3b
EX_3b_premises = []
EX_3b_conclusions = [r'(\CFDiamond A \leftrightarrow \neg \CFBox \neg A)']
EX_3b_settings = {
    'N' : 5,
    'contingent' : False,
    'disjoint' : False,
    'non_empty' : False,
    'non_null' : False,
    'max_time' : 1,
    'iterate' : 1,
    'expectation' : False,
}
EX_3b_example = [
    EX_3b_premises,
    EX_3b_conclusions,
    EX_3b_settings,
]
"""
Running with 5 states, I can complete the search for a countermodel in 0.2251 seconds.
Running with 6 states, it takes 5.5069 seconds.
Running with 7 or more states, it takes longer than 10 seconds, and I did not complete any searches of that length.

\\CFDiamond A is defined as ⊤ ◇→ A, which is in turn defined as ¬(⊤ □→ ¬A).
\\neg \\CFBox \\neg A is defined as ¬(⊤ □→ ¬A)
Hence, it is not surprising that these are equivalent, as they are defined the same way.
This is similar to showing that (\\Diamond A \\leftrightarrow \\neg \\Box \\neg A).
There are a few more steps of definitions in showing that \\CFDiamond A and \\neg \\CFBox \\neg A are defined the same way, so arguably this result is a little less trivial, but they both come purely from definitions and not semantics.
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

    # New examples
    # "EX_2" : EX_2_example,
    # "EX_3a" : EX_3a_example,
    "EX_3b" : EX_3b_example,
}


if __name__ == '__main__':
    import subprocess
    file_name = os.path.basename(__file__)
    subprocess.run(["model-checker", file_name], check=False, cwd=current_dir)
