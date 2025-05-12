"""
Examples Module for bimodal logic theory.

This module provides a collection of test cases for bimodal semantic theory,
which combines temporal and modal operators to reason about what is true
at different times and in different possible worlds.

Module Structure:
----------------
1. Imports:
   - System utilities (os, sys)
   - Local semantic definitions (BimodalSemantics, BimodalProposition, BimodalStructure)
   - Local operator definitions (bimodal_operators)

2. Semantic Theory:
   - default_theory: Default bimodal semantic framework
   - semantic_theories: Dictionary of semantic theory implementations

3. Example Definitions:
   - example_range: Dictionary of example test cases
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
    BimodalStructure,
    BimodalSemantics,
    BimodalProposition,
)
from operators import bimodal_operators

#######################
### DEFAULT SETTINGS ###
#######################

general_settings = {
    "print_constraints": False,
    "print_z3": False,
    "save_output": False,
    "align_vertically": False,
}



####################################
### DEFINE THE SEMANTIC THEORIES ###
####################################

bimodal_theory = {
    "semantics": BimodalSemantics,
    "proposition": BimodalProposition,
    "model": BimodalStructure,
    "operators": bimodal_operators,
    # translation dictionary is only required for comparison theories
}



##############################################################################
############################### COUNTERMODELS ################################
##############################################################################

#################################
### EXTENSIONAL COUNTERMODELS ###
#################################

# EX_CM_1: DISJUNCTION TO CONJUNCTION
EX_CM_1_premises = ['(A \\vee B)']
EX_CM_1_conclusions = ['(A \\wedge B)']
EX_CM_1_settings = {
    'N' : 1,
    'M' : 1,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 2,
    'expectation' : True,
}
EX_CM_1_example = [
    EX_CM_1_premises,
    EX_CM_1_conclusions,
    EX_CM_1_settings,
]



###########################
### MODAL COUNTERMODELS ###
###########################

# MD_CM_1: DISTRIBUTE NECESSITY OVER DISJUNCTION
MD_CM_1_premises = ['\\Box (A \\vee B)']
MD_CM_1_conclusions = ['\\Box A', '\\Box B']
MD_CM_1_settings = {
    'N' : 1,
    'M' : 1,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 2,
    'iterate' : 2,
    'expectation' : True,
}
MD_CM_1_example = [
    MD_CM_1_premises,
    MD_CM_1_conclusions,
    MD_CM_1_settings,
]

# MD_CM_2: DISTRIBUTE POSSIBILITY OVER CONJUNCTION
MD_CM_2_premises = ['\\Diamond (A \\vee B)']
MD_CM_2_conclusions = ['(\\Diamond A \\wedge \\Diamond B)']
MD_CM_2_settings = {
    'N' : 1,
    'M' : 1,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 2,
    'expectation' : True,
}
MD_CM_2_example = [
    MD_CM_2_premises,
    MD_CM_2_conclusions,
    MD_CM_2_settings,
]

# MD_CM_3: ACTUALITY TO NECESSITY
MD_CM_3_premises = ['A']
MD_CM_3_conclusions = ['\\Box A']
MD_CM_3_settings = {
    'N' : 1,
    'M' : 1,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 2,
    'expectation' : True,
}
MD_CM_3_example = [
    MD_CM_3_premises,
    MD_CM_3_conclusions,
    MD_CM_3_settings,
]

# MD_CM_4: POSSIBILITY TO ACTUALITY
MD_CM_4_premises = ['\\Diamond A']
MD_CM_4_conclusions = ['A']
MD_CM_4_settings = {
    'N' : 1,
    'M' : 1,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 2,
    'expectation' : True,
}
MD_CM_4_example = [
    MD_CM_4_premises,
    MD_CM_4_conclusions,
    MD_CM_4_settings,
]

# MD_CM_5: POSSIBILITY TO NECESSITY
MD_CM_5_premises = ['\\Diamond A']
MD_CM_5_conclusions = ['\\Box A']
MD_CM_5_settings = {
    'N' : 1,
    'M' : 1,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 2,
    'expectation' : True,
}
MD_CM_5_example = [
    MD_CM_5_premises,
    MD_CM_5_conclusions,
    MD_CM_5_settings,
]

# MD_CM_6: INCOMPATIBLE POSSIBILITIES
MD_CM_6_premises = ['\\Diamond A', '\\Diamond B']
MD_CM_6_conclusions = ['\\Diamond (A \\wedge B)']
MD_CM_6_settings = {
    'N' : 1,
    'M' : 1,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 2,
    'expectation' : True,
}
MD_CM_6_example = [
    MD_CM_6_premises,
    MD_CM_6_conclusions,
    MD_CM_6_settings,
]



###########################
### TENSE COUNTERMODELS ###
###########################

# TN_CM_1: 
TN_CM_1_premises = ['A']
TN_CM_1_conclusions = ['\\Future A']
TN_CM_1_settings = {
    'N' : 1,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 5,
    'expectation' : True,
}
TN_CM_1_example = [
    TN_CM_1_premises,
    TN_CM_1_conclusions,
    TN_CM_1_settings,
]

# TN_CM_2: 
TN_CM_2_premises = ['\\future A', '\\future B']
TN_CM_2_conclusions = ['\\future (A \\wedge B)']
TN_CM_2_settings = {
    'N' : 1,
    'M' : 3,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 5,
    'expectation' : True,
}
TN_CM_2_example = [
    TN_CM_2_premises,
    TN_CM_2_conclusions,
    TN_CM_2_settings,
]




#############################
### BIMODAL COUNTERMODELS ###
#############################

# BM_CM_1: ALL FUTURE TO NECESSITY
BM_CM_1_premises = ['\\Future A']
BM_CM_1_conclusions = ['\\Box A']
BM_CM_1_settings = {
    'N' : 1,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 5,
    'expectation' : True,
}
BM_CM_1_example = [
    BM_CM_1_premises,
    BM_CM_1_conclusions,
    BM_CM_1_settings,
]

# BM_CM_2: ALL PAST TO NECESSITY
BM_CM_2_premises = ['\\Past A']
BM_CM_2_conclusions = ['\\Box A']
BM_CM_2_settings = {
    'N' : 1,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 5,
    'expectation' : True,
}
BM_CM_2_example = [
    BM_CM_2_premises,
    BM_CM_2_conclusions,
    BM_CM_2_settings,
]
"""
The model-checker provides a countermodel showing that 'Past(A)' does not entail 'Box(A)'.
This makes sense as it is possible for A to have always been true without it necessarily
being true, for example if it becomes false in the future.

