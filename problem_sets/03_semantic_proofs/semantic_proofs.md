# [Problem Set #3: Semantic Proofs](https://github.com/benbrastmckie/ModalHistory?tab=readme-ov-file#problem-sets)

> Instructions for the problem set for this week

This problem set concerns the semantics for _propositional modal logic_.
A number of definitions are included in the [notation.sty](https://github.com/benbrastmckie/ModalHistoryPrivate/blob/master/assets/notation.sty) file.
Please read the relevant portion of the [Logic Notes](https://github.com/benbrastmckie/LogicNotes) for the definitions.
As always, feel free to open issues if there is anything that it would be helpful to discuss.

## Problem Set

> Overview of the sections in the problem set.

There are sixty-four problems, four of which I provided as example solutions.
Work together to complete the [solutions](https://github.com/benbrastmckie/ModalHistoryPrivate/blob/master/problem_sets/03_pset/03_solutions.tex) by writing 6/60 solutions for the problems for this week.
General information is provided in the [collaboration](https://github.com/benbrastmckie/ModalHistoryPrivate/blob/master/problem_sets/collaboration.md) document.

### Truth-Conditions

The problem set begins by considering a number of natural connections between the operators included in the language and the set-theoretic operations of complement, intersection, and union.
In addition to set operations, connections between the interpretation of modal are explored by way of a number of equivalences in order to get another perspective on the semantics.

### Frames

By contrast to Kripke's _model structures_ which include a designated world $G$ in addition to the set of all worlds $K$ and a relation over those worlds $R$, the semantics has been presented in a modern form which highlights the role of the _frame_ which is a relational structure consisting of a set of worlds and a relation over those worlds.
The _models_ of the language are then interpreted over a frame where the world of evaluation is included alongside the model in order to evaluate sentences, highlighting the variability of worlds in interpreting modal sentences.

By contrast to last week, the proofs this week are much more mechanical, falling out of the definitions.
Finding countermodels requires a little more ingenuity, but also proceeds by applying the definitions.
One natural way to proceed in approaching these problems is to attempt to build a countermodel by starting with a minimal frame consisting of one world $w$ and the empty relation.
You can then proceed by changing the frame only as needed to make the assumptions true and the consequent false.

For instance, if we want to show that not every serial frame is reflexive, we can't make the frame serial by letting $R(w, w)$ since this would also make it reflexive.
Instead, we might add a new world $u$ where $R(w, u)$.
Although $w$ is related to some world, so far $u$ is not, and so the frame is not serial.
We could of course continue in this fashion, adding a further world $v$ for $u$ to see, and so on.
For instance, you might let worlds be the natural numbers where every world sees it its successor and nothing else.
Although this is a serial frame that is not reflexive, there is a much simpler one, indeed infinitely many.
In #2.1, I provide a finite frame with five elements, but even this is more than is needed.
Instead of introducing a further world $v$, we could have just let $R(u, w)$ and nothing else.

Note that the frame constraints provided in the Logic Notes are not intended to be exhaustive.
Some of the problems will require you to think a bit outside the box.

### Characterization

The problem set closes by checking elements of the soundness proofs for the various modal proof systems that we considered in the previous problem set.
Additionally, a number of logical equivalences help to give some sense of the shape of the resulting logics.
