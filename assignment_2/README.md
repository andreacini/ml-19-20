# Assignment 2

In this assignment you are asked to:

1. Implement a neural network to classify images;
2. Operate on some hyper-parameters to improve the performance.

Both requests are very similar to what we have seen during the labs, but require you to follow **exactly** our specifications. 

Once completed, please submit your solution on the iCorsi platform following subsequent indications. 


## Tasks

Implement a multi-class classifier to identify the subject of images (airplane, automobile and bird) from [CIFAR-10](https://www.cs.toronto.edu/%7Ekriz/cifar.html) data set.


### T1. Follow our recipe

1. Download and load CIFAR-10 dataset using the following [function](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10/load_data), and consider only the first three classes (Check `src/utils.py`, we already provided you with a function for this!)
2. Preprocess the data:
    - Normalize each pixel of each channel so that the range is [0, 1];
    - Create one-hot encoding of the labels.
3. Build a neural network with the following architecture: 
    - Convolutional layer, with 8 filters of size 5 by 5, stride of 1 by 1, and ReLU activation;
    - Max pooling layer, with pooling size of 2 by 2;
    - Convolutional layer, with 16 filters of size 3 by 3, stride of 2 by 2, and ReLU activation;
    - Average pooling layer, with pooling size of 2 by 2;
    - Layer to convert the 2D feature maps to flat vectors;
    - Dense layer with 8 neurons and tanh activation;
    - Dense output layer with softmax activation;
    - **Bonus** (Optional): modify the model as follows: 
        + Add a dropout layer with dropout probability of 0.3 before each Dense layer;
        + Add L2 regularization with factor 0.005 on the weights to every Dense layer 
        + Use Leaky ReLU activations instead of ReLU ones. Set the slope of the Leaky ReLU for `x < 0` to 0.15.
4. Train the model on the training set from point 1 for 500 epochs:
    - Use the RMSprop optimization algorithm, with a learning rate of 0.003 and a batch size of 128;
    - Use categorical cross-entropy as a loss function;
    - Implement early stopping, monitoring the validation accuracy of the model with a patience of 10 epochs and use 20% of the training data as validation set;
    - When early stopping kicks in, and the training procedure stops, restore the best model found during training.
5. Draw a plot with epochs on the x-axis and with two graphs: the train accuracy and validation accuracy (remember to add a legend to distinguish the two graphs!).
6. Assess the performance of the network on the test set loaded in point 1, and provide an estimate of the classification accuracy that you expect on new and unseen images. 


### T2. Hyper-parameter tuning

Tune the learning rate and the number of neurons in the last dense hidden layer with a grid search.

- Consider the following ranges for the two hyper-parameters:
    + learning rate: [0.01, 0.0001]
    + number of neurons: [8, 64]
- Keep all the other hyper-parameters as in task T1.
- Perform a grid search on the chosen ranges basing on hold-out cross-validation in the training set and identify the most promising hyper-parameter setup  
- Compare accuracy on the test set achieved by the most promising configuration with that of the model obtained in task T1. Are the accuracy levels statistically different?

Use training and test sets from point 1, task T1, and use 20% of the training data as validation set.


## Instructions

### Tools

Your solution must be entirely coded in **Python 3** ([not Python 2](https://python3statement.org/)).
We recommend to use Keras from TensorFlow2 that we seen in the labs, so that you can reuse the code in there as reference. 

All the required tasks can be completed using Keras. On the [documentation page](https://www.tensorflow.org/api_docs/python/tf/keras/) there is a useful search field that allows you to smoothly find what you are looking for. 
You can develop your code in Colab, where you have access to a GPU, or you can install the libraries on your machine and develop locally.


### Submission

In order to complete the assignment, you must submit a zip file named `as2_surname_name.zip` on the iCorsi platform containing: 

1. the two saved models, say `nn_task1.h5` and `nn_task2.h5`. 
2. a working example `run_models.py` that loads the test set in CIFAR-10 dataset, preprocesses the data, loads the two trained models from file and evaluate their accuracy;
3. a folder `src` with all the source code you used to build, train, and evaluate your models.

The Zip file should eventually look like as follows

```
as2_surname_name/
    deliverable/
        run_models.py
        nn_task1.h5  # or any other file storing the model from task T1
        nn_task2.h5  # or any other file storing the model from task T2
    src/
        file1.py
        file2.py
        ...
```


### Evaluation criteria

You will get a positive evaluation if:

- your code runs out of the box (i.e., without us needing to change your code to evaluate the assignment);
- your code is properly commented;
- the performance assessment is conducted appropriately;

You will get a negative evaluation if: 

- we realize that you copied your solution;
- your code requires us to edit things manually in order to work;
- you did not follow our detailed instructions in tasks T1 and T2.

Bonus parts are optional and are not required to achieve the maximum grade, however they can grants you extra points.

