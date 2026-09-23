---
title: "Generation Is Not Inquiry"
date: 2026-09-23
tags: ["generative-ai", "reasoning", "architecture"]
draft: false
description: "AI inference, reasoning, and inquiry are routinely collapsed into one idea. They are different mechanisms, and the distinction matters when we build systems expected to earn justified confidence."
hero: "img/posts/generation-is-not-inquiry/hero.jpg"
hero_alt: "Four-panel infographic: model inference as execution, text generation as an autoregressive loop, what generation lacks, and a real inquiry loop of observe, hypothesize, test, evaluate, revise"
---

We increasingly hear that artificial intelligence systems “run inference loops.” The phrase sounds stronger than the underlying mechanism usually warrants.

To a machine-learning engineer, *inference* can simply mean executing a trained model against new input. To a logician, scientist, or ordinary reader, inference suggests something richer: reasoning from premises, weighing evidence, drawing conclusions, testing explanations, and perhaps revising a conclusion when the evidence proves it wrong.

Those are different things.

For a deployed large language model, inference ordinarily means executing a model whose learned parameters are already fixed. Given some context, the model computes a probability distribution over possible next tokens, selects one according to its decoding procedure, adds that token to the context, and repeats.

In simplified form:

```
C_t  →  P(x_{t+1} | C_t)  →  x_{t+1}  →  C_{t+1}
```

The variables:

- **C_t**: the context at step *t*, meaning the original prompt plus every token generated so far.
- **P(x_{t+1} | C_t)**: the probability distribution the model computes over possible next tokens, given that context.
- **x_{t+1}**: the single token the decoding procedure selects, by greedy choice, sampling, or another rule.
- **C_{t+1}**: the context with that token appended, which becomes the input to the next step.

This is a genuine computational loop. It is an **autoregressive generation loop**.

It is not, by itself, an inquiry loop.

That distinction matters because much of the confusion surrounding generative AI begins when we slide unnoticed between these meanings of *inference*.

## Three different activities

At least three activities are routinely collapsed into the same vocabulary.

**Model inference** is the execution of a trained model against an input to produce an output.

**Generation** is the iterative production of tokens conditioned on the prompt, preceding tokens, model parameters, and decoding strategy.

**Inquiry** is an epistemic process in which observations constrain hypotheses, hypotheses entail testable expectations, evidence is gathered, alternatives are evaluated, and conclusions are revised accordingly.

The first two are intrinsic to ordinary LLM operation. The third requires additional machinery.

A basic model interaction looks approximately like this:

[
\text{Prompt} \rightarrow \text{Model Inference} \rightarrow \text{Generated Output}
]

Scientific or evidential inquiry has a different topology:

[
\text{Observation} \rightarrow \text{Hypothesis} \rightarrow \text{Prediction} \rightarrow \text{Test} \rightarrow \text{Evidence} \rightarrow \text{Revision}
]

The second process contains something the first does not necessarily possess: a mechanism by which reality can push back.

## The overloaded word “inference”

The terminology is legitimate. Machine-learning engineers did not invent the word carelessly.

In machine learning, *inference* conventionally means applying a trained model to new input to obtain a prediction or output. IBM and Google Cloud use the term in substantially this sense. Training adjusts model parameters. Inference applies the trained model.

In logic and epistemology, inference refers to movement from premises or evidence toward a conclusion.

The same word therefore operates at two different descriptive levels.

Consider the sentence:

> “The AI inferred that the network failure was caused by DNS.”

An engineer might mean that the model received diagnostic information and generated “DNS failure” as its output.

A reader might reasonably understand something considerably stronger: that the system examined evidence, considered competing causal explanations, derived their consequences, tested those consequences against observations, and concluded that DNS was the explanation best supported by the evidence.

Those descriptions are not equivalent.

The ambiguity encourages us to attribute epistemic properties to a computational operation merely because both are called *inference*.

## Deduction, induction, and abduction

The classical distinction among deduction, induction, and abduction helps clarify what generative AI is actually doing.

**Deduction** asks: Given these premises, what must follow?

If all humans are mortal and Socrates is human, then Socrates is mortal. The validity of the inference concerns the relationship between premises and conclusion.

LLMs can produce excellent deductive arguments. They can also lose track of premises, introduce unstated assumptions, or generate an invalid intermediate step. Their ability to produce deductive reasoning should therefore be distinguished from possessing a native computational mechanism that guarantees deductive validity.

