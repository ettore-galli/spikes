from hello_iris.iris_prepare import prepare_iris_data


def perform_iris_deep_learning(iris_data_file: str):
    prepared_data = prepare_iris_data(iris_data_file)
    print(prepared_data)
