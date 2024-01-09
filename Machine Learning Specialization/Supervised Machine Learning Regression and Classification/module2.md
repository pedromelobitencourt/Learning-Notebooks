# Multiple Linear Regression

It can use, not only one feature, but a lot of features

It's not multivariate regression

In the house price example, we had only the size of the house (x1). What if we have the number of bedrooms (x2), number of floors (x3), age of home (x4) as well?

* **x<sub>j</sub>**: j<sup>th</sup> feature
* **n**: number of features
* **x<sup>i</sup>**: features of i<sup>th</sup> training example
* **x<sub>j</sub><sup>i</sup>**: value of feature j in i<sup>th</sup> training example

Now, the model will be:

* **f<sub>w, b</sub>** = w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub> + w<sub>3</sub>x<sub>3</sub> + w<sub>4</sub>x<sub>4</sub> + b

* b: base price

Example: f<sub>w, b</sub> = 0.1x<sub>1</sub> + 4x<sub>2</sub> + 10x<sub>3</sub> - 2x<sub>4</sub> + 80


In a more general way:

* **f<sub>w, b</sub>** = w<sub>1</sub>x<sub>1</sub> + w<sub>2</sub>x<sub>2</sub> + ... + w<sub>n</sub>x<sub>n</sub> + b = w · x + b

* **Vector *w***: w = [w<sub>1</sub> + w<sub>2</sub> + w<sub>3</sub> + ... + w<sub>n</sub>]

* **Vector *x***: x = [x<sub>1</sub> + x<sub>2</sub> + x<sub>3</sub> + ... + x<sub>n</sub>]
 
* **b**: number


Vector *w* and *b* are the parameters of the model