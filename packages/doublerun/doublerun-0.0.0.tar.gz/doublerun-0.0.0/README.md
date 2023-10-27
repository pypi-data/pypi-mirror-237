# Introduction 

This repository was created to provide reusable tools for validating "double-runs" in the context of the Cockpit migration project, but also for other refactoring projects (MLOps, LACI, etc.).

# Getting Started

Inside the `src/doublerun/` folder, you will find two scripts:
* `pandas.py`: Contains functions for checking that 2 `pandas` `DataFrames` are equal or spot their differences.
* `spark.py` : Contains functions for checking that 2 `spark` `DataFrames` are equal or spot their differences.

Inside the `examples` folder, you will find notebooks detailing how these tools could be used.

# Contributing

In order to contribute, create your branch with a meaningful title representing a feature you would like to develop (Examples: `pandas_visualisation_mismatches`, `pandas_high_perf_dask`, `spark_notebooks`, etc.). Please, have a look at existing branches before creating a new one.

Then, make a pull request to the `dev` branch to make sure no conflicts are created when we will be merging multiple branches together.

When writing a new function or modifying someone else's, feel free to add your name to the docstring so that people can contact you for help. Example:

```py
def some_function(df1, df2):
    """
    This functions does this and that.

    args :
        df1, df2 -> DataFrames to do stuff on.

    authors:
        Pierre Adeikalam : pierre.adeikalam@axa-direct.com (Creator)
        John Doe : john.doe@axa-direct.com (Contributor)
    """
```