Concrete example:
'I have always been younger than '22' does not entail 'I am necessarily younger than 22'.
The countermodel could represent a world in which I am 21, satisfying the premise, but
where in the future, I am 22, and because we can time shift, this results in there being
an alternate world in which I am 22, falsifying the conclusion.
"""

# BM_CM_3: POSSIBILITY TO SOME FUTURE
BM_CM_3_premises = ['\\Diamond A']
BM_CM_3_conclusions = ['\\future A']
BM_CM_3_settings = {
    'N' : 2,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 2,
    'expectation' : True,
}
BM_CM_3_example = [
    BM_CM_3_premises,
    BM_CM_3_conclusions,
    BM_CM_3_settings,
]

# BM_CM_4: POSSIBILITY TO SOME PAST
BM_CM_4_premises = ['\\Diamond A']
BM_CM_4_conclusions = ['\\past A']
BM_CM_4_settings = {
    'N' : 2,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 2,
    'expectation' : True,
}
BM_CM_4_example = [
    BM_CM_4_premises,
    BM_CM_4_conclusions,
    BM_CM_4_settings,
]




##############################################################################
################################## THEOREMS ##################################
##############################################################################

############################
### EXTENSIONAL THEOREMS ###
############################

# EX_TH_1: CONJUNCTION TO DISJUNCTION 
EX_TH_1_premises = ['(A \\wedge B)']
EX_TH_1_conclusions = ['(A \\vee B)']
EX_TH_1_settings = {
    'N' : 1,
    'M' : 1,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 2,
    'expectation' : True,
}
EX_TH_1_example = [
    EX_TH_1_premises,
    EX_TH_1_conclusions,
    EX_TH_1_settings,
]



######################
### MODAL THEOREMS ###
######################

# MD_TH_1: NECESSITY DISTRIBUTE OVER IMPLICATION
MD_TH_1_premises = ['\\Box (A \\rightarrow B)']
MD_TH_1_conclusions = ['(\\Box A \\rightarrow \\Box B)']
MD_TH_1_settings = {
    'N' : 2,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 2,
    'expectation' : False,
}
MD_TH_1_example = [
    MD_TH_1_premises,
    MD_TH_1_conclusions,
    MD_TH_1_settings,
]

# MD_TH_2: TEST CONTINGENCY SETTING
MD_TH_2_premises = ['\\Box A']
MD_TH_2_conclusions = []
MD_TH_2_settings = {
    'N' : 1,
    'M' : 2,
    'contingent' : True,
    'disjoint' : False,
    'max_time' : 2,
    'expectation' : True,
}
MD_TH_2_example = [
    MD_TH_2_premises,
    MD_TH_2_conclusions,
    MD_TH_2_settings,
]



######################
### TENSE THEOREMS ###
######################

# TN_TH_2: 
TN_TH_2_premises = ['A']
TN_TH_2_conclusions = ['\\Future \\past A']
TN_TH_2_settings = {
    'N' : 2,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 2,
    'expectation' : False,
}
TN_TH_2_example = [
    TN_TH_2_premises,
    TN_TH_2_conclusions,
    TN_TH_2_settings,
]



########################
### BIMODAL THEOREMS ###
########################

# BM_TH_1: NECESSITY TO ALL FUTURE (PERPETUITY)
BM_TH_1_premises = ['\\Box A']
BM_TH_1_conclusions = ['\\Future A']
BM_TH_1_settings = {
    'N' : 1,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 5,
    'expectation' : False,
}
BM_TH_1_example = [
    BM_TH_1_premises,
    BM_TH_1_conclusions,
    BM_TH_1_settings,
]

# BM_TH_2: NECESSITY TO ALL PAST (PERPETUITY)
BM_TH_2_premises = ['\\Box A']
BM_TH_2_conclusions = ['\\Past A']
BM_TH_2_settings = {
    'N' : 1,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 2,
    'expectation' : False,
}
BM_TH_2_example = [
    BM_TH_2_premises,
    BM_TH_2_conclusions,
    BM_TH_2_settings,
]

# BM_TH_3: POSSIBILITY TO SOME FUTURE (PERPETUITY)
BM_TH_3_premises = ['\\future A']
BM_TH_3_conclusions = ['\\Diamond A']
BM_TH_3_settings = {
    'N' : 1,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 5,
    'expectation' : False,
}
BM_TH_3_example = [
    BM_TH_3_premises,
    BM_TH_3_conclusions,
    BM_TH_3_settings,
]

# BM_TH_4: POSSIBILITY TO SOME PAST (PERPETUITY) 
BM_TH_4_premises = ['\\past A']
BM_TH_4_conclusions = ['\\Diamond A']
BM_TH_4_settings = {
    'N' : 1,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 2,
    'expectation' : False,
}
BM_TH_4_example = [
    BM_TH_4_premises,
    BM_TH_4_conclusions,
    BM_TH_4_settings,
]


#######################
### CUSTOM EXAMPLES ###
#######################

# Custom theorem 1
CM_TH_1_presmises = [r'\Box A']
CM_TH_1_conclusions = [r'\Past \Box A \wedge \Box A \wedge \Future A']
CM_TH_1_settings = {
    'N' : 1,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 5,
    'expectation' : False,
}
CM_TH_1_example = [
    CM_TH_1_presmises,
    CM_TH_1_conclusions,
    CM_TH_1_settings
]
"""
The model-checker says that there is no countermodel for Box(A) entails Always(Box(A)).
This makes sense since it is a true theorem.
Intuitively, it says that if something is necessarily true, it is always necessarily true.
This follows from the fact that if something is necessarily true, it is ncessarily
necessarily true, and from the fact that every possible past and future exists at the current time
in a time shifted world, so if something is true in every world, it is true in every time. 

