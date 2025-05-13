# 24.711: The Modern History of Modal Logic

> A graduate course in _Philosophical Logic_ at MIT covering the modern history of modal logic.

**Description:** The seminar will cover the modern history of modal logic, focusing on the development of both its proof theories and semantic systems.
(1) The first module will begin with C.I. Lewis' systems of strict implication 1912 - 1932, focusing on the early motivations and interpretations.
The module will conclude with Ruth Barcan Marcus' first-order extensions of the systems of strict implication 1946 and the objections raised by Quine 1943 - 1953 that modal logic will lead back into the "jungle of Aristotelian metaphysics".
(2) The second module will focus on the development of intensional semantics by comparing Carnap 1946 and Kripke's 1963 accounts.
We will then consider Prior 1967 and Thomason's 1970 tense logics and some of the attempts to fit these semantic systems together by Montague 1973 and Kaplan 1989.
This module will conclude with an alternative bimodal system that I am developing.
(3) The third module will begin with the intensional semantics for counterfactuals developed by Stalnaker 1968 and Lewis 1973.
We will then move to review some of the early criticisms by Fine 1975 and others, comparing the hyperintensional account that Fine 2012 offers as an alternative.
I will then present the extension that I have developed of Fine's semantics for counterfactuals, extending this system further to accommodate tensed counterfactuals.
(4) The fourth module will close by considering hyperintensional semantic theories more generally and their logics for propositional identity, subject-matter, essence, ground, and logical subtraction.

## Overview

```bash
ModalHistory/
├── 1_modal_logic/                 # MODULE 1 MATERIALS
│   ├── 00_week/                   # Introduction and Origins
│   ├── 01_week/                   # Early Modal Systems
│   └── 02_week/                   # Quantified Modal Logic
├── 2_intensional_semantics/       # MODULE 2 MATERIALS
│   ├── 03_week/                   # Carnap and Kripke
│   ├── 04_week/                   # Prior and Thomason
│   ├── 05_week/                   # Montague and Kaplan
│   └── 06_week/                   # The Construction of Possible Worlds
├── 3_counterfactual_conditionals/ # MODULE 3 MATERIALS
│   ├── 08_week/                   # Similarity and Imposition
│   ├── 09_week/                   # Counterfactual Worlds
│   └── 10_week/                   # Programmatic Semantics
├── 4_constitutive_explanation/    # MODULE 4 MATERIALS
│   ├── 12_week/                   # Identity and Aboutness
│   ├── 13_week/                   # Necessary and Sufficient
│   └── 14_week/                   # Formal Track Presentations
├── final_projects/                # FINAL PROJECT MATERIALS AND EXAMPLES
├── problem_sets/                  # PROBLEM SETS AND SOLUTIONS
│   ├── 01_tooling/                # Git and LaTeX setup
│   ├── 02_axiomatic_proofs/       # Axiomatic proof systems
│   ├── 03_semantic_proofs/        # Model theory and semantics
│   ├── 04_tense_logic/            # Temporal logic
│   ├── 05_bimodal_logic/          # Multiple modalities
│   ├── 06_model_checker/          # Programmatic verification
│   ├── 07_bimodal_semantics/      # Advanced semantic systems
│   └── 08_state_semantics/        # Hyperintensional semantics
└── README.md                      # COURSE OVERVIEW AND SYLLABUS
```

### Time and Location

The seminar will be held in the Stata Building, room `32-D831` at MIT on Mondays from 2-5pm.
I am always happy to meet after the seminar and to hold office hours by appointment at `32-D962`.

### Further Particulars

