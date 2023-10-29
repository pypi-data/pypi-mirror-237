import numpy as np
import matplotlib.pyplot as plt

def show(subplot: tuple, mat: list, figsize=(10, 10)):
    fig, ax = plt.subplots(subplot[0], subplot[1], figsize=figsize)
    for i, axi in enumerate(ax):
        axi.imshow((mat[i].numpy() / 2 + 0.5))
        axi.axis('off')
    
    plt.show()

def save(path, mat):
    # img = mat / 2 + 0.5
    img = mat
    plt.imsave(path, img)


def cos_sim(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
