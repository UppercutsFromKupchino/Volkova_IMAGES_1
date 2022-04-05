from cv2 import imread, imshow, waitKey, IMREAD_GRAYSCALE, imwrite
import numpy as np
from math import sqrt
from plots import make_plots


# Загрузка изображения
def load_image(text):
    text += '.jpg'
    image = imread(f'{text}', IMREAD_GRAYSCALE)
    return image


# Увеличение резкости
def increase_sharpness(image, text):
    mask_gauss = ((1, 2, 1), (2, 4, 2), (1, 2, 1))
    result_image = image.copy()
    result_image = result_image.astype(np.int32)
    mean_value = 0
    k = 0.5

    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            mean_value += image[i][j]
    mean_value = mean_value / (image.shape[0] * image.shape[1])

    for i in range(1, image.shape[0] - 2):
        for j in range(1, image.shape[1] - 2):

            z_mean = 0
            z_gaussian = 0

            for di in range(-1, 2):
                for dj in range(-1, 2):
                    z_mean += image[i + di][j + dj] ** 2
                    z_gaussian += image[i + di][j + dj] * mask_gauss[1 + di][1 + dj]
            z_mean = sqrt(z_mean / 9)
            if z_mean < 0.01:
                result_image[i][j] = z_gaussian + (image[i][j] - z_gaussian)
            else:
                result_image[i][j] = z_gaussian + ((k * mean_value / z_mean) * (image[i][j] - z_gaussian))

    min_result_image = min(result_image.ravel())
    coeff = (max(result_image.ravel()) + abs(min_result_image)) / 256

    for i in range(1, result_image.shape[0] - 2):
        for j in range(1, result_image.shape[1] - 2):
            result_image[i][j] += abs(min_result_image)
            result_image[i][j] = int(result_image[i][j] / coeff)

    result_image = result_image.astype(np.uint8)

    imshow('result', result_image)
    waitKey(0)
    imwrite(f'{text}-result.jpg', result_image)

    return result_image


if __name__ == '__main__':
    var_text = 'people'
    var_image = load_image(var_text)
    result = increase_sharpness(var_image, var_text)
    make_plots(var_image, result)
