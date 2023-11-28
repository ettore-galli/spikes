import numpy as np


def positive(x, th, th0):
    # print(f"input: x={x}, th={th}, th0={th0}")
    measure = np.dot(th.T, x) + th0
    return np.sign(measure)


def signed_dist(x, th, th0):
    # (transpose(theta)@p + theta_0)/norm(theta)
    return (np.dot(th.T, x) + th0) / np.linalg.norm(th)


def rv(value_list):
    return np.array([value_list])


def score(data, labels, th, th0):
    return (positive(data, th, th0) == labels).sum()


def best_separator(data, labels, ths, th0s):
    scores = np.sum(np.sign(np.dot(ths.T, data) + th0s.T) == labels, axis=1)
    maxscore = np.argmax(scores)

    return (ths.T[maxscore]).T, th0s.T[maxscore].reshape(1, 1)


if __name__ == "__main__":
    data = np.transpose(np.array([[1, 2], [1, 3], [2, 1], [1, -1], [2, -1]]))
    labels = rv([-1, -1, +1, +1, +1])

    th = np.array([1, 1])
    th0 = -2
    p_positive = lambda p: positive(p, th, th0)

    result = p_positive(data)

    print(result)

    # print(th.T, data)
    # print(np.dot(th.T, data))

    print("-" * 50)

    # print(np.dot(th.T, data) + th0 == labels)
    # print(positive(data, th, th0) == labels)
    # print((positive(data, th, th0) == labels).sum())

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

    th0s = np.array([1, 2, 3, 0, 5])

    print(data)
    print(labels)
    print(ths)
    print(th0s)

    # Data
    print(data, labels, ths.T, th0s)

    # Progressive construction
    print(np.dot(ths.T, data))  # plane
    print(np.dot(ths.T, data) + th0s.T)  # with offset
    print(np.sign(np.dot(ths.T, data) + th0s.T))  # sign
    print(np.sign(np.dot(ths.T, data) + th0s.T) == labels)  # compared to labels
    print(np.sum(np.sign(np.dot(ths.T, data) + th0s.T) == labels, axis=1))  # scores

    data = np.transpose(np.array([[1, 2], [1, 3], [2, 1], [1, -1], [2, -1]]))
    scores = np.sum(np.sign(np.dot(ths.T, data) + th0s.T) == labels, axis=1)
    maxscore = np.argmax(scores)

    # d_ata = [
    #     [ 1  1  2  1  2]
    #     [ 2  3  1 -1 -1]
    # ]
    # l_abels = [[-1 -1  1  1  1]]
    # thetas = [
    #     [ 0.98645534 -0.02061321 -0.30421124 -0.62960452  0.61617711  0.17344772
    # -0.21804797  0.26093651  0.47179699  0.32548657]
    #     [ 0.87953335  0.39605039 -0.1105264   0.71212565 -0.39195678  0.00999743
    # -0.88220145 -0.73546501 -0.7769778  -0.83807759]
    # ]
    # thetaszeros= [
    #     [ 0.65043158  0.61626967  0.84632592 -0.43047804 -0.91768579 -0.3214327
    # 0.0682113  -0.20678004 -0.33963784  0.74308104]
    # ]

    print(scores, maxscore)

    print(ths.T[maxscore])
    print(th0s.T[maxscore])
    print(th0s.T[maxscore].reshape(1, 1))
    print(ths.T[maxscore], th0s.T[maxscore])

    print([x.tolist() for x in best_separator(data, labels, ths, th0s)])
