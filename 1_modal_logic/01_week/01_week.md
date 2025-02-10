# [Week 01](https://github.com/benbrastmckie/ModalHistory/tree/master?tab=readme-ov-file#week-01-early-modal-systems-feb-10)

- Lewis, C. I. “A New Algebra of Implications and Some Consequences.” The Journal of Philosophy, Psychology and Scientific Methods 10, no. 16 (July 1913): 428–38. https://doi.org/10.2307/2012900.
- ———. “Alternative Systems of Logic.” The Monist 42, no. 4 (October 1932): 481–507.
- ———. “Strict Implication–An Emendation.” The Journal of Philosophy, Psychology and Scientific Methods 17, no. 11 (May 1920): 300–302. https://doi.org/10.2307/2940598.
- **———. “The Calculus of Strict Implication.” Mind, New Series, 23, no. 90 (April 1914): 240–47.**
- ———. “The Matrix Algebra for Implications.” The Journal of Philosophy, Psychology and Scientific Methods 11, no. 22 (October 1914): 589–600. https://doi.org/10.2307/2012652.
- ———. “The Structure of Logic and Its Relation to Other Systems.” The Journal of Philosophy 18, no. 19 (September 1921): 505–16. https://doi.org/10.2307/2939309.
- **[Appendix II] Lewis, C. I., and C. H. Langford. Symbolic Logic. New York: Century Company, 1932.**
- McKinsey, J. C. C. “A Reduction in Number of the Postulates for C. I. Lewis’ System of Strict Implication.” Bulletin of the American Mathematical Society 40, no. 6 (1934): 425–28. https://doi.org/10.1090/S0002-9904-1934-05881-6.
- **Barcan, Ruth C. "A Functional Calculus of First Order Based on Strict Implication." The Journal of Symbolic Logic 11, no. 4 (1946): 115–18. https://doi.org/10.2307/2269159.**
- ———. "The Deduction Theorem in a Functional Calculus of First Order Based on Strict Implication." Journal of Symbolic Logic 11, no. 4 (1946): 115–18.

## Admin

- Who is on which track
- Does everyone have access to the private repo/emails who wants it?
- Presentation sign-up 
- Will leave time to check in about the collaborating with Git
- Backgrounds in logic and Hilbert's system

## Topics

### "Implication and the Algebra of Logic" (1912)

> Last time we saw...

- Inchoate conception and motivations driving Lewis
  - A logic of the possible and necessary, not just the actual
  - Necessary as something like, or including, the _a priori_
  - Aim to extend the vocabulary that PM introduces is a good one
- Motivation
  - What should we require of a new program in logic?
  - Perfectly clear theoretical target is too much to ask
  - Methodology for developing the logic
  - Consistency is vital
  - Motivation from the inadequacies of the existing systems
    - Avoid absurd propositions (these indicate limited meaning of 'implies')
    - Provide a better reading of 'implies'
  - Intended applications (theoretical role)
    - Some appeal what can be known _a priori_
    - Some appeal to the ability to test/reason about scientific hypotheses
  - Stipulated systems ultimately draw on abductive support
- Anachronism
  - Compare the extensional and intensional algebras
  - Some grounds for resonance with what Lewis writes
  - Wants to reason about the possible not just the actual

### Russell, Frege, and Carroll

> Why does Russell insist that \*1.1 cannot be expressed symbolically?

- **[sec. 2] Heijenoort, Jean van, ed. “Begriffsschrift, a Formula Language, Modeled upon That of Arithmetic, for Pure Thought: GOTTLOB FREGE(1879).” In Frege and Gödel: Two Fundamental Texts in Mathematical Logic, 1–82. Harvard University Press, 2013. https://doi.org/10.4159/harvard.9780674864603.c2.**
- **Carroll, Lewis. “WHAT THE TORTOISE SAID TO ACHILLES.” Mind IV, no. 14 (April 1895): 278–80. https://doi.org/10.1093/mind/IV.14.278.**
- **[Sec. 38] Russell, Bertrand. Principles of Mathematics. New York,: Routledge, 1903.**
- **[pp. 99] Russell, Bertrand, and Alfred North Whitehead. _Principia Mathematica_. 2nd ed. Vol. 1. Cambridge: Cambridge University Press, 1910.**

