# Problem Sets

> The problem sets follow the [Logic Notes](https://github.com/benbrastmckie/LogicNotes/blob/main/LogicNotesCurrent.pdf) which provide essential theoretical background for the course

In addition to the relevant portion of the Logic Notes and the collaboration overview, please read the instructions for each week linked below.
These instructions will provide some discussion of the problem set for that week.

Here are some general points about collaboration in LaTeX using Git.

## Collaboration

Work together to complete the solutions for each week by observing the following protocols:

> 1. Make sure to pull changes (sync) before starting to work on any problems
> 2. Add your name to the problems you want to work on, pushing changes immediately to "check out" the problems
> 3. If a problem has been checked out once, make a copy of the solution block below to contribute your solution below
> 4. If there are already two people working on a problem, try to find another problem to work on
> 5. If you make some progress (even partial) and get stuck, push changes for others to see/help/etc.
> 6. If you have questions or comments, please open a new issue (it's possible to link line numbers) 
> 7. It is best practice to have one sentence per numbered line, making it easier to add comments
> 8. If possibly, try to avoid breaking formal expressions across lines to improve readability
> 9. I will comment on your solutions, adding my name to the reviewers (feel free to add comments/questions as well)
> 10. If the comments have been addressed or no longer relevant, feel free to remove comments
> 11. If you want to add comments, make sure to create a new line below to do so (this will help avoid merge conflicts)
> 12. All the defined commands can be found in [assets/notation.sty](../problem_sets/assets/notation.sty) but feel free to use what you like
> 13. I will try to include comments alongside the definitions of the commands and environments in notation.sty to explain their use
> 14. Make sure that the document builds without errors before pushing changes
> 15. Please try to choose a diversity of problem types to work on each week

If one solution has already been provided, you are welcome to try to improve on that solution, writing your own version below, or else presenting an alternative since it can be helpful to get different perspectives on the same problem.
For instance, if someone has written a proof that only appeals to basic axioms and rules, you might try to provide a more economical version which appeals to previously established results, or _vice versa_ since having both types of proof is helpful.
The aim here is not to one-up each other but to apply the powers of our collective intelligence to complete the problem set to a far greater degree of rigor than would be practical for any one individual on their own so that we all benefit from each other's efforts.

You are invited to work together however you see fit.
This could mean looking at the problems individually and then convening with others to try to unlock them, or else writing your own solutions, pushing changes, and opening an issue to discuss online.
There are typically many different solutions, and often something to learn from each.
Solutions that are partial or sketchy can still be very helpful to others who are attempting the problems.
Additionally, others may see your partial solution and be able to help you fill in the gaps.

In addition to solving problems, you will also be asked to check others work.
If you check a problem that someone else wrote and it looks good, please add your name in brackets next to theirs in the list of collaborators.
If you review a solution that does not look right, please add in-line comments or raise this as an issue.
Note that some of these problems are harder than others.

There is no exam for this class, so the point here is just to learn as much as you can from the problems and from each other in completing them (I will also help in the issues).
I don't want anyone to feel stressed that they are not contributing enough, but I also want everyone to contribute and to be engaged learning together.
If you are new to writing proofs, keep in mind that producing solutions is not all of it.
Rather, asking good questions is often a very helpful contribution as this will help to surface issues that might otherwise go overlooked or under-explained.
It is also important to remember that we are all coming from different formal backgrounds, where both asking and trying to answer questions are some of the best means by which to learn.

If you have any general or specific questions, feel free to open an [issue](https://github.com/benbrastmckie/ModalHistory/issues) which is reserved for collaboration on problem sets (including technical problems).
Also note that issues should strive to be separated by topic, e.g., one issue per problem unless it is the same specific issue in multiple problems.
It is a low-stakes judgment call where to divide issues, so don't worry too much about it.

## Git

You can find some information about Git [here](https://github.com/benbrastmckie/VSCodium/blob/master/docs/git.md) as well as many other places online.
You might quiz an LLM about Git, or find a short tutorial to watch on YouTube if Git is new and you have questions.
We will only be using the very basics which I'll outline as the following workflow:

> - Open VSCodium (or other IDE) and go to your project (you can save these as a workspace if you like)
> - Open the Source Control in the left sidebar (or press `Ctrl+Shift+G`)
> - Click `Sync Changes` or the `⋯` (three dots) to pull down the most recent changes to the repo
> - Find the problems you want to work on, adding your name to each (or a copy if someone already has)
> - Save the document and you'll see your changed files under "Changes"
> - Hover over "Changes" and click the `+` icon to stage all changes
> - Type a commit message in the text box at the top
> - Click the ✓ (checkmark) icon to commit
> - Click `Sync Changes` or the `⋯` (three dots) menu and select "Push" others can see the problems you are working on
> - Do your best to work on the problems
> - If you finish a problem (or get stuck), save and commit your changes, syncing and pushing as before
> - Others will then be able to see the progress that you made which may help
> - If you get stuck, pushing changes makes your work easy to reference in issues (you can even link line numbers)
> - Then proceed to work on other problems

It might feel a little clunky at first but should end up pretty seamless with a bit of practice.
If you think about the alternative (emailing `.tex` files around), this is a pretty elegant way to collaborate.
This same workflow is also great for personal projects, allowing you to backup and search the full history, add branches, and lots more.

### Merge Conflicts

Although the protocols described above should help to avoid merge conflicts, these will likely happen.
This is where you sync changes, pulling down the most recent version before working on a problem.
Someone else then goes and does the same thing, pulling down those changes and working on the _same_ problem.
Maybe you forgot to add your name to the problem, pushing those changes before setting about working on it, and so they had no way of knowing that you were working on it.
One of you finishes before the other and pushes changes.
Then the other goes to push their changes and crash!

But don't worry, nothing is broken or lost, it's just a pain.
What Git will do will be to add markers to indicate the conflicting versions of the same lines.
If you got the merge conflict, that means the version you are trying to contribute is conflicting with the version on the repo and so you will have to go and pick which version the repo should include.
When you take a look at the conflict, the best thing to do is to remove the markers and try to preserve both your solution and the solution that was already up there.
Once all the markers are removed, you will be able to save, commit, and push as before.

If this seems daunting, you can open an issue to get my help, or it might help to get an LLM to describe the situation you are facing and talk you through what to do step-by-step.
It honestly shouldn't take more than a minute to fix.
If you feel like somehow you totally messed things up, again don't worry since we can always revert to older commits (this is something I will do if need be).
At most, you will have lost the changes that you were trying to push, but that is if you accidentally delete your changes since Git won't do this for you.

To avoid this scenario, be sure to add your name to the problems you want to work on, saving and pushing these changes before starting to work on the problems themselves.
Then you can take the time you need to write up you solution, pushing changes before going on to work on another problem.

## Problem Sets

### [Problem Set #1: Tooling](01_tooling/tooling.md)

> Problem Set #1: Tooling (due prior to class week 01)

An introduction to essential tools for the course: setting up a text editor (VSCodium/NeoVim), installing LaTeX, configuring Git with SSH authentication, and practicing the Git workflow.
This problem set ensures everyone has the necessary technical foundation to collaborate on future assignments.

Here are the [instructions](01_tooling/tooling.md) for this problem set.

### [Problem Set #2: Axiomatic Proofs](02_axiomatic_proofs/axiomatic_proofs.md)

> Problem Set #2: Axiomatic Proofs (due prior to class week 03)

Explores classical propositional logic using Hilbert's axiom system which is then extended to propositional modal logics.
This problem set includes metalinguistic abbreviations, derived metarules, and axiomatic proofs, gradually building a stock of derivations to tackle increasingly complex problems.

Here are the [instructions](02_axiomatic_proofs/axiomatic_proofs.md) for this problem set, the [TeX file](02_axiomatic_proofs/02_solutions.tex), and the [PDF](02_axiomatic_proofs/02_solutions.pdf).

### [Problem Set #3: Semantic Proofs](03_semantic_proofs/semantic_proofs.md)

> Problem Set #3: Semantic Proofs (due prior to class week 05)

Focuses on semantics for propositional modal logic, examining natural connections between logical operators and set-theoretic operations.
Students explore intensional frames, create countermodels, and test the soundness of various modal proof systems through mechanical proofs and equivalence demonstrations.

Here are the [instructions](03_semantic_proofs/semantic_proofs.md) for this problem set, the [TeX file](03_semantic_proofs/03_solutions.tex), and the [PDF](03_semantic_proofs/03_solutions.pdf).

### [Problem Set #4: Tense Logic](04_tense_logic/tense_logic.md)

> Problem Set #4: Tense Logic (due prior to class week 06)

Examines propositional tense logic semantics with both basic tense operators and inevitability operators.
Students work on regimenting English sentences, analyzing temporal frame constraints, providing countermodels to tense logic axioms, and evaluating semantic indeterminacy where sentences are evaluated at both a history and time.

Here are the [instructions](04_tense_logic/tense_logic.md) for this problem set, the [TeX file](04_tense_logic/04_solutions.tex), and the [PDF](04_tense_logic/04_solutions.pdf).

### [Problem Set #5: Bimodal Logic](05_bimodal_logic/bimodal_logic.md)

> Problem Set #5: Bimodal Logic (due prior to class week 08)

Explores propositional bimodal logic semantics through three main sections: comparing Kaplan and Montague's Cartesian semantics, investigating the task semantics for bimodal language, and extending the framework to include operators for the open past, future, and inevitability, concluding with mixed modal operators.

Here are the [instructions](05_bimodal_logic/bimodal_logic.md) for this problem set, the [TeX file](05_bimodal_logic/05_solutions.tex), and the [PDF](05_bimodal_logic/05_solutions.pdf).

### [Problem Set #6: Model-Checker](06_model_checker/model_checker.md)

> Problem Set #6: Model-Checker (due prior to class week 09)

Introduces computational methods for modal logic through installation and use of the model-checker tool powered by the SMT solver Z3.
Students learn to create model-checker projects, run examples, and understand how to evaluate logical consequences and find countermodels, shifting from manual proofs to automated verification.

Here are the [instructions](06_model_checker/model_checker.md) for this problem set.

### [Problem Set #7: Bimodal Semantics](07_bimodal_semantics/bimodal_semantics.md)

> Due before Apr 18 (Week 11)

Applies the model-checker to bimodal semantics through three tasks: exploring the existing documentation and test examples, creating and testing new examples to evaluate the model-checker's performance, and extending the bimodal language by defining a new operator using the existing operators, providing practical experience with computational semantic tools.

Here are the [instructions](07_bimodal_semantics/bimodal_semantics.md) for this problem set.

### [Problem Set #8: State Semantics](08_state_semantics/state_semantics.md)

> Due before class on Apr 28 (Week 12)

Uses the model-checker to explore state semantics for counterfactual conditionals, focusing on interpreting hyperintensional models.
Students analyze existing counterfactual countermodels, create their own examples with customized settings, test logical equivalences between operators, and enhance their ability to translate between formal models and natural language examples.

Here are the [instructions](08_state_semantics/state_semantics.md) for this problem set.