Concrete example:
'The ball is necessarily red or not red' entails 'the ball is always necessarily red or not red'.
"""

# Custom countermodel 2
CM_CM_2_presmises = [r'\Future \future A', r'\Future \future B']
CM_CM_2_conclusions = [r'\future (A \wedge B)']
CM_CM_2_settings = {
    'N' : 2,
    'M' : 3,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 5,
    'expectation' : True,
}
CM_CM_2_example = [
    CM_CM_2_presmises,
    CM_CM_2_conclusions,
    CM_CM_2_settings
]
"""
The model-checker says that there is no countermodel for Future(future(A)) and Future(future(B))
entails future(A ∧ B). This is wrong, in that there is a countermodel, but it is correct in that
there is no countermodel with the given settings. In particular, I claim there is no finite
countermodel for this example. If in particular, if Future(future(A)) holds, then A will always
be true at some point in the future. This is only possible if A is true in the final time state.
By symmetry, B is also true in the final time state. So (A ∧ B) is true in the final time state.
Hence, future(A ∧ B) is true from every time state. However, if we allow infinitely many times,
then there's a counterexample where each time state alternates between having A and B true. In
this case, it is never the case that A and B are true at the same time, but they are both always
true at some point in the future.

Concrete example:
'It will always be the case that the current year will be even in the future' and
'It will always be the case that the current year will be odd in the future' does not entail
'The current year will be both even and odd in the future' when there are infinitely many years,
but it does when there are finitely many years, because the last year must be both even and odd.
"""

# Custom countermodel 3
CM_CM_3_presmises = [r'\Future \future A']
CM_CM_3_conclusions = [r'\Future B']
CM_CM_3_settings = {
    'N' : 2,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 5,
    'expectation' : True,
}
CM_CM_3_example = [
    CM_CM_3_presmises,
    CM_CM_3_conclusions,
    CM_CM_3_settings
]
"""
This seems to be a case where the model checker fails to find a countermodel when one should exist.
The truth of Future(future(A)) shouldn't have any bearing on Future(B), as B is unrelated to A.