- Carroll gives a puzzle about deduction
- Russell concludes that we must have a primitive rule of inference (a notion of _therefore_)
  - [p. 51] Must distinguish 'implies' from 'therefore'
  - Although there are systems (like natural deduction) which only have rules, there is no system which only has axioms
- Russell maintains Frege's use of 'assertion'
  - True propositions may be said to be _asserted_
  - $p \rightarrow q$ does not _assert_ either $p$ or $q$, though these propositions are considered
  - The relation _therefore_ only holds between asserted propositions
  - Cites Frege's discussion of assertion
  - [p. 52] "Wherever therefore occurs, the hypothesis may be dropped, and the conclusion asserted by itself. This seems to be the first step in answering Lewis Carroll’s puzzle."
- Frege introduces the turnstile $\vdash$ to express a _judgement_
  - Contrasts this with a, "mere combination of ideas"

### "The Calculus of Strict Implication" (1914)

- Motivation
  - [p. 241] Material implication, "cannot apply to a world in which there is a difference between real and possible, between false and absurd"
  - Strict implication, "admits of the distinction of true and necessary, of false and meaningless."
  - [FN 1] Pragmatic, writing, "a calculus in logic may be, as pure mathematics, true; as applied mathematics, either absolutely or pragmatically false."
  - [p. 242] Contrasts intensional disjunction as, "it is _impossible_ that p and q should both be false" as opposed to extensional disjunction as, "it happens to be the fact that at least one of the propositions, p and q, is true".
- Systems
  - [p. 243] M1 - M7 vs S1 - S11
    - Recall the contrast between replacing material implication and extending it
    - Here we find an extension with clear priority given to strict implication
    - S7 $\Box(\Box(p \vee q) \rightarrow (p \vee q))$ is a necessitated version of the T axiom
    - S9 $\Box(\Box(p \vee (q \vee r)) \rightarrow \Box(q \vee (p \vee r)))$
      - Derives instances of the paradoxes of strict implication (somehow)
      - Follows in a Hilbert system from N and A1
  - Notes the absence of the paradoxes from the system of strict implication
  - [p. 244] Aim to distinguish the useful theorems writing, "It is easy to demonstrate that an infinity of such absurd propositions follow from the assumptions of material implication. The significant and useful theorems of that calculus thus appear to be, like Gratiano's reasons, two grains of wheat. That they are not hid in two bushels of chaff is due to the restraining intelligence which manipulates the system."
  - Falsely claims that, "These theorems are absurd only in the sense that they are utterly in applicable to our modes of inference and proof."
- Interpretation
  - Characterizes, "the nature of any world to which this system of material implication would apply," as:
    - "In such a world, all-possible must be necessary, the contingent cannot exist, the false must be absurd and impossible, and the contrary to fact supposition must be quite meaningless."
    - "[T]he true must necessarily true, true _a priori_, if 'a proposition is implied by any proposition'."
    - "[T]he contingent cannot exist, since all facts will be necessarily as they are, and the truth about them _a prori_."
    - [p.245] "[T]he false will be impossible and absurd"
  - By contrast, "The system of strict implication distinguishes the false from the absurd, the merely contrary to fact from the impossible, and the merely true--- the contingent--- from the necessarily true whose very denial implies it."
    - Considers paradoxes of strict implication, "That the merely contrary to fact implies anything is repugnant to common sense.  But does the impossible--- the absurd supposition--- imply anything and everything? And is the necessarily true, whose denial is absurd, implied by any proposition whatever?"
  - Are there contingent propositions?
    - [p.246] "If we ask, now, whether the actual world is such a one as material implication may apply to, the answer is not self-evident. Here, again, we are reminded of rival geometries. We do not discover the necessity of all facts, nor the absurdity of every contrary to fact hypothesis. Nor are we able to verify that ubiquity of the implication relation demanded by material implication. One may thus maintain that the real is not the all-possible, that reality is, in some part, contingent and not necessary, that the multiverse of things 'hang together by their edges,' and, consequently, that the system of material implication is false as an applied logic.  But an obvious reply has it that this is a generalisation from our ignorance,--- that our belief in the contingent and the false but not absurd, is due to the smallness of our ken. A decision on metaphysical grounds would thus be doubtful."
    - "Pragmatically, however, implication is an obviously false logic.  If 'p implies q' means only 'it is false that p is true and q false,' then the implication relation is far too ubiquitous to be of any use.  If we ask for the consequences of any proposition, we are immediately confronted with all the truths we can think of. If we are so foolish as to make a condition contrary to fact, we must at once accept its own contradictory as the logical result. Not only is such reasoning applicable only to a monistic universe,  but it is suited only to infinite wisdom."
    - "[The] few theorems present propositions clearly reveals its meaning of 'implies'--- and the infinity like them which are omitted--- are not capable of _any_ proper use as rules for reasoning."
