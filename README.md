# 24.711: The Modern History of Modal Logic

> A graduate course in _Philosophical Logic_ at MIT covering the modern history of modal logic.

**Description:** The seminar will cover the modern history of modal logic, focusing on the development of both its proof theories and semantic systems. (1) The first module will begin with C.I. Lewis' systems of strict implication 1912 - 1932, focusing on their early motivations and interpretations. The module will conclude with Ruth Barcan Marcus' first-order extensions of the systems of strict implication 1946 and the critiques raised by Quine 1943 - 1947 that modal logic will lead back into the "jungle of Aristotelian metaphysics". (2) The second module will focus on the development of intensional semantics by comparing Carnap 1946 and Kripke's 1963 accounts. We will then consider Prior's 1967 tense logics and some of the early attempts to fit these semantic systems together in Montague 1973, Fine 1977, and Kaplan 1989. This module will conclude with Dor and Goodman 2020 paper along with an alternative bimodal system that I have developed. (3) The third module will begin with the intensional semantics for counterfactuals developed by Stalnaker 1968 and Lewis 1973. We will then move to review some of the early criticisms by Fine 1975 and others, comparing the hyperintensional account that Fine 2012 offers as an alternative. I will then present the extension that I have developed of Fine's semantics for counterfactuals. (4) The fourth module will close by considering hyperintensional semantic theories and their logics for propositional identity, subject-matter, essence, ground, and logical subtraction.

## Overview

The seminar will be held in the Stata Building, room `32-D831` at MIT.

