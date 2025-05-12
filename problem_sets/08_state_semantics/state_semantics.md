# [Problem Set 08: State Semantics](https://github.com/benbrastmckie/ModalHistoryPrivate?tab=readme-ov-file#problem-sets)

> Use the `model-checker` to explore the state semantics for counterfactual conditionals and constitutive explanatory operators.

This problem set will be very similar to the previous problem set, only this time we will be using the `model-checker` to explore the state semantics for counterfactual conditionals.
Instead of encountering the state semantics first through writing semantic proofs, we will begin by using the `model-checker` to explore the theory's extension. 
This has its advantages in that it allows you to survey the system much more quickly, however, there is also the major disadvantage in that it is harder to make sense of the models that the `model-checker` finds.
Accordingly, the aim of this problem set is to get some practice interpreting the hyperintensional models that the `model-checker` finds.
To help with this, we will make use of some of the settings which that theory provides.

As before, we will start by creating a new project, where I will set out the steps as before.
Hopefully some of the unfamiliarity with this methodology is beginning to wear off, paying dividends for your upfront investment.

## State Semantics Project

You will begin much as before by running the following in the terminal.
I have added a new iteration tool which you can get by updating:

```bash
model-checker -u
```

Open the terminal and navigate to `problem_sets/08_pset` as you did in the previous problem set.
You will now need to create a new project, but this time you can run the following without arguments:

```
model-checker
```

Running `model-checker` without arguments is the same as running `model-checker -l default`.
Although this is the same theory we used in `06_pset`, there have been some minor changes.
As before, use your first name to create a project, hitting `y` to test the project once it builds.

There have been some changes to the `README.md` which serves as a reference.
Then open the `examples.py` module in the project that you created and scroll down to the end.
Go to any line that is commented out in `example_range` and hit `ctrl+/` to uncomment it (in VSCodium).

It is important that when calling the `model-checker`, you provide the appropriate path to the file you want it to run.
To run a test, use the same keybinding you created in `06_pset` or run `model-checker examples.py` from the `problem_sets/08_pset/` directory.
Using the keybinding will automatically find the path to the file you have open, so that makes things easy.
Alternatively, you can change directory with `cd path/to/directory` and you can see your current working directory with `pwd`.

## Problems

Unlike the implementation of the bimodal semantics which I only got to start working recently, the default semantics has been much more thoroughly tested and optimized.
Accordingly, you will see lots of examples in the `examples.py` file in your project.
The aim here is to explore some of the examples already provided as well as constructing new examples.
We will then use the settings to tweak the outputs in different ways before defining a two additional operators in terms of the primitives already provided.

### Problem 1: Countermodels

Look through the existing counterfactual countermodels (labeled `CF_CM_#`) finding an example to analyze.
Scroll down to the end, turning on just that example and look at the models it provides. 
If you want to see more than one model, you can increase the `iterate` setting.

Once you settle on an output, cut and paste the countermodel it finds into a `consol` docstring (see example below).
See if you can find a concrete instance of that countermodel, or say why this cannot easily be done if you disagree that there should be countermodels.
It's OK if this is tentative and exploratory, and you are free to rely on natural language intuitions, or appeal to logical considerations, whatever seems most relevant.

Here is an example where I will begin with a `python` docstring followed by a `consol` docstring:

```python
# CF_CM_16: SIMPLIFICATION OF DISJUNCTIVE CONSEQUENT
CF_CM_16_premises = ['\\neg A','(A \\boxright (B \\vee C))']
CF_CM_16_conclusions = ['(A \\boxright B)','(A \\boxright C)']
CF_CM_16_settings = {
    'N' : 4,
    'contingent' : True,
    'non_null' : True,
    'non_empty' : True,
    'disjoint' : False,
    'max_time' : 2,
    'iterate' : 1,
    'expectation' : True,
}
CF_CM_16_example = [
    CF_CM_16_premises,
    CF_CM_16_conclusions,
    CF_CM_16_settings,
]
"""
The model-checker provides a countermodel showing that (A \\boxright (B \\vee C)) does not entail either (A \\boxright B) or (A \\boxright C).
This makes sense since even if all of the outcome world states that result from making A true are worlds in which either B or C is true, we can't conclude that B (similarly C) is true in all of these outcome world states.
The \\neg A premise has been added simply to ensure that we find a countermodel in which A is false.

Concrete example:
"If it were raining, either the game would have been canceled or moved indoors" does not entail "If it were raining, the game would have been canceled" nor does it entail "If it were raining, the game would have been moved indoors".
The countermodel shows that among the outcome world states in which it is raining, the game is canceled in some and indoors in others so that the disjunctive consequent is guarenteed to be true without either disjunct being guarenteed to be true.
"""
```

Here is one such countermodel.