**Induction** asks: What general pattern is supported by these observations?

There is a loose analogy here with machine learning itself. During training, models acquire statistical regularities from enormous collections of examples. During ordinary inference, however, the deployed model is not updating its learned parameters from each new answer. It is applying patterns acquired previously.

**Abduction** asks: What explanation best accounts for these observations?

This is particularly important for generative AI because many valuable LLM tasks have an abductive form.

Why did the server fail? What diagnosis explains these symptoms? What architectural defect could produce this behavior? What interpretation best explains this passage?

An LLM can generate remarkably plausible candidate explanations because its training enables it to model patterns connecting observations with explanations expressed in language.

But plausibility is not verification.

At the model-execution level, an autoregressive LLM repeatedly computes a conditional distribution over subsequent tokens. Whatever higher-order reasoning behavior emerges from that computation, the inference procedure itself supplies no independent criterion of truth.

Research into LLM reasoning supports caution here. Mondorf and Plank survey evidence that models can rely on surface patterns and correlations rather than stable reasoning procedures. Sheng et al. found that strong performance on familiar reasoning rules did not guarantee generalization to unseen rules across deductive, inductive, and abductive tasks.

## The token loop

The native loop of an autoregressive language model is comparatively straightforward:

[
\text{Context}
\rightarrow P(\text{next token})
\rightarrow \text{selected token}
\rightarrow \text{updated context}
\rightarrow \cdots
]

Each generated token becomes part of the context used to calculate the next one.

This iterative structure can produce something that looks remarkably like deliberation.

A model can write:

> “My first hypothesis is X. However, consideration Y weakens that explanation. Therefore, I should reconsider and adopt Z.”

The text describes reflection.

Nothing about the autoregressive loop itself establishes that X was tested, that Y came from an independent observation, or that Z corresponds more closely to reality.

Without external mechanisms, the model has no requirement to observe the world after making its initial claim. It has no mandatory falsification step. It need not construct competing hypotheses. It need not test their respective predictions. It does not ordinarily modify its trained parameters because its previous answer proved false.

Most importantly, token probability does not contain a truth predicate.

A highly probable continuation can be false. An improbable continuation can be true.

Fluency and truth frequently correlate because the model was trained on human-produced information in which useful linguistic and factual regularities exist. That correlation cannot bear the entire epistemic load.

## From a token loop to a truth-seeking system

This is where AI architecture becomes more interesting than the language model considered in isolation.

A model can be embedded inside a system that provides mechanisms the model itself lacks:

[
\text{Observe}
\rightarrow \text{Hypothesize}
\rightarrow \text{Derive Expectations}
\rightarrow \text{Test}
\rightarrow \text{Evaluate}
\rightarrow \text{Revise}
\rightarrow \text{Report or Act}
]

**Observe.** The system receives information that did not originate merely from its own previous generation. This might include documents, databases, source code, telemetry, sensor measurements, web resources, experimental results, or human testimony.

**Hypothesize.** The generative model proposes candidate explanations. This is where the abductive utility of generative AI becomes useful. The model can search a large conceptual space quickly and articulate possibilities a human investigator might otherwise overlook.

**Derive expectations.** If hypothesis (H) is correct, what should we observe?

[
H \rightarrow E
]

where (E) represents an expected observation.

**Test.** The system queries databases, executes code, searches authoritative sources, runs diagnostic commands, performs calculations, requests measurements, or asks a qualified human.

Now information can enter the process from outside the generative loop.

**Evaluate.** The observed result is compared with the expectation.

[
E_{\text{predicted}} \stackrel{?}{=} E_{\text{observed}}
]

Agreement increases the hypothesis's evidential support. Disagreement may weaken or falsify it, depending on the structure of the claim and test.

**Revise.** The system modifies its working hypothesis, confidence, plan, or final response.

Notice what need not happen here: the model's neural-network weights do not have to change. The *system state* can change even when the *model parameters* remain fixed.

That distinction is critical for agentic AI.

**Report or act.** The system communicates what was established, what remains uncertain, what evidence was used, and what assumptions remain unresolved.

At that point we have something substantially richer than autoregressive generation. We have an **evidence-bearing inquiry loop**.

## Models generate. Systems investigate.

The distinction suggests a useful architectural principle:

> **Models generate. Systems investigate.**

The language model is valuable precisely because generation is valuable.

It can propose hypotheses, formulate queries, derive implications, translate between representational forms, synthesize evidence, identify inconsistencies, write code, explain results, and recommend subsequent tests.