The seminar will be divided into the four modules indicated below.
Readings will be arranged chronologically where primary readings for each week will be in **bold**.
All readings will be accessible on the [private repository](https://github.com/benbrastmckie/ModalHistoryPrivate) for the seminar.
Some readings may be subject to change.

Students taking the course for credit may choose between the _formal track_ which fulfills the logic requirement and the _historical track_ which does not.
All students will be required to have a GitHub account to access the private repository for the course.
Please send me an email from the same email address that you use to sign into GitHub to gain access.
Add a star to this repository so that I can verify that you have created an account and see who is taking the course.

There are two tracks to choose from where grades will be determined accordingly:

### Historical Track

- [10%] Present a topic in class (15min), revising the class notes for that week
- [10%] Open two [issues](https://github.com/benbrastmckie/ModalHistory/issues) to raise a substantial question or make an observation
- [80%] Write a final term paper (5k words)

### Formal Track

- [10%] Present a topic in class (15min), revising the class notes for that week
- [10%] Open two [issues](https://github.com/benbrastmckie/ModalHistory/issues) to raise a substantial question or make an observation
- [40%] Make substantial contributions to all eight collaborative problem sets
- [40%] Complete and present a final project by either:
  - Presenting and discussing an important formal result
  - Using the model-checker to implement a semantics

### Tooling

Although optional for students on the _historical track_, the [first problem set](https://github.com/benbrastmckie/ModalHistoryPrivate/blob/master/problem_sets/01_pset/tooling.md) for students on the _formal track_ will consist of:

- Installing either [VSCodium](https://github.com/benbrastmckie/VSCodium), [NeoVim](https://github.com/benbrastmckie/.config), or equivalent for writing in markdown, LaTeX, as well as using the [model-checker](https://github.com/benbrastmckie/ModelChecker) to complete the final problem sets at the end of the course (instructions will be provided).
- Accepting the invitation to the private problem set repository for this course, adding an SSH key.
- Using Git to push changes to the installation documentation (collaboration is encouraged on all problem sets).

> As the problem sets are collaborative, it will be important to all be on the same page using Git to push and pull changes to markdown, LaTeX, and Python files (no prior background is required).

## Module 1: Modal Logic

This module focuses on the advantages and limitations of the purely syntactic approaches to modal logic inspired by _Principia Mathematica_ as well as the challenge of interpreting the modal operators that the early pioneers faced.

### [Week 00: Introduction and Origins](https://github.com/benbrastmckie/ModalHistory/blob/master/1_modal_logic/00_week/00_week.md)

This week will present the ambitions for this seminar before presenting the system of material implication developed in _Principia Mathematica_ and Lewis' early essays motivating the development of a logic of strict implication by appealing to the paradoxes of material implication.

- **[pp. 102-4, 108] Russell, Bertrand, and Alfred North Whitehead. _Principia Mathematica_. 2nd ed. Vol. 1. Cambridge: Cambridge University Press, 1910.**
- **Lewis, C. I. “Implication and the Algebra of Logic.” Mind XXI, no. 84 (1912): 522–31. https://doi.org/10.1093/mind/XXI.84.522.**
- Lewis, C. I. “Interesting Theorems in Symbolic Logic.” The Journal of Philosophy, Psychology and Scientific Methods 10, no. 9 (April 1913): 239–42. https://doi.org/10.2307/2012471.
- Lewis, C. I. “The Issues Concerning Material Implication.” The Journal of Philosophy, Psychology and Scientific Methods 14, no. 13 (June 1917): 350–56. https://doi.org/10.2307/2940255.

### [Week 01: Lewis & Langford's Modal Systems](https://github.com/benbrastmckie/ModalHistory/blob/master/1_modal_logic/01_week/01_week.md)

This week will focus on the proof systems that Lewis and Langford developed for modal logic.

> Problem Set #1: Tooling

- Lewis, C. I. “A New Algebra of Implications and Some Consequences.” The Journal of Philosophy, Psychology and Scientific Methods 10, no. 16 (July 1913): 428–38. https://doi.org/10.2307/2012900.
- ———. “Alternative Systems of Logic.” The Monist 42, no. 4 (October 1932): 481–507.
- ———. “Strict Implication–An Emendation.” The Journal of Philosophy, Psychology and Scientific Methods 17, no. 11 (May 1920): 300–302. https://doi.org/10.2307/2940598.
- **———. “The Calculus of Strict Implication.” Mind, New Series, 23, no. 90 (April 1914): 240–47.**
- ———. “The Matrix Algebra for Implications.” The Journal of Philosophy, Psychology and Scientific Methods 11, no. 22 (October 1914): 589–600. https://doi.org/10.2307/2012652.
- ———. “The Structure of Logic and Its Relation to Other Systems.” The Journal of Philosophy 18, no. 19 (September 1921): 505–16. https://doi.org/10.2307/2939309.
- **Lewis, C. I., and C. H. Langford. Symbolic Logic. New York: Century Company, 1932.**
- McKinsey, J. C. C. “A Reduction in Number of the Postulates for C. I. Lewis’ System of Strict Implication.” Bulletin of the American Mathematical Society 40, no. 6 (1934): 425–28. https://doi.org/10.1090/S0002-9904-1934-05881-6.

### [Week 02: Quantified Modal Logic](https://github.com/benbrastmckie/ModalHistory/blob/master/1_modal_logic/02_week/02_week.md)

This week will focus on the logical form of modal locutions and the quantified modal systems pioneered by Ruth Barcan Marcus.

- Fitch, Frederic B. “Modal Functions in Two-Valued Logic.” The Journal of Symbolic Logic 2, no. 23 (1937): 125–28.
- ———. “Note on Modal Functions.” The Journal of Symbolic Logic 4, no. 3 (1939): 115–16.
- McKinsey, J. C. C. “Review: Frederic B. Fitch, Note on Modal Functions.” The Journal of Symbolic Logic 5, no. 1 (1940): 31.
- **Quine, W. V. “Notes on Existence and Necessity.” The Journal of Philosophy 40, no. 5 (1943): 113–27. https://doi.org/10.2307/2017458.**
- **Church, Alonzo. Review of Review of Notes on Existence and Necessity, by Willard V. Quine. The Journal of Symbolic Logic 8, no. 1 (1943): 45–47. https://doi.org/10.2307/2267994.**
- McKinsey, J. C. C. “On the Syntactical Construction of Systems of Modal Logic.” The Journal of Symbolic Logic 103 (1945): 83–94.
- Fitch, Frederic B. “Review: J. C. C. McKinsey, On the Syntactical Construction of Systems of Modal Logic.” The Journal of Symbolic Logic 11, no. 3 (1946): 98–99.
- **Barcan, Ruth C. "A Functional Calculus of First Order Based on Strict Implication." The Journal of Symbolic Logic 11, no. 4 (1946): 115–18. https://doi.org/10.2307/2269159.**
- ———. "The Deduction Theorem in a Functional Calculus of First Order Based on Strict Implication." Journal of Symbolic Logic 11, no. 4 (1946): 115–18.
- **Quine, W. V. "Review: Ruth C. Barcan, A Functional Calculus of First Order Based on Strict Implication." The Journal of Symbolic Logic 11, no. 3 (September 1946): 96–97. https://doi.org/10.2307/2266766.**

### [Week 03: Quine's Critique](https://github.com/benbrastmckie/ModalHistory/tree/master/1_modal_logic/03_week)

This week will focus on the philosophical criticisms that Quine raised against the development of modal logic.

> Problem Set #2: Axiomatic Proofs

- **Barcan, Ruth C. "The Identity of Individuals in a Strict Functional Calculus of Second Order." The Journal of Symbolic Logic 12, no. 1 (1947): 12–15.**
- **Quine, W. V. "The Problem of Interpreting Modal Logic." The Journal of Symbolic Logic 12, no. 2 (1947): 43–48. https://doi.org/10.2307/2267247.**
- **Barcan, Ruth C. "Review: W. V. Quine, The Problem of Interpreting Modal Logic." The Journal of Symbolic Logic 12, no. 4 (1947): 139–41.**
- Quine, W. V. "On What There Is." The Review of Metaphysics 2, no. 5 (September 1948): 21–38.
- Smullyan, Arthur Francis. "Modality and Description." The Journal of Symbolic Logic 13, no. 1 (1948): 31–37.
- Barcan, Ruth C. "Review: Arthur Francis Smullyan, Modality and Description." The Journal of Symbolic Logic 13, no. 3 (1948): 149–50.
- Fitch, Frederic B. "The Problem of the Morning Star and the Evening Star." Philosophy of Science 16, no. 2 (April 1949): 137–41.
- Barcan, Ruth C. "Strict Implication, Deducibility and the Deduction Theorem." The Journal of Symbolic Logic 18, no. 3 (1953): 234–36.
- **Quine, W. V. "Three Grades of Modal Involvement." In Proceedings of the 11th International Congress of Philosophy, 14:65–81. Amsterdam: North-Holland, 1953.**

## Module 2: Intensional Semantics

> Semantic approaches to interpretational and metaphysical readings of the modal operators.

### [Week 04: Carnap's Semantics](https://github.com/benbrastmckie/ModalHistory/blob/master/2_intensional_semantics/04_week/04_week.md)

### [Week 05: Kripke's Semantics](https://github.com/benbrastmckie/ModalHistory/blob/master/2_intensional_semantics/05_week/05_week.md)

> Problem Set #3: Semantic Proofs

### [Week 06: Prior and Thomason's Semantics](https://github.com/benbrastmckie/ModalHistory/blob/master/2_intensional_semantics/06_week/06_week.md)

### [Week 07: Perpetuity Principles](https://github.com/benbrastmckie/ModalHistory/blob/master/2_intensional_semantics/07_week/07_week.md)

> Problem Set #4: Bimodal Logic

### Week 08: Spring Break (no class)

### [Week 09: "The Construction of Possible Worlds" (Brast-McKie)](https://github.com/benbrastmckie/ModalHistory/blob/master/2_intensional_semantics/09_week/09_week.md)

## Module 3: Counterfactual Conditionals

> The semantics and logic for counterfactual conditionals.

### [Week 10: Similarity Semantics](https://github.com/benbrastmckie/ModalHistory/blob/master/3_counterfactual_conditionals/10_week/10_week.md)

> Problem Set #5: Counterfactual Semantics

### [Week 11: Imposition Semantics](https://github.com/benbrastmckie/ModalHistory/blob/master/3_counterfactual_conditionals/11_week/11_week.md)

### [Week 12: "Counterfactual Worlds" (Brast-McKie)](https://github.com/benbrastmckie/ModalHistory/blob/master/3_counterfactual_conditionals/12_week/12_week.md)

> Problem Set #6: Model-Checker

## Module 4: Constitutive Explanation

> Hyperintensional semantics and logic for constitutive explanatory operators and logical subtraction

### [Week 13: Identity and Aboutness (Brast-McKie)](https://github.com/benbrastmckie/ModalHistory/tree/master/4_constitutive_explanation/13_week)

> Problem Set #7: Hyperintensional Semantics

### [Week 14: Necessary and Sufficient](https://github.com/benbrastmckie/ModalHistory/tree/master/4_constitutive_explanation/14_week)

> Problem Set #8: Programmatic Semantics

### [Week 15: Formal Track Presentations](https://github.com/benbrastmckie/ModalHistory/tree/master/4_constitutive_explanation/15_week)

Presentations are intended to provide a brief (15min) and accessible overview of each project.
