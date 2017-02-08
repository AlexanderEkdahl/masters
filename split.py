import random


def split_train_test(dataset, ratio=0.3):
    train, test = [], []

    for datapoint in dataset:
        if random.random() > ratio:
            train.append(datapoint)
        else:
            test.append(datapoint)

    return (train, test)
