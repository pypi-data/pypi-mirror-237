# survshap

<!-- badges: start -->
<!-- badges: end -->

## Overview 
The `survshap` package contains an implementation of the **SurvSHAP(t)** method, the first time-dependent explanation method for interpreting survival black-box models. It is based on SHapley Additive exPlanations (SHAP) but extends it to the time-dependent setting of survival analysis. SurvSHAP(t) is able to detect time-dependent variable effects and its aggregation determines the local variable importance.

Read more about SurvSHAP(t) in [our paper](https://doi.org/10.1016/j.knosys.2022.110234).

## Installation
```python
pip install survshap
```

## Citation
If you use this package, please cite our paper:
    
```bib
@article{survshap,
    title = {SurvSHAP(t): Time-dependent explanations of machine learning survival models},
    journal = {Knowledge-Based Systems},
    volume = {262},
    pages = {110234},
    year = {2023},
    issn = {0950-7051}
    }
```
