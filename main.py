from cv2 import imread, imshow, waitKey, IMREAD_GRAYSCALE


# Загрузка изображения
def load_image(text):
    image = imread(f'{text}', IMREAD_GRAYSCALE)
    return image


# Среднеарифметический фильтр
def mean_arithmetic(image):
    result_image = image.copy()

    for i in range(1, image.shape[0] - 2):
        for j in range(1, image.shape[1] - 2):

            mean = 0

            for di in range(-1, 2):
                for dj in range(-1, 2):
                    mean += image[i + di][j + dj]

            result_image[i][j] = mean / 9

    imshow('result-mean', result_image)
    waitKey(0)


# Гауссиан 3x3
def gaussian_3(image):
    mask = ((1, 2, 1), (2, 4, 2), (1, 2, 1))
    image_gaussian = image.copy()

    # Свертка
    for i in range(1, image.shape[0] - 2):
        for j in range(1, image.shape[1] - 2):

            z_x = 0

            for di in range(-1, 2):
                for dj in range(-1, 2):
                    z_x += image[i + di][j + dj] * mask[1 + di][1 + dj]

            image_gaussian[i][j] = z_x

    return image_gaussian


# Увеличение резкости
def increase_sharpness(image, image_gaussian):
    result_image = image.copy()

    mean_value = 0
    for i in range(0, image.shape[0] + 1):
        for j in range(0, image.shape[1] + 1):
            mean_value += image[i][j]
    mean_value = mean_value / image.shape[0] * image.shape[1]

    for i in range(1, image.shape[0] - 2):
        for j in range(1, image.shape[1] - 2):
            k_g = mean_value


if __name__ == '__main__':
    var_text = 'people_shum.jpg'
    var_image = load_image(var_text)
    mean_arithmetic(var_image)
