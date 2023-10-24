# Parkinson-detect

![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)
![Python 3.8](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue)


**Parkinson Detect** 

 
### 00 Colab Examples:
* Pretrained 🎯
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]()


* Trained from scratch 🎯
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]()

### 01 Install 🚀
The library has been tested on Linux, MacOSX and Windows. It relies on the following Python modules:

Pandas
Numpy
Scipy
Scikit-learn
Pytorch

Parkinson detect can be installed from [PyPI](https://pypi.org/project/Parkinson-detect):

<pre>
pip install parkinson-detect
</pre>

#### Post installation check
After a correct installation, you should be able to import the module without errors:

```python
import parkinson as pk
```

### 02 Parkinson example on sampled data step by step ➡️


#### 1️⃣ Load the Data 💽


```python

import parkinson as pk
df = dataset_test()

```


#### 2️⃣ Load the trained model or train your model ⚙️

```python
from parkinson import Resnet34


# Create an XGBoost classifier object
resnet = Resnet34(eval_metric="error")

# Train the XGBoost classifier on the training data
model = resnet.fit(X_train, y_train)
```

#### 3️⃣ Monitor Performance 📈





#### 4️⃣ Visualisation 📊


##### Beeswarn plot

```python
import pandas as pd
from parkinson import viz

viz.beeswarn_plot()
```
![sample](images/chart5.png)


### 03 Acknowledgements

The contributors to this library are 
* [Anas Filali]()
* [Mounim A El-Yacoubi]()
* [Dijana Petrovska-Delacrétaz]()
* [AhmedZaiou]()
* [Gaëtan Brison]()


### 04 Reference

Anas Filali (1, 2, 3) , Laetitia Jeancolas (4) , Graziella Mangone (5) , Sara Sambin (5) , Alizé Chalançon (5) , Manon Gomes (5) , Stéphane Lehéricy (5) , Jean-Christophe Corvol (5) , Marie Vidailhet (5) , Isabelle Arnulf (5) , Mounim A El-Yacoubi (3) , Mounim El Yacoubi (1, 2, 3) , Dijana Petrovska-Delacrétaz (1, 2, 3). "Early-stage parkinson's disease detection based on action unit derivatives". Available at https://hal.science/hal-04178781


1 IP Paris - Institut Polytechnique de Paris
2 TSP - EPH - Département Electronique et Physique
3 ARMEDIA-SAMOVAR - ARMEDIA
4 Concordia University Montreal
5 ICM - Institut du Cerveau - Paris Brain Institute
