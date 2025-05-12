Miguel Final Presentation outline

# Revamping the `exclusion` theory in `theory_lib`

This project concerns revamping the exclusion semantics from Bernard and Champollion (2024)'s unilateral exclusion semantics for negation. This semantics is interesting because it uses different machinery in the formal aspect from something like Ben's theory of counterfactuals, meaning that it is not something we are used to implementing in the `model-checker`. We have tried to implement the exclusion semantics (`exclusion` in `theory_lib`), but I am not confident that it is actually working because some things that Champollions has countermodels to we do not find countermodels for. 

## Differences in formal machinery
Bernard and Champollion use three things that are different from existing semantics (`default` and `imposition`):
- Sets of states
- Fusion over uninterpreted sets of states in constraints
- Functions from states to states in semantic clauses _and_ quantification over said functions
Right now, we implement functions as Z3 `Function`s. However, one cannot quantify over Z3 `Function` objects, so this means we have to resort to instantiating a new `Function` object every time we want to call the semantic clause involving the quantification over functions. We also deal with sets by making z3 set objects and translating between these and python sets as necessary.

There are some problems with the current approach:
- Z3 `Function`s become objects in the  model, meaning that if we want to evaluate a constraint after finding a model (as we often do when finding verifiers and falsifers for propositions in the `default` semantics) we need the function to be in the model, meaning it needs to have been there before the model was solved for. 
