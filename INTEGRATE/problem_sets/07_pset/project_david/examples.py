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

"""

DAVID PROBLEM 1: 

The model-checker provides a counter-model showing that \Diamond A does not entail A. This counter-model includes a world, accessible from another, in which A. But, at that world (which sees the A-world), not-A. So, at that world it's the case that not-A. But, at that world, it's possible that A (as it sees an A-world). 

Concrete example: 

There is a world, w2, accessible from w1, in which it is raining. So, \Diamond it is raining. But, it's not raining in the actual w1. That is: we have a modal in which it is possible that it's raining but it's not raining. So, from \Diamond, we cannot infer A. 

"""

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

# TN_CM_1: ALL FUTURE TO NECESSITY
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

# TN_CM_2: ALL PAST TO NECESSITY
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

# MD_CM_3: POSSIBILITY TO SOME FUTURE
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

# MD_CM_4: POSSIBILITY TO SOME PAST
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

# MD_CM_DL1: SOME PAST AND SOME FUTURE TO NECESSITY 
BM_CM_DL1_premises = ['\\past A \\wedge \\future A']
BM_CM_DL1_conclusions = ['\\Box A']
BM_CM_DL1_settings = {
    'N' : 2,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 10,
    'expectation' : True,
}
BM_CM_DL1_example = [
    BM_CM_DL1_premises,
    BM_CM_DL1_conclusions,
    BM_CM_DL1_settings,
]

# MD_CM_DL2: ALL PAST AND ALL FUTURE TO NECESSITY 
BM_CM_DL2_premises = ['\\Past A \\wedge \\Future A']
BM_CM_DL2_conclusions = ['\\Box A']
BM_CM_DL2_settings = {
    'N' : 2,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 10,
    'expectation' : True,
}
BM_CM_DL2_example = [
    BM_CM_DL2_premises,
    BM_CM_DL2_conclusions,
    BM_CM_DL2_settings,
]


""" 

DAVID PROBLEM 2_DL1: 

The example: past A wedge  future A to Box A. That is: if there's some time in the past that A and some time in the future that A. Therefore, necesarilly A. 

I'm puzzled by the model checker's answer to this, so I've pasted it here: 

World Histories:
  W_0: (-1:c) =⟹ (0:a)
  W_1:           (0:c) =⟹ (+1:a)

Evaluation Point:
  World History W_0: c =⟹ a
  Time: 0
  World State: a

INTERPRETED PREMISE:

1.  |past A wedge future A| = < {a}, {c} >  (True in W_0 at time 0)
      |A| = < {c}, {a} >  (True in W_0 at time -1)
      |A| = < {c}, {a} >  (False in W_0 at time 0)
      |A| = < {c}, {a} >  (False in W_0 at time 1)

INTERPRETED CONCLUSION:

2.  |Box A| = < {c}, {a, c} >  (False in W_0 at time 0)
      |A| = < {c}, {a} >  (False in W_0 at time 0)
      |A| = < {c}, {a} >  (True in W_1 at time 0)

DAVID PROBLEM 2 DL2: 

This countermodel makes sense. There are two worlds, w0 and w1. At w0, there's some past time in which A is true. In w0, there's also a time in the future at which A is true. Those are the only past times and only future times. So, the conjunction is true. But, there's a world accessible from w0 at which A is false. So, Past A and Future A does not yield Box A. 

'At every past time, there's war and at every future time there's war'. It does not follow from this that `necesarilly, there's war'. There is a world accessible from this world (say) in which everyone's a pacifist and there's no war. 
"""




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

# MD_TH_2: 
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
    "BM_CM_DL1" : BM_CM_DL1_example,


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
    # "BM_CM_DL1" : BM_CM_DL1_example,
    "BM_CM_DL2" : BM_CM_DL2_example,



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
}