- Outlook
  - [p. 247] "But even if, in the end, one prefer the false simplicity of material implication, this much at least, remains clear; the present calculus of propositions is only one among a  number of such systems, each of which may be self-consistent and a possible choice as an applied logic."
   
### [Appendix II] "Symbolic Logic" (1932)

- Presents A-axioms and B-axioms
  - Primitives symbols include $\neg, \wedge, \vee, \Diamond, \exists$
    - '$\Diamond$' reads 'Is self-consistent'
    - $\exists$ is higher-order
  - Primitive rules
    - [p. 125] Uniform substitution
    - [p. 126] Conjunction introduction
    - Modus ponens (not to be confused with 11.7/B.7)
  - Observations
    - A7 $\Box(\neg \Diamond p \rightarrow \neg p)$ is a necessitated version of T
    - B9 $\exists p, q: \neg\Box(p \rightarrow q) \wedge \neg\Box(p \rightarrow \neg q)$ posits contingency
  - Deducible
    - B1-8 are deducible from A1-8
    - A1-7 are deducible from B1-8
    - Lewis asks if A8 deducible from B1-8?
    - Parry shows otherwise by the matrix method
      - [p. 229] "The nature of the matrix method and the characteristics of  'implication'-relations which have just been considered make it  obvious that there is an immense variety of truth-value systems,  every one of them having its determined structure and its  definite laws, and any one of which might conceivably be taken  as a calculus of propositions. We do not need to discover such  systems: they can be devised in various simple ways."
      - [p. 233] "A truth-value system is essentially an abstract mathematical structure. It becomes a system of logical truth only by  interpretation. That the structure of a logical calculus can be  thus considered in abstraction from its logical meaning is a fact  of the greatest importance, and one which has commonly been  overlooked."
  - Matrix Method (proto models) to demonstrate:
    - Consistency
    - That strict systems are not reducible to system of material implication
      - [p. 495] "$\neg(p \wedge \neg q) \strictif (p \strictif q)$ has the value 3 or 4 when p = 1 and q = 2."
    - Independence
  - Method: produce a minimal, consistent, and strong logic
- C-axioms
  - C10 $\Box(\Box p \rightarrow \Box\Box p)$
    - Converse is deducible from $\Box(p \rightarrow \Diamond p)$
    - See 18.4 in Ch.VI
  - C13 $\Diamond\Diamond p$
    - [p. 499] A1-8 leave open two possibilities:
      - (a) that there exists propositions which are necessarily-necessary though this is no different from being necessary
      - (b) that there exist propositions which are necessary but no propositions which are necessarily-necessary
    - C10 expresses (a) and C13 expresses (b) and hence contrary assumptions
    - $\Box(\Box\Box p \rightarrow \Box(\Box p \leftrightarrow p))$ is said to be deducible from 19.84 in Ch.VI
  - C11 $\Box(\Diamond p \rightarrow \neg\Diamond\neg\Diamond p)$
    - The consequent is read as "Its not possible that its not possible that p" 
  - C12 $\Box(p \rightarrow \neg\Diamond\neg\Diamond p)$
    - Called the "Brouwersche Axiom" in connection with $A \rightarrow \neg\neg A$ from intuitionistic logic