Concrete example:
'It will always be the case that it will rain at some point in the future' does not entail
'It will always be the case that unicorns exist'.
"""

# Custom theorem 4
CM_TH_4_presmises = [r'\Box A']
CM_TH_4_conclusions = [r'\Always A']
CM_TH_4_settings = {
    'N' : 1,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 5,
    'expectation' : False,
}
CM_TH_4_example = [
    CM_TH_4_presmises,
    CM_TH_4_conclusions,
    CM_TH_4_settings
]
"""
This the same example as CM_TH_1, but using the defined operator instead.
It works in the same way.
"""

# Custom countermodel 5
CM_CM_5_presmises = [r'\Always A']
CM_CM_5_conclusions = [r'\Box A']
CM_CM_5_settings = {
    'N' : 2,
    'M' : 1,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 5,
    'expectation' : True,
}
CM_CM_5_example = [
    CM_CM_5_presmises,
    CM_CM_5_conclusions,
    CM_CM_5_settings
]
"""
This is another test of the 'Always' operator. The model checker successfuly
finds a countermodel, which is correct.

Concrete example:
'The ball is always red' does not entail 'The ball is necessarily red'.
The countermodel shows that there can be one world in which something is
always true, while there is another world where it is not always true.
"""


###############################################
### DEFINE EXAMPLES AND THEORIES TO COMPUTE ###
###############################################

# NOTE: at least one theory is required, multiple are permitted for comparison
semantic_theories = {
    "Brast-McKie" : bimodal_theory,
    # additional theories will require their own translation dictionaries
}

test_example_range = {
    ### COUNTERMODELS ###

    # Extensional Countermodels
    "EX_CM_1" : EX_CM_1_example,
    
    # Modal Countermodels
    "MD_CM_1" : MD_CM_1_example,
    "MD_CM_2" : MD_CM_2_example,
    "MD_CM_3" : MD_CM_3_example,
    "MD_CM_4" : MD_CM_4_example,
    "MD_CM_5" : MD_CM_5_example,
    "MD_CM_6" : MD_CM_6_example,

    # Tense Countermodels
    "TN_CM_1" : TN_CM_1_example,
    "TN_CM_2" : TN_CM_2_example,

    # Bimodal Countermodels
    "BM_CM_1" : BM_CM_1_example,
    "BM_CM_2" : BM_CM_2_example,
    "BM_CM_3" : BM_CM_3_example,
    "BM_CM_4" : BM_CM_4_example,

    ### THEOREMS ###

    # Extensional Theorems
    "EX_TH_1" : EX_TH_1_example,

    # Modal Theorems
    "MD_TH_1" : MD_TH_1_example,
    "MD_TH_2" : MD_TH_2_example,

    # Tense Theorems
    "TN_TH_2" : TN_TH_2_example,

    # Bimodal Theorems
    "BM_TH_1" : BM_TH_1_example,
    "BM_TH_2" : BM_TH_2_example,
    "BM_TH_3" : BM_TH_3_example,
    "BM_TH_4" : BM_TH_4_example,

    # Custom examples
    "CM_TH_1" : CM_TH_1_example,
    "CM_CM_2" : CM_CM_2_example,
    "CM_CM_3" : CM_CM_3_example,
    "CM_TH_4" : CM_TH_4_example,
    "CM_CM_5" : CM_CM_5_example,
}

# NOTE: at least one example is required, multiple are permitted for comparison
example_range = {

    ### COUNTERMODELS ###

    # Extensional Countermodels
    # "EX_CM_1" : EX_CM_1_example,
    
    # Modal Countermodels
    # "MD_CM_1" : MD_CM_1_example,
    # "MD_CM_2" : MD_CM_2_example,
    # "MD_CM_3" : MD_CM_3_example,
    # "MD_CM_4" : MD_CM_4_example,
    # "MD_CM_5" : MD_CM_5_example,
    # "MD_CM_6" : MD_CM_6_example,

    # Tense Countermodels
    # "TN_CM_1" : TN_CM_1_example,
    # "TN_CM_2" : TN_CM_2_example,

    # Bimodal Countermodels
    # "BM_CM_1" : BM_CM_1_example,
    # "BM_CM_2" : BM_CM_2_example,
    # "BM_CM_3" : BM_CM_3_example,
    # "BM_CM_4" : BM_CM_4_example,

    ### THEOREMS ###

    # Extensional Theorems
    # "EX_TH_1" : EX_TH_1_example,

    # Modal Theorems
    # "MD_TH_1" : MD_TH_1_example,
    # "MD_TH_2" : MD_TH_2_example,

    # Tense Theorems
    # "TN_TH_2" : TN_TH_2_example,

    # Bimodal Theorems
    # "BM_TH_1" : BM_TH_1_example,
    # "BM_TH_2" : BM_TH_2_example,
    # "BM_TH_3" : BM_TH_3_example,
    # "BM_TH_4" : BM_TH_4_example,

    # Custom Theorems
    # "CM_TH_1" : CM_TH_1_example,
    # "CM_CM_2" : CM_CM_2_example,
    # "CM_CM_3" : CM_CM_3_example,
    # "CM_TH_4" : CM_TH_4_example,
    "CM_CM_5" : CM_CM_5_example,
}
