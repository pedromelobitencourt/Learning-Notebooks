# Neural Network Training

```
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(units=25, activation='sigmoid'),
    Dense(units=15, activation='sigmoid'),
    Dense(units=1, activation='sigmoid'),
])

from tensorflow.keras.losses import BinaryCrossentropy

model.compile(loss=BinaryCrossentropy)
```

With the *compile* function, we compile the model using a specific loss function

Now, to train the model:

```
model.fit(X, Y, epochs=100)
```

* **epochs**: number of steps in gradient descent

There are three steps in the model training:

1. Specify how to compute output given the input x

    model = Sequential([...])
    ![create-the-model-step](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/create_model_step.png)
2. Specify loss and cost

    model.compile(loss=BinaryCrossentropy) # Binary Cross Entropy

    L(f(x), y) = -ylog(f(x)) - (1-y)log(1 - f(x))
    ![loss-and-cost-functions-step](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/cost_loss_functions_step.png)
3. Train on data to minimize J(w, b)
    
    model.fit(X, Y, epochs=100)
    ![gradient-descent-step](/Machine%20Learning%20Specialization/Advanced%20Learning%20Algorithms/assets/module2/gradient_descent_step.png)

There are a lot more loss function, such as: MeanSquaredError (for regression problems)

