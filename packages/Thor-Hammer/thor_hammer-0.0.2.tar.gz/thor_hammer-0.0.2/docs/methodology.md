---
hide: 
    - navigation
comments: true
---

# Causal Assumptions

Mjölnir takes causal assumptions from the user in the form of a directed acyclic graph on the variables of interest.

# Conformal Prediction

[*Conformal prediction (CP) is a machine learning framework for uncertainty quantification that can produce prediction regions (prediction intervals) for any underlying point predictor (where statistical, machine or deep learning) only assuming exchangeability of the data.*](https://en.wikipedia.org/wiki/Conformal_prediction) Anastasios N. Angelopoulos and Stephen Bates provide [*A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification*](https://arxiv.org/abs/2107.07511). They also produced the following education videos providing an introduction and discussion of conformal prediction.

<iframe width="560" height="315" src="https://www.youtube.com/embed/nql000Lu_iE?si=5_xQ4VGE3p_SbB_-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/TRx4a2u-j7M?si=z9KY4KmwrK5CuGBh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/37HKrmA5gJE?si=CQInpwy_Kc91t_RL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Mjölnir uses the [MAPIE](https://mapie.readthedocs.io/en/latest/) package to provide conformal prediction.

# Symbolic Regression

Mjölnir learns symbolic expressions which are optimized to be accurate and simple. This is accomplished via genetic programming which searches a space of possible expression trees via generating generations of expressions and selecting based on accuracy and simplicity in terms of the expression tree structure.

Mjölnir uses the [gplearn](https://gplearn.readthedocs.io/en/stable/) package to provide symbolic regression via genetic programming.

# Computer Algebra System

Mjölnir provides Sympy expressions of the symbolic expressions learned in the symbolic regression. This provides a means of using conventional mathematical techniques to understand the model. Mjölnir also has some specialized methods for answering questions relevant to model understanding such as stationary points.

# Do-Calculus

In the future Mjölnir will be equipped with [do-calculus](https://plato.stanford.edu/entries/causal-models/do-calculus.html) operations so that the underlying causal DAG can be modified to identify causal estimators.