```consol
State Space:
  #b000 = □
  #b001 = a (world)
  #b010 = b (world)
  #b100 = c (world)

The evaluation world is: b

INTERPRETED PREMISES:

1.  |\neg A| = < {b}, {a, c} >  (True in b)
      |A| = < {a, c}, {b} >  (False in b)

2.  |(A \boxright (B \vee C))| = < {□}, ∅ >  (True in b)
      |A| = < {a, c}, {b} >  (False in b)
      |A|-alternatives to b = {a, c}
        |(B \vee C)| = < {a, c}, {b} >  (True in c)
          |B| = < {a}, {b, c} >  (False in c)
          |C| = < {c}, {a, b} >  (True in c)
        |(B \vee C)| = < {a, c}, {b} >  (True in c)
          |B| = < {a}, {b, c} >  (False in c)
          |C| = < {c}, {a, b} >  (True in c)
        |(B \vee C)| = < {a, c}, {b} >  (True in a)
          |B| = < {a}, {b, c} >  (True in a)
          |C| = < {c}, {a, b} >  (False in a)
        |(B \vee C)| = < {a, c}, {b} >  (True in a)
          |B| = < {a}, {b, c} >  (True in a)
          |C| = < {c}, {a, b} >  (False in a)

INTERPRETED CONCLUSIONS:

3.  |(A \boxright B)| = < ∅, {□} >  (False in b)
      |A| = < {a, c}, {b} >  (False in b)
      |A|-alternatives to b = {a, c}
        |B| = < {a}, {b, c} >  (False in c)
        |B| = < {a}, {b, c} >  (True in a)

4.  |(A \boxright C)| = < ∅, {□} >  (False in b)
      |A| = < {a, c}, {b} >  (False in b)
      |A|-alternatives to b = {a, c}
        |C| = < {c}, {a, b} >  (True in c)
        |C| = < {c}, {a, b} >  (False in a)
```

#### State Space:

    #b000 = □ (null state)
    #b001 = a (world where it's raining and game is canceled)
    #b010 = b (world where it's not raining and game proceeds normally)
    #b100 = c (world where it's raining and game is moved indoors)

The evaluation world is: `b` (actual world where it's not raining)

#### Key interpretations:

    A = "it is raining"
    B = "the game is canceled" 
    C = "the game is moved indoors"

#### In the evaluation world `b`:

- It's not raining (¬A is true)
- If it were raining (A), then either the game would be canceled (B) or moved indoors (C)
- This is verified by checking A-alternatives to b (worlds a and c):
  - In world a: it's raining and game is canceled (B true, C false)
  - In world c: it's raining and game is moved indoors (B false, C true)
- Neither "if it were raining, game would be canceled" nor "if it were raining, game would be moved indoors" is true
  - Because each is false in one of the A-alternatives

### Problem 2: New Example

Come up with an example of your own to add to `examples.py` and run a test with the `model-checker`.
I would encourage you to cut and paste, or you could even set up a snippet in VSCodium to automate example creation.

The next step is to tune the settings to help make the example easy to interpret.
For instance, you can make it contingent, or find the right number of atomic elements to include.
The `disjoint` setting will require you to include many more elements to find an example, but has the advantage of making it much easier to interpret.

After tuning the settings, you can try iterating through models by increasing the value of `iterate`.
This can help to find a countermodel that is natural and easy to interpret.

Once you settle on a countermodel, provide a concrete instance in English, and say whether the `model-checker` is getting things right or not.
Provide your analysis in a docstring as above.

### Problem 3: Logical Equivalence

We have not yet had occasion to use the `model-checker` to check logical equivalences.
Although the `model-checker` only searches through finitely many models where has a finite state space, the `model-checker` can still rule out all small countermodels in this way where 'small' means less than `2^N` states.
The bigger the number `N` for which there are no countermodels, the more certain you may be that there are no finite countermodels.

Here is an interesting case to check:

    (\\CFBox A \\leftrightarrow \\Box A)

This says that `\\CFBox A` and `\\Box A` are materially equivalent (have the same truth-value).
By making the sentence above a conclusion of an example with no premises, we may check if there are any models in which the sentence above is false.
If there are no countermodels below `2^N` for some value of `N`, it follows that `\\CFBox A` and `\\Box A` have the same truth-value in all such models.
Put otherwise, `\\CFBox A` and `\\Box A` are logically equivalent over the space of finite models with `2^N` states.

What does all of this mean?
Here we must look at the definition of `\\CFBox` since `\\Box` is primitive, quantifying over all world states.
For instance, if the definition of `\\CFBox` amounted to no more than relabeling `\\Box`, their logical equivalence should not surprise.

This problem asks you to create an example with no premises where `(\\CFBox A \\leftrightarrow \\Box A)` is the conclusion to check that it is valid.
The next step is to see how big you can make `N` before the Z3 times out, stating this briefly in a docstring.
Now do the same thing for the following case:

    (\\CFDiamond A \\leftrightarrow \\neg \\CFBox \\neg A)

In a docstring, discuss the significance of this result in contrast to showing that `(\\Diamond A \\leftrightarrow \\neg \\Box \\neg A)` is valid.

## Concluding Remarks

There are many other operators provided by the default semantics.
Now that you've had some experience using the `model-checker`, a good final project could be conducting a study of the interactions between some of them.
This could include finding the elements we have covered so far, providing a systematic analysis together with some philosophical discussion.

Although we will not be covering this in this final problem set, 
You are also welcome to try to define your own primitive operator
