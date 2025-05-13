# [Problem Set #2: Axiomatic Proofs](https://github.com/benbrastmckie/ModalHistory?tab=readme-ov-file#problem-sets)

This problem set concerns _classical propositional logic_ in the guise of a Hilbert system and an extension thereof to a number of _propositional modal logics_.
A number of definitions are included in the [notation.sty](https://github.com/benbrastmckie/ModalHistoryPrivate/blob/master/assets/notation.sty) file.
Please read the [Logic Notes](https://github.com/benbrastmckie/LogicNotes) up to the end of the section on quantified modal logics (you are welcome to skip over the Fitch system of pages 2-3).

## Problem Set

> Overview of the sections in the problem set.

Work together to complete the [solutions](https://github.com/benbrastmckie/ModalHistoryPrivate/blob/master/problem_sets/02_pset/02_solutions.tex) by writing 10/60 solutions for the problems for this week and checking another 5/60.
General information is provided in the [collaboration](https://github.com/benbrastmckie/ModalHistoryPrivate/blob/master/problem_sets/collaboration.md) document.

### Metalinguistic Abbreviation

We start with some familiar territory, defining certain operators in terms of others.
Although this problem set is focused on proof theory, it is worth justifying the conventions that we will adopt.
The definitions and semantic proofs in this section will help to do so.

### Derived Metarules and Axiomatic Proofs

Like all proof systems, Hilbert's axiom system takes some getting used to, especially coming from a natural deduction system like the Fitch system presented in this [textbook](https://github.com/benbrastmckie/ForAllX) and in many other introductory logic courses.
Moreover, when we first set out to build up a stock of derivations, we have very little to work with at the beginning, making it difficult to write derivations that only cite the axioms and rules included in the system.
Our aim is to change this one derivation at a time where we may cite instances of the derivations we have already provided in order to write further derivations a little more easily.
So even as we try to write derivations of increasing complexity and difficulty, we have more to make use of as we proceed, and so it typically gets easier as you go, not harder.

The derivations that we will be writing are _schematic_ insofar as we will not be using the well-formed sentences (wfss) of our formal language, but rather schematic variables which have wfss as their values.
This is convenient since each time we complete a schematic derivation, really what we have is a recipe for writing derivations (infinitely many) by uniformly substituting wfss for the schematic variables in the derivation that we have written.
It is for this reason that we may make use of the schematic derivations that we have established in order to provide further schematic derivations (henceforth, these will just be called _derivations_).

> [!NOTE]
> You are free to appeal to previous problems to complete derivations, citing the appropriate name for each justification (these are in bold or you can cite the section and problem number, e.g. \#6.1).
> There are a few worked examples in the solutions which should help to give you some sense of how these proofs are meant to go.
> As you will see in the example derivations, each line should consist of a line number, schema, and a justification.

There are two types of derivations to keep track of: (1) _derived rules_ of the form `$\Gamma \vdash \varphi$` where $\Gamma$ is a set of well-formed sentences and $\varphi$ a further sentence; and (2) _metarules_ of the form `If $\Gamma_1 \vdash \varphi_1,...,\Gamma_n \vdash \varphi_n$, then $\Sigma \vdash \psi$`.
You might think of (1) as a special case of (2) when there are no assumptions following the 'If', thinking of _theorems_ as a special case of (1) which have no premises (i.e. $\Gamma$ is the empty set).
Nevertheless, it is often useful to think of (1) and (2) as rather different from each other and to think of deriving theorems as very similar to deriving rules.
For instance, deriving a rule (1) amounts to writing a derivation which begins with the premises $\Gamma$ and ends with $\varphi$.
In the case of a theorem, there are no premises and so we are left with only the axioms to work with, though things otherwise proceed in a similar manner.
By contrast, to establish a metarule (2), we start out assuming the antecedent derivation(s) which make assertions about what is derivable from what without giving us a concrete derivation.
We then have to reason our way to a further claim about what is derivable from what (our conclusion derivation).
Even though (2) may sound more involved, we often have more to work with given the derivations we start out assuming.
Rather, deriving rules as in (1) without any additional assumptions are often the trickiest proofs to write.
In order to make our lives easier, we begin by proving some convenient metarules that we may use throughout.
Some of these are rather trivial and just a convenience.

Note that writing axiomatic proofs can be pretty unintuitive at first, and so it can take working through a few problems before you start to build any sense of confidence about how these are supposed to go.
I leave it to you to practice with as many as you need to get a decent sense of things and to review the problems of your peers to see what you can learn or perhaps teach, catching mistakes or pointing out easier ways to do things.
Once you get the hang of it, these can be pretty fun.

## Regimentation and Interpretation

This section provides a chance to think about using our propositional modal language to regiment English sentences.
We won't be too concerned to get the "right" regimentation, but rather to populate the options, using the expressive power that our language affords to resolve any ambiguities that we can.
The section ends with some of the readings that one might give to the modals to try out of the different axioms.

## Modal Axiomatic Proofs

Our system is set up so that the deduction theorem holds.
This is not true of all systems, but a virtue of ours since it also makes writing proofs a lot easier.
I will add a proof of the deduction theorem for our modal Hilbert system shortly, but until then, you are welcome to make use of this handy metarule.
The proofs of the other metarules (extending them to our propositional modal language) are the same, and so need not be repeated.
Nevertheless, you may proceed by appealing to any derivations or metarules given above the problem you are working on.

## Further Particulars

Hopefully I have not made too many errors, but if I have, don't hesitate to raise this in the issues.

If you have any technical questions (software, LaTeX, etc.), don't hesitate to bring them up!
Also, LLMs are very good at LaTeX (and troubleshooting) so well worth seeing what they can do to help.
