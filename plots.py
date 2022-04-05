import matplotlib.pyplot as plt
import numpy as np


def make_plots(image, result_image):

    image_srez = [i for i in image[int(image.shape[0] / 2)]]
    result_srez = [i for i in result_image[int(result_image.shape[0] / 2)]]

    plt.subplot(111)
    x = np.arange(0, int(image.shape[1]), 1)
    plt.plot(x, image_srez)

    plt.show()

    plt.subplot(111)
    x = np.arange(0, int(image.shape[1]), 1)
    plt.plot(x, result_srez)

    plt.show()
