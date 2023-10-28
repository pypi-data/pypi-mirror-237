<p align="center" style="text-align:center">
  <img src="resources/sensai-logo.png" style="width:400px"><br>
  the Python library for sensible AI

  <div align="center" style="text-align:center">
  <a href="https://pypi.org/project/sensai/">
      <img src="https://img.shields.io/pypi/v/sensai.svg" alt="PyPI">
  </a>
  <a href="https://raw.githubusercontent.com/jambit/sensAI/master/LICENSE">
        <img alt="License" src="https://img.shields.io/pypi/l/sensai">
  </a>
  <a href="https://github.com/jambit/sensAI/actions/workflows/tox.yaml">
        <img src="https://github.com/jambit/sensAI/actions/workflows/tox.yaml/badge.svg" alt="Build status">
  </a>
  </div>
</p>


## About sensAI

sensAI provides a framework for AI and machine learning applications, integrating industry-standard libraries and providing additional abstractions that facilitate rapid implementation, experimentation as well as deployment. 

In particular, sensAI provides ...

* **machine learning** methods
  * **regression and classification** models
    * unified interface to models and algorithms of other machine learning libraries, particularly **scikit-learn**, **PyTorch** and **TensorFlow**
    * additional implementations of our own, e.g. for k-nearest neighbour models and naive Bayes models
  * mechanisms for **feature generation**, which serve to decouple externally provided input data from the data that is actually required as input to particular models
  * mechanisms for model-specific (input and output) **data transformation**, enabling, for example, convenient model-specific scaling/normalisation or encodings of features
  * (parallelised) **hyper-parameter optimisation** methods
  * **cloud-based tracking** of experimental results (with direct support for Microsoft Azure)
* **combinatorial optimisation**
  * **stochastic local search** methods, including (adaptive) simulated annealing and parallel tempering
* general utilities, including ...
  * extensive **caching mechanisms** (using SQLite, pickle and MySQL as backends)
  * multi-processing tools, e.g. a debugger for pickle errors

## Documentation

Reference documentation and tutorials can be found [here](https://jambit.github.io/sensAI/docs/).

### Integrating sensAI into a Project

sensAI may be integrated into your project in several ways: 

1. **Install it as a library** with `pip install sensai`.
   Choose this option as a regular user of sensAI with no intention of extending
   the library as part of your work.
2. **Include sensAI's source code as a package within your project** (e.g. in `src/sensai`), which you synchronise with a sensAI branch.
   Choose this option if you intend to make changes to sensAI as you develop your project. When using this option, you (and others) may even make changes to sensAI in several branches of your project and even several projects using the same inclusion mechanism at the same time.
   See developer documentation in README-dev.md for details on how synchronisation works.


## Contributors

sensAI is being developed by the artificial intelligence group at [jambit GmbH](http://www.jambit.com) and by members of [appliedAI](http://www.appliedai.de).

The main contributors are Dominik Jain, Michael Panchenko, Kristof Schröder and Magnus Winter.

### How to contribute 

External contributions are welcome! Please issue a pull request.

#### Code Style

If you decide to contribute, please strive for consistency with the existing codebase.