The seminar will be divided into the four modules indicated below.
The readings for each week will be provided below and accessible on the [private repository](https://github.com/benbrastmckie/ModalHistoryPrivate) for the seminar.
Readings for each week will be arranged chronologically where primary readings will be in **bold**.

There are two tracks for this course where grades for the seminar will be calculated as below.
Students taking the course for credit may choose between the _formal track_ which fulfills the logic requirement and the _historical track_ which does not.

Although optional for the _historical track_ I will be revising and expanding these [Logic Notes](https://github.com/benbrastmckie/LogicNotes) for this course.
The material presented here will not be the focus of the seminar meetings, though certain core topics relevant to both tracks will be covered in an accessible manner.

If you are looking for further background in propositional and first-order logic, the [ForAllX textbook](https://github.com/benbrastmckie/ForAllX) provides an introduction.
See Chapter 0 for a brief introduction to the subject-matter of logic, describing what it is that logic aims to study.

### Historical Track

- [10%] Present a topic in class, revising the class notes for that week
- [10%] Open five [issues](https://github.com/benbrastmckie/ModalHistory/issues) in this repo to post a substantial question or comment
- [80%] Write a final term paper (5k words)

### Formal Track

- [10%] Present a topic in class, revising the class notes for that week
- [10%] Open five [issues](https://github.com/benbrastmckie/ModalHistory/issues) in this repo to post a substantial question or comment
- [40%] Make contributions to all eight collaborative problem sets 
- [40%] Complete and present a final project by either:
  - Presenting and discussing an important formal result
  - Using the model-checker to implement a semantics
  - Other projects with approval

In addition to the weekly readings, the [problem sets](/problem_sets) will draw from the [Logic Notes](https://github.com/benbrastmckie/LogicNotes/blob/main/LogicNotesCurrent.pdf) (changes are underway).
It will be important to be able to push and pull changes with Git so that I can see your contributions to the eight collaborative problem sets (details on how to do this is covered in the first problem set).

### Tooling

Although optional for the _historical track_, the [first problem set](/problem_sets/01_tooling/tooling.md) for students on the _formal track_ will consist of:

- Installing either [VSCodium](https://github.com/benbrastmckie/VSCodium), [NeoVim](https://github.com/benbrastmckie/.config), or equivalent for writing in markdown, LaTeX, as well as using the [model-checker](https://github.com/benbrastmckie/ModelChecker) to complete the final problem sets at the end of the course (instructions will be provided).
- Install LaTeX on your machine if you have not already done so.
- Use Git to push changes to the private repository, adding an SSH key as needed.

This is a great opportunity for upgrading you tool kit, gaining some experience using Git to collaborate if you have not done so before.
No prior experience is required.

### Presentations

> In class presentations differ from the presentation of a final project for the _formal track_.

The presentations in class may consist of leading a discussion about a particular topic or paper or presenting the outline of a formal result of general significance in an accessible way.
I have begun to gather papers for two potential topics to present in [week 1](1_modal_logic/01_week/01_week.md).
Presenters for each week will also be responsible for contributing to the class notes for that week.

### Final Projects

For students on the formal track, the final project is a significant component of the course. For guidelines, templates, and examples, please see the [Final Projects](/final_projects/README.md).

The final project constitutes 40% of the grade for the formal track and 80% for the historical track. Students will present their project outlines in the final seminar.

#### Historical Track

- Write a 5,000 word term paper on course literature or related topics
- Brief presentation (~10 minutes) in final seminar
- Schedule meeting to discuss topic before preparing outline

#### Formal Track (Choose One)

- **Mathematical**: Present and explain an important formal result
  - Focus on classic results in one of the logics we covered (or related)
  - Emphasis on clear presentation and interpretation
- **Programmatic**: Conduct semantic studies using the model-checker
  - Build and document a model-checker project
  - Analyze countermodels and logical consequences
  - Present findings in Jupyter notebook

## Problem Sets

> Eight problem sets to be completed collectively by those on the formal track

The problem sets follow the [Logic Notes](https://github.com/benbrastmckie/LogicNotes/blob/main/LogicNotesCurrent.pdf) which I will be revising and extending before each assignment.
These notes are extremely terse, so if there are parts that don't make sense, please raise a question in the issues and we can chat about it there.
This will help to include others in the conversation and help me to improve the notes.

The problem sets are to be completed in collaboration with your peers by pushing and pulling changes with Git.
Here is an [example](problem_sets/02_axiomatic_proofs/02_solutions.pdf) of a proof based problem set.

More information is provided in the [Problem Sets](/problem_sets/README.md) document about how to use Git to work effectively together.

## Module 1: Modal Logic

This module focuses on the advantages and limitations of the purely syntactic approaches to modal logic inspired by _Principia Mathematica_ as well as the challenge of interpreting the modal operators that the early pioneers faced.

### [Week 00: Introduction and Origins](1_modal_logic/00_week/00_week.md) (Feb 03)

> Problem Set #1: Tooling (due prior to class week 01)

This week will present the ambitions for this seminar before presenting the system of material implication developed in _Principia Mathematica_ and Lewis' early essays motivating the development of a logic of strict implication by appealing to the paradoxes of material implication.

> Entries are arranged in chronological order where **bold** items are primary.

- **[pp. 91, 94-104] Russell, Bertrand, and Alfred North Whitehead. _Principia Mathematica_. 2nd ed. Vol. 1. Cambridge: Cambridge University Press, 1910.**
- **Lewis, C. I. "Implication and the Algebra of Logic." Mind XXI, no. 84 (1912): 522–31. https://doi.org/10.1093/mind/XXI.84.522.**
- Lewis, C. I. "Interesting Theorems in Symbolic Logic." The Journal of Philosophy, Psychology and Scientific Methods 10, no. 9 (April 1913): 239–42. https://doi.org/10.2307/2012471.
- Lewis, C. I. "The Issues Concerning Material Implication." The Journal of Philosophy, Psychology and Scientific Methods 14, no. 13 (June 1917): 350–56. https://doi.org/10.2307/2940255.

### [Week 01: Early Modal Systems](1_modal_logic/01_week/01_week.md) (Feb 10)

> Problem Set #2: Axiomatic Proofs (due prior to class week 03)

This week will focus on the proof systems that Lewis and Langford developed for modal logic, as Barcan Marcus' extension to the first-order.

- Lewis, C. I. "A New Algebra of Implications and Some Consequences." The Journal of Philosophy, Psychology and Scientific Methods 10, no. 16 (July 1913): 428–38. https://doi.org/10.2307/2012900.
- ———. "Alternative Systems of Logic." The Monist 42, no. 4 (October 1932): 481–507.
- ———. "Strict Implication–An Emendation." The Journal of Philosophy, Psychology and Scientific Methods 17, no. 11 (May 1920): 300–302. https://doi.org/10.2307/2940598.
- **———. "The Calculus of Strict Implication." Mind, New Series, 23, no. 90 (April 1914): 240–47.**
- ———. "The Matrix Algebra for Implications." The Journal of Philosophy, Psychology and Scientific Methods 11, no. 22 (October 1914): 589–600. https://doi.org/10.2307/2012652.
- ———. "The Structure of Logic and Its Relation to Other Systems." The Journal of Philosophy 18, no. 19 (September 1921): 505–16. https://doi.org/10.2307/2939309.
- **[Appendix] Lewis, C. I., and C. H. Langford. Symbolic Logic. New York: Century Company, 1932.**
- McKinsey, J. C. C. "A Reduction in Number of the Postulates for C. I. Lewis' System of Strict Implication." Bulletin of the American Mathematical Society 40, no. 6 (1934): 425–28. https://doi.org/10.1090/S0002-9904-1934-05881-6.
- **Barcan, Ruth C. "A Functional Calculus of First Order Based on Strict Implication." The Journal of Symbolic Logic 11, no. 4 (1946): 115–18. https://doi.org/10.2307/2269159.**
- ———. "The Deduction Theorem in a Functional Calculus of First Order Based on Strict Implication." Journal of Symbolic Logic 11, no. 4 (1946): 115–18.

### [Week 02: Quantified Modal Logic](1_modal_logic/02_week/02_week.md) (TUESDAY, Feb 18 due to President's Day)

This week will focus on the quantified modal systems pioneered by Ruth Barcan Marcus and Quine's philosophical criticisms.

- Fitch, Frederic B. "Modal Functions in Two-Valued Logic." The Journal of Symbolic Logic 2, no. 23 (1937): 125–28.
- ———. "Note on Modal Functions." The Journal of Symbolic Logic 4, no. 3 (1939): 115–16.
- McKinsey, J. C. C. "Review: Frederic B. Fitch, Note on Modal Functions." The Journal of Symbolic Logic 5, no. 1 (1940): 31.
- **Quine, W. V. "Notes on Existence and Necessity." The Journal of Philosophy 40, no. 5 (1943): 113–27. https://doi.org/10.2307/2017458.**
- Church, Alonzo. Review of Review of Notes on Existence and Necessity, by Willard V. Quine. The Journal of Symbolic Logic 8, no. 1 (1943): 45–47. https://doi.org/10.2307/2267994.
- McKinsey, J. C. C. "On the Syntactical Construction of Systems of Modal Logic." The Journal of Symbolic Logic 103 (1945): 83–94.
- Fitch, Frederic B. "Review: J. C. C. McKinsey, On the Syntactical Construction of Systems of Modal Logic." The Journal of Symbolic Logic 11, no. 3 (1946): 98–99.
- **Barcan, Ruth C. "A Functional Calculus of First Order Based on Strict Implication." The Journal of Symbolic Logic 11, no. 4 (1946): 115–18. https://doi.org/10.2307/2269159.**
- ———. "The Deduction Theorem in a Functional Calculus of First Order Based on Strict Implication." Journal of Symbolic Logic 11, no. 4 (1946): 115–18.
- **Quine, W. V. "Review: Ruth C. Barcan, A Functional Calculus of First Order Based on Strict Implication." The Journal of Symbolic Logic 11, no. 3 (September 1946): 96–97. https://doi.org/10.2307/2266766.**
- Barcan, Ruth C. "The Identity of Individuals in a Strict Functional Calculus of Second Order." The Journal of Symbolic Logic 12, no. 1 (1947): 12–15.
- **Quine, W. V. "The Problem of Interpreting Modal Logic." The Journal of Symbolic Logic 12, no. 2 (1947): 43–48. https://doi.org/10.2307/2267247.**
- Smullyan, Arthur Francis. "Review: W. V. Quine, The Problem of Interpreting Modal Logic." The Journal of Symbolic Logic 12, no. 4 (1947): 139–41.
- Quine, W. V. "On What There Is." The Review of Metaphysics 2, no. 5 (September 1948): 21–38.
- Barcan, Ruth C. "Strict Implication, Deducibility and the Deduction Theorem." The Journal of Symbolic Logic 18, no. 3 (1953): 234–36.
- Quine, W. V. "Three Grades of Modal Involvement." In Proceedings of the 11th International Congress of Philosophy, 14:65–81. Amsterdam: North-Holland, 1953.

## Module 2: Intensional Semantics

Semantic approaches to interpretational and metaphysical readings of the modal operators.

### [Week 03: Carnap and Kripke](2_intensional_semantics/03_week/03_week.md) (Feb 24)

> Problem Set #3: Modality (due prior to class week 05)

- Carnap, Rudolf. Introduction to Semantics. Harvard University Press, 1942.
- **Carnap, Rudolf. "Modalities And Quantification." The Journal of Symbolic Logic, 1946.**
- Kripke, Saul A. "A Completeness Theorem in Modal Logic." The Journal of Symbolic Logic 24, no. 1 (March 1959): 1–14. https://doi.org/10.2307/2964568.
- **———. "Semantical Analysis of Modal Logic I Normal Modal Propositional Calculi." Mathematical Logic Quarterly 9, no. 5–6 (January 1963): 67–96. https://doi.org/10.1002/malq.19630090502.**

### [Week 04: Prior and Thomason](2_intensional_semantics/04_week/04_week.md) (Mar 3)

> Problem Set #4: Tense (due prior to class week 06)

- Kripke, Saul A. "Letter from Saul Kripke to A. N. Prior, Sept. 3, 1958," September 3, 1958.
- ———. "Letter from Saul Kripke to A.N. Prior, Oct. 13, 1958," October 13, 1958.
- Prior, Arthur N. Past, Present and Future. Oxford, New York: Oxford University Press, 1967.
- ———. Time and Modality. Westport, Conn.: Greenwood Press, 1955.
- **Thomason, Richmond H. "Indeterminist Time and Truth-Value Gaps." Theoria 36, no. 3 (1970): 264–81. https://doi.org/10.1111/j.1755-2567.1970.tb00427.x.**

### [Week 05: Montague and Kaplan](2_intensional_semantics/05_week/05_week.md) (Mar 10)

- **[Sec 3] Montague, Richard. "The Proper Treatment of Quantification in Ordinary English." In Approaches to Natural Language: Proceedings of the 1970 Stanford Workshop on Grammar and Semantics, edited by K. J. J. Hintikka, J. M. E. Moravcsik, and P. Suppes, 221–42. Dordrecht: Springer Netherlands, 1973. https://doi.org/10.1007/978-94-010-2506-5_10.**
- **[XVIII] Kaplan, David. "Demonstratives: An Essay on the Semantics, Logic, Metaphysics and Epistemology of Demonstratives and Other Indexicals." In Themes From Kaplan, edited by Joseph Almog, John Perry, and Howard Wettstein, 481–563. Oxford University Press, 1989.**
- Dorr, Cian, and Jeremy Goodman. "Diamonds Are Forever." Noûs 54, no. 3 (2020): 632–65. https://doi.org/10.1111/nous.12271.

### [Week 06: "The Construction of Possible Worlds" (Brast-McKie)](2_intensional_semantics/06_week/06_week.md) (Mar 17)

> Problem Set #5: Bimodal Logic (due prior to class week 08)

- **Brast-McKie, Benjamin. "The Construction of Possible Worlds" (draft)**

### Week 07: Spring Break (Mar 24)

> No class or assignments

## Module 3: Counterfactual Conditionals

The semantics and logic for counterfactual conditionals.

### [Week 08: Similarity and Imposition](3_counterfactual_conditionals/08_week/08_week.md) (Mar 31)

> Problem Set #6: Model-Checker (due prior to class week 09)

- Stalnaker, Robert C. "A Theory of Conditionals." In Studies in Logical Theory, edited by Nicholas Rescher, 2:98–112. American Philosophical Quarterly Monographs. Oxford: Blackwell, 1968.
- **[pp. 1-19, 48 - 50] Lewis, David. Counterfactuals. Harvard: Harvard University Press, 1973.**
- Bennett, Jonathan. "Counterfactuals and Possible Worlds." Canadian Journal of Philosophy 4, no. 2 (December 1974): 381–402. https://doi.org/10.1080/00455091.1974.10716947.
- **Fine, Kit. "Critical Notice." Mind 84, no. 335 (1975): 451–58.**
- Nute, Donald. "Counterfactuals and the Similarity of Words." The Journal of Philosophy 72, no. 21 (1975): 773–78. https://doi.org/10.2307/2025340.
- Loewer, Barry. "Counterfactuals with Disjunctive Antecedents." The Journal of Philosophy 73, no. 16 (1976): 531–37. https://doi.org/10.2307/2025717.
- Lewis, David. "Counterfactual Dependence and Time's Arrow." Noûs 13, no. 4 (1979): 455–76. https://doi.org/10.2307/2215339.
- **Fine, Kit. "Counterfactuals Without Possible Worlds." Edited by John Smylie. Journal of Philosophy 109, no. 3 (2012): 221–46. https://doi.org/10.5840/jphil201210938.**
- ———. "A Difficulty for the Possible Worlds Analysis of Counterfactuals." Synthese 189, no. 1 (November 1, 2012): 29–57. https://doi.org/10.1007/s11229-012-0094-y.
- ———. "A Theory of Truthmaker Content I: Conjunction, Disjunction and Negation." Journal of Philosophical Logic 46, no. 6 (December 2017): 625–74. https://doi.org/10.1007/s10992-016-9413-y.

### [Week 09: "Counterfactual Worlds" (Brast-McKie)](3_counterfactual_conditionals/09_week/09_week.md) (Apr 7)

> Problem Set #7: Programmatic Semantics (due prior to class week 10)

This week will present the forthcoming paper:

- **Brast-McKie, Benjamin. ["Counterfactual Worlds"](https://github.com/benbrastmckie/ModelChecker/blob/master/Counterfactuals.pdf), JPL**

### [Week 10: Programmatic Semantics](3_counterfactual_conditionals/10_week/10_week.md) (Apr 14)

> Problem Set #8: Hyperintensional Semantics (due prior to class week 12)

- **Davis, Martin, and Hilary Putnam. "A Computing Procedure for Quantification Theory." J. ACM 7, no. 3 (July 1, 1960): 201–15. https://doi.org/10.1145/321033.321034.**

### Week 11: Patriot's Day (no class Apr 21)

## Module 4: Constitutive Explanation

Hyperintensional semantics and logic for constitutive explanatory operators

### [Week 12: Identity and Aboutness (Brast-McKie)](4_constitutive_explanation/12_week/12_week.md) (Apr 28)

This week will present the following paper:

- **Brast-McKie, Benjamin. "Identity and Aboutness." Journal of Philosophical Logic 50, no. 6 (December 1, 2021): 1471–1503. [https://doi.org/10.1007/s10992-021-09612-w](https://doi.org/10.1007/s10992-021-09612-w).**

### [Week 13: Necessary and Sufficient](4_constitutive_explanation/13_week/13_week.md) (May 5)

This week will explore themes related to relevance, essence, ground, and constitutive explanation.

### [Week 14: Formal Track Presentations](4_constitutive_explanation/14_week/14_week.md) (May 12)

Presentations are intended to provide a brief (15min) and accessible overview of each project. For more information on final projects, see the [Final Projects](/final_projects/README.md).