The stronger architecture appears when probabilistic generation is connected to deterministic computation, authoritative retrieval, empirical observation, logical validation, tool execution, and human judgment.

The model proposes. The environment constrains. Tools test. Evidence returns. The system revises.

This also explains why tool-augmented AI systems can have different reliability characteristics from isolated chatbots. A calculator can constrain arithmetic. A compiler can reject invalid syntax. A theorem prover can constrain formal derivations. A database can return authoritative records. A retrieval system can expose primary sources. A sensor can report an external state. A human expert can adjudicate questions requiring accountable judgment.

Each introduces constraints that do not originate solely from the model's probability distribution.

## The architectural question we should be asking

Asking whether an AI system “has an inference loop” tells us surprisingly little. Almost every deployed neural model performs inference in the machine-learning sense.

The useful questions are these:

- What information enters the system after generation?
- What could prove its proposed answer wrong?
- Does it generate competing explanations?
- Can it derive observations that would distinguish among them?
- Can it obtain those observations independently of its own generated text?
- What changes when the evidence contradicts the answer?

Those questions expose the actual epistemic architecture.

A system in which

[
\text{Generation} \rightarrow \text{Generation} \rightarrow \text{Generation}
]

is still operating within a generative loop, regardless of how many times it asks itself to “reflect.”

A system in which

[
\text{Generation}
\rightarrow \text{External Test}
\rightarrow \text{Evidence}
\rightarrow \text{Revision}
]

has crossed an important architectural boundary. Something outside the model can constrain what the model says.

## Designing AI for justified confidence

Where factual accuracy matters, systems should retrieve authoritative sources or primary data rather than relying solely on parametric memory.

Where causal explanation matters, systems should consider multiple hypotheses rather than immediately elaborating the first plausible explanation.

Where verification is possible, hypotheses should produce explicit expectations that can be checked. Where deterministic tools exist, those tools should constrain probabilistic generation. Where claims remain uncertain, the final response should preserve that uncertainty rather than allowing linguistic fluency to conceal it. Where consequences are substantial, qualified humans should remain accountable for judgment and action.

And when a model fails, the failure should be captured for evaluation, system improvement, or subsequent retraining. We should not describe an ordinary inference call as having “learned from its mistake” when no persistent learning occurred.

One useful progression is:

[
\text{Generation}
<
\text{Generation + Retrieval}
<
\text{Generation + Verification}
<
\text{Evidence-Bearing Inquiry}
]

The symbols represent increasing epistemic constraint, not a universal ranking of system capability. Different applications require different architectures.

A creative writing assistant may need little external verification. A medical, scientific, intelligence, financial, or engineering system requires considerably more.

## Generation is not inquiry

Generative AI is powerful enough that we do not need to exaggerate what its native mechanism does.

An LLM performs genuine machine-learning inference. It executes learned statistical structure against new context and generates outputs through an autoregressive decoding process. Those outputs can contain deductions, inductions, hypotheses, explanations, critiques, and even descriptions of the model correcting itself.

The production of reasoning-shaped language does not establish an evidence-bearing reasoning process.

Inquiry requires constraint. Something must be capable of telling the system that its attractive explanation is wrong.

That constraint may come from logic, computation, retrieved evidence, experimental observation, sensors, authoritative records, or human expertise. Whatever its source, it must introduce information that is not merely another continuation generated from the model's own prior text.

Do not merely ask:

> **Does the model have an inference loop?**

Ask:

> **What can falsify its output, and what happens when it does?**

That is the boundary between generating a plausible answer and building a system capable of earning justified confidence.

## References

IBM (n.d.) *What is LLM inference?* IBM Think. https://www.ibm.com/think/topics/llm-inference

Google Cloud (n.d.) *What is AI inference? How it works and examples.* https://cloud.google.com/discover/what-is-ai-inference

Mondorf, P. and Plank, B. (2024) ‘Beyond Accuracy: Evaluating the Reasoning Behavior of Large Language Models: A Survey’, *arXiv:2404.01869*. https://arxiv.org/abs/2404.01869

Sheng, Y., Wen, W., Li, L. and Zeng, D. (2025) ‘Evaluating Generalization Capability of Language Models across Abductive, Deductive and Inductive Logical Reasoning’, *Proceedings of the 31st International Conference on Computational Linguistics*, pp. 4945–4957. https://aclanthology.org/2025.coling-main.330/
