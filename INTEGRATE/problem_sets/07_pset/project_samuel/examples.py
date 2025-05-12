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

"""
SAM Problem 1: Interpretation
The model-checker provides a countermodel showing that \Diamond A does not entail \Box A.
This makes sense because for \Diamond A to be true, there only needs to be one world where A is true. On the other hand, for \Box A to be true, every world has to be such that A is true. We can create a countermodel where there are two worlds. The first world is such that A is true while the second is such that A is false. In such a model, \Diamond A is true because the first world satisfies A, but \Box A is false because there is a world where A is false, namely the second one.

Concrete example:
"It is possible that it is raining" does not entail "It is necessary that it is raining".
The countermodel shows two worlds where it's raining in one but not the other. Thus, it is possible that is raining because there is a rain world, but it is not necessary that it is raining because not all worlds are rain worlds.
"""

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
    'max_time' : 10,
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

# BM_CM_SH1: ALL FUTURE AND ALL PAST TO NECESSITY
BM_CM_SH1_premises = ['\\Future A \\wedge \\Past A']
BM_CM_SH1_conclusions = ['\\Box A']
BM_CM_SH1_settings = {
    'N' : 1,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 60,
    'expectation' : True,
}
BM_CM_SH1_example = [
    BM_CM_SH1_premises,
    BM_CM_SH1_conclusions,
    BM_CM_SH1_settings,
]

"""
SAM Problem 2: Extension

English Translation: "In the future, it is always raining, and in the past it is always raining" entails "It is necessary that it is raining".
The model checker concluded that there is a countermodel. In this countermodel, there is a world W_0 that is at time 0 whose past times are all such that A is true and whose future times are all such that A is true. But, there is a world W_1 at time 0 where A is false. Thus, \\Future A \\wedge \\Past A is true but \\Box A is not, so the former does not entail the latter.
"""

# BM_CM_SH2: POSSIBILITY TO SOMETIMES V1
BM_CM_SH2_premises = ['\\Diamond A']
BM_CM_SH2_conclusions = ['\\Sometime A']
BM_CM_SH2_settings = {
    'N' : 1,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 240,
    'expectation' : True,
}
BM_CM_SH2_example = [
    BM_CM_SH2_premises,
    BM_CM_SH2_conclusions,
    BM_CM_SH2_settings,
]

# BM_CM_SH3: POSSIBILITY TO SOMETIMES V2
BM_CM_SH3_premises = ['\\Diamond A']
BM_CM_SH3_conclusions = ['\\past A \\vee future A \\vee A']
BM_CM_SH3_settings = {
    'N' : 1,
    'M' : 2,
    'contingent' : False,
    'disjoint' : False,
    'max_time' : 240,
    'expectation' : True,
}
BM_CM_SH3_example = [
    BM_CM_SH3_premises,
    BM_CM_SH3_conclusions,
    BM_CM_SH3_settings,
]

"""
SAM Problem 3: Break Things

BM_CM_SH3 says that there is a countermodel. I believe that I have defined the Sometimes operator in an identical way to how the conclusion appears in BM_CM_SH3, so I am unsure why BM_CM_SH2 says that there is no countermodel and does so within 0.4986 seconds as opposed to becasue it is timing out.
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
    "BM_CM_SH1" : BM_CM_SH2_example,
    "BM_CM_SH2" : BM_CM_SH2_example,
    "BM_CM_SH3" : BM_CM_SH2_example,

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

    # "BM_CM_SH1" : BM_CM_SH1_example,
    "BM_CM_SH2" : BM_CM_SH2_example,
    # "BM_CM_SH3" : BM_CM_SH3_example,

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
