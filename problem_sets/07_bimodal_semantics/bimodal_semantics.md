# [Problem Set 07: Model-Checker](https://github.com/benbrastmckie/ModalHistory?tab=readme-ov-file#problem-sets)

In a surprise upset in the ongoing battle between me and the `model-checker`, I have managed to get an implementation of the bimodal semantics working.
This is _good news_ because it means you can begin to familiarize yourself with this new methodology while working in familiar territory.
This is _bad news_ because it means there are still likely to be problems with the implementation, yielding undesired results.
With this in mind, the plan for this problem set is three-fold:

1. Explore the documentation that I have created so far as well as the small set of examples that I used to test the bimodal semantics.
2. Run the `model-checker` on new examples, looking both for cases where the `model-checker` gets things right as well as those it may get wrong.
3. Extend the expressive resources of the bimodal language by defining a new operator in terms of the operators that I provide.

Although these exercises should not take as long as writing proofs, do start early in case you hit any bugs or want to ask questions.
Since I am getting this problem set to you later than I had intended, it's OK if you are a bit late too.
Nevertheless, having some familiarity with the material before the next seminar will help make our discussion more productive.

## Bimodal Project

You will begin much as before by running the following in the terminal.
To pull down the most recent version which includes the bimodal semantics, run:

```bash
model-checker -u
```

Navigate to `problem_sets/07_pset` as you did in the previous problem set.
You will now need to create a new project, but this time we will specify the bimodal semantics with:

```
model-checker -l bimodal
```

The `-l` flag is short for `--load` where the name of the theory is specified after.
Running `model-checker` without arguments is the same as running `model-checker -l default` where last time we loaded the default semantics.
I intend to change this name to `state-semantics` at some point, but haven't gotten around to it.

As before, use your first name to create a project, hitting `y` to test the project once it builds.
Check to see if there is a `README.md` and give it a read (you can skip the **Implementation Details** section).
You will find a lot of information in the `README.md` which serves as a reference.
As this instance of the bimodal semantics is all yours, you are welcome to make changes to the `README.md` to include notes.

Then open the `examples.py` module in the project that you created and scroll down to the end.
Go to any line that is commented out in `example_range` and hit `ctrl+/` to uncomment it (in VSCodium).

To run a test, use the same keybinding you created in the last problem set (or run `model-checker examples.py` from the `problem_sets/07_pset/` directory).

## Running Tests

The assignment from here is simple and intended to give you some practice using this tool.
To begin with, run through the examples that exist so far. 
I recommend running them one at a time by (un)commenting lines.
Do your best to make sense of the outputs that you are getting.

### Problem 1: Interpretation

Choose an example which has a countermodel and find where that example is defined (recall the `F12` and `alt+left_arrow` for jumping to definitions and back from last week).
In a docstring, provide a brief explanation of the output for that example, along with a concrete example in English which is an instance.
That is, use a triple backtick to open and close a docstring block just under the example as given below:

```python
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
"""
The model-checker provides a countermodel showing that (A ∨ B) does not entail (A ∧ B).
This makes sense since one of the disjuncts A and B can be true without both A and B being true.

Concrete example:
"Either it's raining or it's snowing" does not entail "It's both raining and snowing".
The countermodel shows a world where it's raining but not snowing, satisfying the disjunction
but falsifying the conjunction.
"""
```

### Problem 2: Extension

Come up with an example of your own to add to `examples.py` and run a test with the `model-checker`.
I would encourage you to cut and paste, or you could even set up a snippet in VSCodium to automate example creation.
For each example, provide a concrete instance in English, and say whether the `model-checker` is getting things right or not.
Include a docstring as above.

### Problem 3: Break Things

Now it's time to test the limits, looking for new examples of where things break down.
This shouldn't be hard since this semantics has not yet been put through its paces.
There are two kinds of failures:

1. Boring failures where Z3 times out
  - There is not much to say about these besides saying which examples timeout
  - Finding many examples that timeout is useful for optimizing the semantics (I have only just started this)

2. Interesting failures where Z3 either:
  - Finds a countermodel that shouldn't exist 
  - Or asserts that there are no countermodels when there should be

The aim here is to find _interesting_ failures, explaining in a docstring why the `model-checker` is wrong (intuitively/semantically).
See if you can find at least one new examples of this kind.
Boring failures are also valuable to know about, though there is not much to say about them.

### Problem 4: Defined Operators

The final question will give you some exposure to the underlying mechanics which makes the bimodal semantics tick.
Begin by taking a look at the `operators.py` module beginning with the docstring at the top.
Each operator is defined to be a **class** within Python consisting of four primary **methods**.
The key semantic methods are `true_at` and `false_at` specifying how the `model-checker` constructs Z3 constraints for sentences including that operator.
Further discussion of the operators is provided in the `README.md` included in your project.

Now skip down to the end of `operators.py` to where the operator collection is defined.
This definition helps to expose the operator classes given in the module, providing expressive resources that can be used in `examples.py`.
The operator collection consists of both primitive operators as well as defined operators.
Although we may expand the language to include further primitive operators, it is also useful to expand the language by defining additional operators given those (primitive and defined) that have already been provided.

Take a look at the defined operators included just above the operator collection.
The key definition is `defined_definition` which provides a translation using prefix notation.
Sentences in this context are lists (indicated by `[ ... ]`) where the operator comes first and is followed by its arguments.
As much as humans struggle with prefix notation, prefix notation is easy for computers to use recursively.

The final problem is to define an additional operator from the operators that have already been given.
To do so, I suggest making a copy of one of the operators that have already been defined (e.g., `ConditionalOperator`), changing the name to something appropriate.
Do your best to conform to the naming conventions used here since this will help to avoid confusion and errors.
Then proceed along the following guidelines:

- Copy a defined operator, changing its name following the `class` keyword, e.g., `DefYourOperator`
- Write a docstring to say in English what your operator means and provide an example
- Also change the string used to call the operator, e.g., `\\your_operator`
- Make sure the arity is correct
- Revise `defined_definition` making use of any other operators given above
- Use the same print method as another operator where these include:
  - `print_over_times`
  - `print_over_worlds`
  - `general_print`
- Expose your operator by including it in the collection 
- Create an example in `examples.py` to test that your operator is working.

It is OK if things don't quite work or you get strange results.
The goal here is to learn how to fish, not to catch one.

## Concluding Remarks

Letting the `model-checker` do the computational work for us leaves room to focus on something that the `model-checker` can't do: survey the language.
You might think that we should be able to somehow automate this process, looking mechanically through the sentences of our language searching for logical consequences.
This would be very nice, but there is a problem: the number of sentences is not just infinite, it grows in size very quickly with syntactic complexity.
This makes surveying the space hard, leaving it to human intuition to know where to look to find logical consequences of interest.
Of course, having the `model-checker` there to help out is handy for evaluating logical consequences and finding countermodels, but it can't tell you what to try first or what to care about.

Despite these limitations, the `model-checker` is an invaluable tool when it comes to exploring and prototyping semantic theories.
Instead of having to check all of our semantic proofs each time we make a tweak to a theory, we can set up unit tests for the `model-checker` to rifle through after each tweak to the semantics we might want to make.
There will be more opportunity to get a sense of how this goes soon.

Although clicking buttons isn't as hard as proving things, there is a lot to take in here to get a sense of this programmatic methodology.
We will be looking a bit into the origins of where this technology first got going in the next seminar meeting where we will take a look at the SAT problem.
As always, if you get stuck or come across something you'd like to share or discuss, please don't hesitate to cut and paste outputs into the [issues](https://github.com/benbrastmckie/ModelChecker/issues).