- Axiom Systems
  - "From the preceding discussion it becomes evident that there is a group of systems of the general type of Strict Implication and each distinguishable from Material Implication."
  - S1 B1-7 contains theorems sec.1-4 from Ch.VI, and sec.5 given T
  - S2 B1-8 contains theorems sec.1-5 from Ch.VI
  - S3 A1-8 contains theorems sec.1-5 from Ch.VI
  - S4 B1-7 and C10 contains S3, A8, and B8 but is incompatible with C13
  - S5 (B1-7 and C11) or (B1-7, C10, C12) contains S4 but is incompatible with C13
  - [p. 501] "In my opinion, the principal logical significance of the system S5 consists in the fact that it divides all propositions into two mutually exclusive classes: the intensional or modal, and the extensional or contingent."
  - "According to the principles of this system, all intensional or modal propositions are either necessarily true or necessarily false. For extensional or contingent propositions, however, possibility, truth, and necessity remain distinct."
  - "Prevailing good use in logical inference--- the practice in mathematical deductions, for example--- is not sufficiently precise and self-conscious to determine clearly which of these five system expresses the acceptable principles of deduction."
  - [p. 502] "The issues concern principally the nature of the relation of 'implies' which is to be relied upon for inference, and certain subtle questions about the meaning of logical 'necessity', 'possibility' or 'self-consistency,' etc.--- for example, whether C10 is true or false."

### [Appendix III] "Symbolic Logic" (1932)

- Axioms strive to be independent and minimal
  - [p. 503] Notes that Parry has proved that S2 and S3 are distinct, "completing proof that all five of the systems S1-S5 are distinct from one another."
  - Notes that McKinsey has derived 11.5/B.5
- Paradoxes of strict implication
  - [p. 511] "confined to the implications which are assertable when one or both of the propositions related is contradictory (equivalent, for some $r$, to $r \wedge \neg r$) or when one or both is analytic (equivalent, for some $r$, to $r \vee \neg r$)."
  - "They do not extend to implications assertable as holding between premises and conclusions both of which are contingent propositions, neither analytic and logically necessary nor contradictory and logically impossible."
  - "Thus they do not affect what implies what amongst empirically substantiated and factually informational premises and their empirically significant consequences."
- Meaning of strict implication
  - "Strict Implication, defining $p \strictif q$ as a statement which holds  when and only when the conjoint statement $p \wedge \neg q$, which asserts  the premise and denies the conclusion, is self-inconsistent, is put forward with the intent to satisfy the requirement that $p \vee q$ hold when and only when $q$ is a consequence validly deducible from the premise $p$."
  - [p. 512] Admits that the paradoxes of strict implication are inescapable consequences of indispensable rules of inference.
- [p. 508] Cites Barcan Marcus' 1946 extension of S2 to the first-order


### MacColl's Algebra

> To what extent did MacColl anticipate the development of modal logic?

- **McColl, Hugh. “Symbolical Reasoning.” Mind 5, no. 17 (1880): 45–60.**
- MacColl, Hugh. “Symbolic Logic (A Reply).” Mind 16, no. 63 (1907): 470–73.
- Rahman, Shahid. “Hugh MacColl and George Boole on Hypotheticals.” In A Boole Anthology: Recent and Classical Studies in the Logic of George Boole, edited by James Gasser, 287–310. Dordrecht: Springer Netherlands, 2000. https://doi.org/10.1007/978-94-015-9385-4_16.
- Astroh, Michael, Ivor Grattan-Guinness, and Stephen Read. “‪A Survey of the Life of Hugh MacColl (1837-1909)‪.” Philosophia Scientiæ 151, no. 1 (2011): 7–29. https://doi.org/10.4000/philosophiascientiae.357.

### Quantified Modal Logic

Here are two ideas for topics to present on (other ideas are welcome).

## Further Particulars

### Presentations

### Hilbert System

- **N** is a metarule, not a rule of inference
  - Otherwise the deduction theorem would lead to modal collapse
    - $\varphi \vdash \Box\varphi$ would give $\vdash \varphi \rightarrow \Box\varphi$ by **DT**
    - With **T** $\vdash \Box\varphi \rightarrow \varphi$, we get $\vdash \Box\varphi \leftrightarrow \varphi$
    - Thus the $\Box$ would be vacuous and so could be dropped altogether
  - Will return to defend the deduction theorem when we develop semantic systems
  - For now, observe that the deduction theorem is a primitive rule in natural deduction systems
  - Instead of restricting the deduction theorem, **N** is a metarule
- Thus we must give a recursive definition of proof
  - We could have started off this way even in propositional logic

### Git, VSCodium, etc.

- How did it go using Git?
- Beware merge conflicts
- Reserve problems to work on, making a copy if someone has started
- Checked a proof
