import numpy as np


def rv(value_list):
    return np.array([value_list])


# Progressive construction
# print(np.dot(ths, data))  # plane
# print(np.dot(ths, data) + th0s.T)  # with offset
# print(np.sign(np.dot(ths, data) + th0s.T))  # sign
# print(np.sign(np.dot(ths, data) + th0s.T) == labels)  # compared to labels
# print(np.sum(np.sign(np.dot(ths, data) + th0s.T) == labels, axis=1))  # scores


# WORKING!!!
def best_separator(data, labels, ths, th0s):
    scores = np.sum(np.sign(np.dot(ths.T, data) + th0s.T) == labels, axis=1)
    maxscore = np.argmax(scores)

    return np.array([ths.T[maxscore]]).T, th0s.T[maxscore].reshape(1, 1)


# WORKING!!!
def best_separator_2(data, labels, ths, th0s):
    scores = np.sum(
        np.sign(np.dot(ths.T, data) + th0s.T) == labels, axis=1, keepdims=True
    )
    maxscore = np.argmax(scores)

    return np.array([ths[:, maxscore]]).T, np.array([th0s])[:, maxscore : maxscore + 1]


if __name__ == "__main__":
    data = np.transpose(np.array([[1, 2], [1, 3], [2, 1], [1, -1], [2, -1]]))
    labels = rv([-1, -1, +1, +1, +1])

    ths = np.array(
        [
            [1, 1],
            [2, 2],
            [3, 3],
            [4, -4],
            [5, -5],
            [6, -6],
            [7, -7],
            [8, -1],
            [9, -1],
            [10, -1],
        ]
    ).T

    th0s = np.array([1, 2, 3, 0, 5, 1, 1, 1, 1])

    # print(data, labels, ths.T, th0s)

    # print("equals")
    # print(np.sign(np.dot(ths.T, data) + th0s.T) == labels)
    # print("scores: sum axis 1")
    # print(np.sum(np.sign(np.dot(ths.T, data) + th0s.T) == labels, axis=1))
    # print("scores: sum keepdims true")

    # scores = np.sum(
    #     np.sign(np.dot(ths.T, data) + th0s.T) == labels, axis=1, keepdims=True
    # )
    # maxscore = np.argmax(scores)
    # print(maxscore)
    print([x.tolist() for x in best_separator(data, labels, ths, th0s)])
    print([x.tolist() for x in best_separator_2(data, labels, ths, th0s)])
