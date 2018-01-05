import cv2
import numpy as np
from matplotlib import pyplot as plt

class Image:
    path = ""
    image = ""

    def __init__(self):
        path = ""
        image = ""

    def openBWImage(self, path):
        self.path = path;
        self.image = cv2.imread(path, 0)
        return self.image

    def openColoredImage(self, path):
        self.path = path;
        self.image = cv2.imread(path)
        return self.image

    def showImg(self):
        cv2.imshow("", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def saveImage(self):
        cv2.imwrite(self.path, self.image)

    def saveInDiffentPath(self, path):
        cv2.imwrite(path, self.image)

    def setColor(self, positionX, positionY, channel, value):
        (b, g, r) = self.image[positionY, positionX]
        if channel == 0:
            self.image[positionY, positionX] = (value, g, r)
        elif channel == 1:
            self.image[positionY, positionX] = (b, value, r)
        else:
            self.image[positionY, positionX] = (b, g, value)

    def turnColoredImageIntoBW(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return self.image

    def equalizeImage(self, img):
        img = cv2.resize(img, (500,500))
        height, width = img.shape
        histograma = []
        probabilidadeDcor = []
        probabilidadeAcumulada = []
        novoTomMapeado = []

        for i in range(256):
            histograma.append(0)
            probabilidadeDcor.append(0.0)
            probabilidadeAcumulada.append(0.0)
            novoTomMapeado.append(0)

        for i in range(0, height):
            for k in range(0, width):
                histograma[img[i][k]] = histograma[img[i][k]] + 1

        numeroDpixels = width * height

        for i in range(256):
            probabilidadeDcor[i] = float(histograma[i]) / float(numeroDpixels)

        probabilidadeAcumulada[0] = probabilidadeDcor[0]
        for i in range(256):
            probabilidadeAcumulada[i] = probabilidadeAcumulada[i - 1] + probabilidadeDcor[i]

        print (probabilidadeAcumulada)
        for i in range(256):
            novoTomMapeado[i] = float(probabilidadeAcumulada[i] * 255)

        print(novoTomMapeado)
        for i in range(0, height):
            for k in range(0, width):
                img[i][k] = (novoTomMapeado[img[i][k]])

        return img

    def applyFilter(self, img, matriz):
        print matriz
        w, h = img.shape
        filtroWeigth = len(matriz)
        filtroHeigth = len(matriz)
        aux = 0
        imgfinal = np.copy(img)
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                for filtroW in range(len(matriz)):
                    for filtroH in range(len(matriz)):
                        imageX = (x - filtroWeigth / 2 + filtroW + w) % w
                        imageY = (y - filtroHeigth / 2 + filtroH + h) % h
                        aux += matriz[filtroW][filtroH] * img[imageX][imageY]
                imgfinal[x][y] = int(aux)
                aux = 0
        return imgfinal

    def transformIntoFrequencyImage(self, img):
        height, width = img.shape
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)
        magnitude = 20 * np.log(np.abs(fshift))
        for i in range(0, height):
            for j in range(0, width):
                img[i][j] = int(magnitude[i][j])
            if (int(magnitude[i][j]) > 255):
                img[i][j] = 255
        return img

    def applyMorphologicalOperator(self, image, structElement, operation):
        if operation == 1:
            img = cv2.dilate(image,structElement,iterations=1)
        if operation == 2:
            img = cv2.erode(image,structElement,iterations=1)
        if operation == 3:
            img = cv2.morphologyEx(image, cv2.MORPH_OPEN, structElement)
        if operation == 4:
            img = cv2.morphologyEx(image, cv2.MORPH_CLOSE, structElement)

        return img