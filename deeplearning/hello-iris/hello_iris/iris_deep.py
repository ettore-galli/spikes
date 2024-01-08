import keras
import numpy as np
from sklearn.model_selection import train_test_split

from hello_iris.iris_prepare import prepare_iris_data, rescale_input


def create_model() -> keras.models.Model:
    # Number of classes in the target variable
    nb_classes = 3

    # Create a sequencial model in Keras
    model = keras.models.Sequential()

    # Add the first hidden layer
    model.add(
        keras.layers.Dense(
            128,  # Number of nodes
            input_shape=(4,),  # Number of input variables
            name="Hidden-Layer-1",  # Logical name
            activation="relu",
        )
    )  # activation function

    # Add a second hidden layer
    model.add(keras.layers.Dense(128, name="Hidden-Layer-2", activation="relu"))

    # Add an output layer with softmax activation
    model.add(keras.layers.Dense(nb_classes, name="Output-Layer", activation="softmax"))

    # Compile the model with loss & metrics
    model.compile(loss="categorical_crossentropy", metrics=["accuracy"])

    return model


def train_model(
    model: keras.models.Model, features: np.ndarray, target: np.ndarray
) -> keras.models.Model:
    # Make it verbose so we can see the progress
    verbose = 1

    # Setup Hyper Parameters for training

    # Set Batch size
    batch_size = 16
    # Set number of epochs
    epochs = 10
    # Set validation split. 20% of the training data will be used for validation
    # after each epoch
    validation_split = 0.2

    x_train, x_test, y_train, y_test = train_test_split(
        features, target, test_size=0.10
    )

    # Fit the model. This will perform the entire training cycle, including
    # forward propagation, loss computation, backward propagation and gradient descent.
    # Execute for the specified batch sizes and epoch
    # Perform validation after each epoch
    history = model.fit(
        x_train,
        y_train,
        batch_size=batch_size,
        epochs=epochs,
        verbose=verbose,
        validation_split=validation_split,
    )

    evaluation_over_test = model.evaluate(x_test, y_test)
    return model, history, evaluation_over_test


def perform_iris_deep_learning(iris_data_file: str):
    features, target, reverse_map = prepare_iris_data(iris_data_file)
    model = create_model()
    print(features, target)

    trained_model, training_history, evaluation_over_test = train_model(
        model=model, features=features, target=target
    )

    print(trained_model)
    print(training_history)
    print(evaluation_over_test)

    prediction_input = [[6.6, 3.0, 4.4, 1.4]]

    # Scale prediction data with the same scaling model
    scaled_input = rescale_input(np.array(prediction_input))

    # Get raw prediction probabilities
    raw_prediction = model.predict(scaled_input)
    print("Raw Prediction Output (Probabilities) :", raw_prediction)

    # Find prediction
    prediction = np.argmax(raw_prediction)
    print("Prediction is ", reverse_map.get(prediction))
