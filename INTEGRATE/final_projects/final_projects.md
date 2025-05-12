# Final Projects

> Final projects overview including grading, expectations, and options.

## Grading Breakdown

The final projects constitute 40% of the grade for those on the formal track and 80% of the grade for those on the historical track.
You are welcome to take an incomplete, turning in the final version a week prior to the department deadline.
I will expected you to submit a detailed outline for your project before the final seminar and to present what your project aims to accomplish in the final seminar.
The outline and presentation will constitute 5% of the grade for those on the formal track and %10 for those on the historical track.
This leaves 35% and 75% for the remainder, respectively.
Although I provide these details for transparency in my approach, I encourage you to just focus on doing your best work and not to think about grades.

## Expectations

> Overview for the formal and historical tracks.

### Historical Track

Write a final term paper (5k words) that either engages in a careful study of some part of the literature that we have engaged with or a nearby topic.
Please schedule a meeting with me to settle on an appropriate topic before preparing the paper outline.
Your final presentation should be brief (~10 minutes) where we will have a bit of time for questions after.
The aim here is to promote the exchange of ideas, helping you to clarify the ambitions of your project as well as benefit from other's questions.

You can find further resources in this [latex_example/README.md](latex_example/) document.

### Formal Track

The final projects for the formal track come in a two flavors:

- **Mathematical:** Present an important formal result discussing its significance
  - This shouldn't be a novel result (unless you have something you want to prove)
  - Rather the aim is to carefully present a classic result in a lucid way
  - Consideration should be paid to motivating the result, interpreting it, and typesetting
  - This can be a good choice to sharpen your comfort reading, understanding, and presenting formal proofs
- **Programmatic:** Use the `model-checker` to conduct a study of a chosen language fragment
  - Build a `model-checker` project, include the relevant operators, and examples under study
  - Use the `model-checker` to find countermodels, providing their interpretation, or establish validity
  - Consider tweaks to the semantics (frame constraints or semantics clauses)
  - Carefully document your findings in a Jupyter notebook, documenting the set up
  - This can be a good choice to gain some familiarity using this novel methodology to streamline research in semantics
- **Historical:** Provide a careful study of one of the texts (or related) that we have covered
  - This doesn't need to be a full essay (2.5k words or so is great)
  - This should be sufficiently formal (this is the formal track)
  - Philosophical reflections on a sufficiently formal subject-matter is great
  - This is an opportunity to hone in on one of the twists and turns in the history of logic
- **Other:** A project that you are already developing or working on that is sufficiently logical
  - If you are already working on a topic that has a clear logic component, feel free to get in touch to see if this could suit
  - I am happy for you to combine you project for this course with those you are working on elsewhere
  - My aim is for the final projects to be useful to you while still fulfilling the logic requirement

In order to make an informed choice, it will help to get some experience using the `model-checker`.
We will have a chance to do this in the next problem set.
Your final presentation should be brief (~10 minutes) where we will have a bit of time for questions after.
The aim here is to promote the exchange of ideas, helping you to clarify the ambitions of your project as well as benefit from other's questions.

If you have a project that does not fit into this scheme, feel free to get in touch to talk about it.
Given that this is a course in philosophical logic, it is important that the projects you choose concern logic.

#### Mathematical

There are many interesting formal results that we have not had time to delve into during this course.
Developing a final project which presents such a result is a chance to become more intimately acquainted with the mathematical logic associated with the systems that we have considered.

Results in mathematics are referred to as "non-trivial" when they establish something of interest and are not completely routine.
This typically suggests a degree of generality (as opposed to relevance only to some particular case, e.g., that claim X is valid).
It also suggests that the result itself does not belong to a class of procedurally similar results (though not always).
For instance, the semantic proofs that we have been doing are all pretty similar (though this doesn't make them easy!).
There are exceptions, such as completeness proofs, since these often have a similar form but are important enough to be non-trivial.

The aim is to find a non-trivial result to study and carefully present.
For instance, you might present the proof that a basic propositional modal logic such as K has the finite modal property.
This is interesting because of its connection to decidability of the satisfiability problem since there are only finitely many models to check.
There are many other results that you might present where you can find examples here:

**Blackburn, P., de Rijke, M., & Venema, Y. (2001). Modal Logic.**
   - Classic textbook with detailed coverage of finite model properties
   - https://doi.org/10.1017/CBO9781107050884

Since these results already have already been established, the achievement here is to understand a result at some depth, communicating your understanding.
This means providing careful motivation as well as cleanly typesetting and discussing the result in a way that makes it more accessible than what you will find in the text above.
Although I am happy to help you choose which result to focus on, part of this project would be to do a bit of digging through a logic textbook.

You can find further resources in this [latex_example/README.md](latex_example/) document.

### Programmatic

Since we are yet to use the `model-checker`, this section aims to give you a better sense of what a `model-checker` project might look like.
In particular, I will try to describe what the project could involve and what the upshots are of working on a project like this.
With that said, projects of this kind could take many different forms, and I would encourage you to explore the topics that appeal most to you.

Having contributed to the problem sets over the course of this term, I'm sure you can get the sense how much time it takes to write semantic proofs.
In order to get a good sense of a semantics, it is necessary to have a sense of the extension of its logical consequence relation.
Although this will typically include infinite may consequences, we can get a decent sense of the corresponding logic by checking finitely many instances.
Since doing so by hand is hard work and so limited as a result, we will use the `model-checker` to streamline this process.

The aim of this project is to equip you with computational tools for exploring semantic systems and rapidly prototyping novel semantic clauses.
This leaves your options open with regard the topic with which you point this methodology.
There will be two problem sets which will help to introduce you to this programmatic methodology before starting on the final project.
In general, applications of the `model-checker` will consist in:

- Choosing a language fragment to study
- Populating a range of examples to evaluate
- Interpreting the results
- Reporting findings in a Jupyter notebook.

You can find further resources in this [jupyter_example/README.md](jupyter_example/README.md) document.

### Historical

The historical track offers an opportunity to engage with the philosophical and logical texts we've studied.
Rather than a full term paper, the aim here is to provide a focused study of approximately 2,500 words that demonstrates both historical sensitivity and formal understanding.

The aim is to conduct a careful textual analysis of some formal topic in the history of logic.
This could be a topic we covered, or something adjacent.
For instance, you could examine the arguments and motivations behind important logical developments such as investigating why Ruth Barcan Marcus defended the Barcan formula.

Alternatively, you could examine the developed of a logical theory from one setting to another.
For instance, you might explore how McTaggart's metaphysical "muddle" evolved into Prior's semantics for tense logic.
As this is a short paper, it will be important to focus on something specific to discuss in detail rather than providing a broad arc.

This could be a choice for those interested in the conceptual foundations of logical systems and how they emerged from philosophical discourse.

You can find further resources in this [latex_example/README.md](latex_example/) document.

### Other Project

If you have another project in mind, feel free to get in touch.
I am happy for you to combine this project with those in your other courses or projects if that makes sense.

