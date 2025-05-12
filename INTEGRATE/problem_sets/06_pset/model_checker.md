# [Problem Set 06: Model-Checker](https://github.com/benbrastmckie/ModalHistoryPrivate?tab=readme-ov-file#problem-sets)

> Instructions for the problem set for this week

This problem set asks you to install the [model-checker](https://github.com/benbrastmckie/ModelChecker), read the documentation, and run a few tests.
Rather than continuing to write proofs, the aim of this problem set is to begin to familiarize yourself with an alternative methodology.
As this is a work in progress, if there are issues that feel less than totally clear, don't hesitate to open an [issue](https://github.com/benbrastmckie/ModalHistoryPrivate).
It would be helpful to me to know what could be better explained as I work to complete fill in the documentation for this project.

## Model-Checker: An Overview

The model-checker is powered by Z3, a modern SMT solver produced by Microsoft where 'SMT' stands for satisfiability modulo theory.
SMT solvers extend traditional SAT (Boolean satisfiability) solvers by adding support for various theories, hence the 'MT' in 'SMT'.
While SAT solvers work purely with Boolean logic (true/false values), SMT solvers can handle richer domains like integer arithmetic, inequalities, real numbers, arrays, bitvectors, and other mathematical structures.
This makes them more powerful and much more convenient for solving complex logical and mathematical problems.
In particular, we will be concerned to evaluate whether a logical consequence in a given language hold or admit of countermodels.

Just as in the model theories that we have been working in, the model-checker makes use of a number of data types, foremost among these are `strings`, `lists`, `dictionaries`, and `booleans`.
The booleans are just the truth-values `True` and `False` familiar from classical logic and strings are much as they were for us when we defined the sentences within a formal language.
Whereas the `booleans` are basic and the `strings` are built up of valid characters, `lists` and `dictionaries` are constructed from other data types.
For instance, an `example` consist of:

```python
    premises = [ prem_1, prem_2, ... ]

    conclusions = [ con_1, con_2, ... ]

    settings = {
        key_1 : value_1,
        key_2 : value_2,
        ...
    }
```

Whereas the `premises` is a (potentially empty) list of strings that is interpreted conjunctively, the `conclusions` is a (potentially empty) list of strings that is interpreted disjunctively.
Thus a countermodel is required to make _all_ of the premises true and _all_ of the conclusions false.
For instance, we might have no premises and just one conclusion so that `conclusions = [ '(A \\rightarrow \\neg \neg A)' ]` where operators are indicated by `\\` preceding the name of the operator.
Since a countermodel would have to make all of the premises true (this is trivially satisfied) and the only conclusion false (this should be impossible give a standard semantics for `\\neg` and `\\rightarrow`).
By contrast to the `premises` and `conclusions`, the `settings` is a dictionary which consists of `keys` which name the various settings and `values` which specify whether those settings.
For instance, we will have a setting with the key `N` which will be given a positive integer value that determines how many elements a model includes, e.g., `N : 3`.

Given an `example`, the model-checker works by translating the premises and conclusions into Z3 constraints which are added to a `solver`.
In particular, the premises are translated to Z3 constraints that require each premise to be true and each conclusion to be false.
Z3 is then tasked with finding a model which _satisfies_ all of the constraints added to the solver.
If Z3 succeeds, it returns the model that it finds, where this is then used to interpret our premises and conclusions, printing the result in a readable form.
If Z3 fails, it will either report an error (maybe it timed out), or it will report that the example is _unsatisfiable_, ruling out the existence of a model that conforms to the `settings`.
In this latter case, we can have Z3 print out the `unsat_core` which consists of the constraints that account for the unsatisfiability in question.

This provides a rough overview of the model-checker.
What remains is to describe how to use the model-checker to study a semantics.
Since this is best achieved through examples and exercises, the following section will provide installation details.
Having already set up VSCodium in the first problem set, this shouldn't take long.
Nevertheless, it is important to proceed carefully, raising any issues that you have along the way.

## Installation

Here are the packages that we will be installing:

- `python3`
- `model-checker`
- `z3-solver`

### Python

We will be using the model-checker in Python 3 and so it will be important to get this installed if you have not already done so.
If you are unsure if you have Python 3 already, run the following command in the terminal (open the terminal in VSCodium with `ctrl + backtick`):

```bash
python3 --version
```

If you get a version number, you should be good to go.
Otherwise, install [Python 3](https://www.python.org/downloads/) for your operating system, raising any [issues](https://github.com/benbrastmckie/ModalHistoryPrivate/issues) you have if you get stuck.
Once this process completes, run the command given above to confirm installation by checking the version number.

If you have not already, add the following extensions to VSCodium:

- Python
- Pylint

These will allow you to easily run Python scripts as well as detect syntax/type errors (called linting; these also exist for LaTeX).

#### VSCodium Config (Optional)

Although optional, I highly recommend making the terminal in VSCodium appear as a tab which you can achieve by:

1. Open VSCodium settings by pressing `Ctrl+Shift+P` and typing 'Preferences: Open User Settings (JSON)'
2. Add the following setting to your `settings.json` file by putting it after the first open brace `{` on a new line:

   ```json
     "terminal.integrated.defaultLocation": "editor",
   ```

3. From any Python file, click the drop down menu next to the play button on the right to "Open Python File in Dedicated Terminal"
4. You should then be able to arrange this tab as a vertical split with the Python file you want to run.
5. To create keybindings to run the current file with Python and the model-checker respectively, add the following to `keybindings.json`:
   - Press `Ctrl+Shift+P` and type 'Preferences: Open Keyboard Shortcuts (JSON)'
   - Add the following to your `keybindings.json` file inside the square brackets:
   ```json
   {
     "key": "ctrl+shift+enter",
     "command": "python.execInTerminal",
     "when": "editorTextFocus && editorLangId == 'python'"
   },
   {
     "key": "ctrl+shift+m",
     "command": "workbench.action.terminal.sendSequence",
     "args": {
       "text": "model-checker ${relativeFile}\u000D"
     },
     "when": "editorTextFocus && editorLangId == 'python'"
   },
   ```
   - You will need to restart VSCodium for these changes to take effect.

Now you can run any file in Python by pressing `Ctrl+Shift+Enter`, and similarly, run any file with the model-checker with `Ctrl+Shift+m` or whatever keybindings you choose to set (there will be an opportunity to test this below).

> Note that you can also add keybindings to build LaTeX files any lots more.

### Model-Checker

As with many pieces of software (called _packages_), there is no GUI (graphical user interface) installer for the model-checker.
Instead, we will install the model-checker using `pip` which is the Python's built in package manager.
This is nice because it is OS agnostic.

You can think of the packages that you install with `pip` as analogous to the extensions we added to VSCodium.
By installing new packages, you are extending what you can do in Python, or at least making it considerably easier.
For instance, installing the model-checker will make all of the functionality that the model-checker provides available to import in a Python file where something similar may be said for Z3.
There will be more on this soon, but first let's complete the installation.

Although you are welcome to use any terminal you like, I will assume that you are working in VSCodium, using its built in terminal for simplicity.
Open the terminal and run the following to update `pip` (if you just installed Python 3, this is unnecessary):

```bash
python3 -m pip install --upgrade pip
```

Now install the model-checker with:

```bash
pip install model-checker
```

You can confirm that the installation succeeded by running:

```bash
model-checker -v
```

The `-v` is called a _flag_, telling the model-checker to perform a certain action or to modify the action it would have performed.
Here are some other flags that can be run as above without other arguments:

- Include `-h` to print help information about the package and its usage.
- Include `-u` to upgrade to the latest version.

More information about the model-checker can be found [here](https://github.com/benbrastmckie/ModelChecker).

### Z3

The model-checker has the `z3-solver` as a dependency which will be installed automatically.
If you encounter any issues with Z3, you can try the following troubleshooting steps:

1. Check Z3 is installed:

```bash
pip show z3-solver
```

2. If missing, install manually:

```bash
pip install z3-solver
```

3. If you get version conflicts, try:

```bash
pip install --upgrade z3-solver
```

More information about installing packages in Python can be found [here](https://packaging.python.org/en/latest/tutorials/installing-packages/).

## Test Project

Having completed the installation, you are ready to start setting up a project with the model-checker.
It will be important to create your test project in right place.
To do so:

- Open the private repo in VSCodium as you have been doing for the other problem sets
- Navigate to `problem_sets/06_pset/` in the built in explorer
- Open the terminal (`ctrl + backtick`)
- This should put you in the `.../ModalHistoryPrivate/` directory
- List the contents of this directory with `ls`
- Change directory with: `cd problem_sets/06_pset/test_projects/`
- Alternatively, right-click on the `test_projects` directory in the explorer, selecting 'Open in Integrated Terminal'

You are now ready to create your test project:

- Run `model-checker` in the terminal (no flags or arguments)
- Enter `y` to create a new project
- Enter your first name in lowercase e.g., 'ben'
- Enter `y` to run the test script

The test should:

- Produce a single countermodel for an example including the counterfactual conditional operator `\\boxright`.
- Report that there are no countermodels found for a further example which is valid (we will call these theorems).

We will spend some time next week interpreting what these outputs mean.
All that matters for now is that the model-checker is printing countermodels when they exist and reporting theorems otherwise.
Once you get it working, commit and sync your changes.

If you have an older computer, the test might timeout.
This is nothing to worry about, simply requiring you to increase the time Z3 is permitted to look for countermodels.
This can be achieved by adjusting the settings for the example you are testing in `examples.py`.

## Examples

With the model-checker up and running, the last step is to familiarize yourself with the form that our examples will take.
To do so:

- Close the terminal, returning to the `.../06_pset/test_projects/` directory in the explorer
- You should now see your project directory along with its contents
- Open `.../06_pset/test_projects/YOUR_PROJECT/examples.py`

Python files are called `modules` where the primary module we will be working with is `examples.py`.
The documentation at the top of `examples.py` (called a `docstring`) provides an overview of the module contents.
The docstring is rather terse, so don't worry if it doesn't make sense just yet.

Skip down to the bottom of `examples.py` where you should see where the `example_range` is defined.
In particular, you should see the single countermodel and the single theorem that were uncommented.
Try another test by running `model-checker examples.py` or using the keybinding you set above.
As described above, it may be easiest to arrange your terminal as a vertical split.

In order to test other examples, go to any line that is commented out in `example_range` and hit `ctrl+/` to uncomment it.
You can also comment out examples that are uncommented in a similar fashion.
If you want to see which example you are turning on or off, you can hover the cursor over the example in question, hold down `ctrl` and click to jump to that definition (or press F12, or define a new keybinding, etc.).
You can jump back to your previous location `alt + left_arrow`.
This provides some ways to easily hop around, though there are many other methods.

After running a few test, read the `README.md` in your project directory (this is in progress).
In addition to providing some idea of how to make sense of the outputs you are getting, this documents the other modules in the directory.
You are welcome to look through the other modules if you like, though we will not be doing too much with them for now.

## SMT Solvers

In [week 10](https://github.com/benbrastmckie/ModalHistoryPrivate/blob/master/readings/10_week/10_week.md) we will read a paper by Martin Davis and Hilary Putnam who kicked of the SAT problem.
Here is a brief overview of SAT solvers and their relation to SMT solvers like Z3.

### Overview

SAT solvers are used to determine whether some number of constraints can be _satisfied_ by being made jointly true.
These solvers work with basic logical operations like AND, OR, and NOT.
SAT solvers were the first tools to tackle what computer scientists call "NP-complete" problems--- a class of problems for which no known polynomial-time algorithm exists, meaning their worst-case time complexity grows exponentially with the size of the input.
To solve these problems efficiently, SAT solvers employ sophisticated methods, particularly one called the DPLL algorithm (named after Davis, Putnam, Logemann, and Loveland).

Building upon these foundations, mathematicians and computer scientists developed even more powerful tools called SMT solvers.
While SAT solvers are limited to basic true/false logic, SMT solvers can work with much richer data types.
For instance, SMT solvers can handle arithmetic with whole numbers and real numbers, inequalities, arrays of values, sequences of binary digits called bit-vectors, as well as functions.
This makes them much more suitable for solving real-world logical and mathematical problems.

To understand how SMT solvers work, think sudoku.
You are given some number of constraints along with the rules of sudoku where the goal is to determine unknowns in a way that is consistent with what you have already without breaking the rules of sudoku.
Or for an even simpler example, suppose that you want to find values for variables `x` and `y` that satisfy these conditions: the sum of `x` and `y` is greater than `0`, `x` is less than `2`, and `y` is less than `2`.
A basic SAT solver couldn't handle this because it involves arithmetic relationships.
However, an SMT solver can tackle this since they include _theories_ where the relevant theory in this case is inequalities in arithmetic.

Given that SMT solvers can express more complex mathematical ideas directly, they can often be used to solve problems more efficiently than if we tried to reduce everything to basic true/false statements.
SMT solvers have proven particularly valuable in mathematical proof verification and theorem proving.
This is just the kind of application at hand.

One of the most prominent SMT solvers is called Z3, developed by Microsoft's research division.
It represents the current state of the art in automated mathematical reasoning, incorporating sophisticated mathematical techniques to solve complex problems.
But the field is changing fast where many labs are racing to produce even more effective SMT solvers.
The long days of computational toil in mathematics and logic may be soon coming to an end, leaving room for theorists to devote their whole attention to theory construction and applications rather than wrote computation.

