# Introduction

Mjölnir is an interpretable machine learning model informed by causal assumptions.

![](assets/thor.jpg)

# Installation

`pip install Thor-Hammer`

# Features

- Causal assumptions are enforced by a user-specified directed acyclic graph.
- Uncertainty is quantified automatically using conformal prediction.
- Symbolic expressions that can be analyzed are produced by training the model.
- The model follows the SKLearn API, so it can be included in instances of [`sklearn.pipeline.Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html).

# Quick Start

```python
from thorshammer import Mjolnir

model = Mjolnir(...)
model.fit(X_train)
model.predict(X_test)
```
