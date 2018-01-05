import numpy as np
import cv2
from Image import Image
from Utils import Utils

class Main(object):

    def __init__(self):
        self.img = Image()
        self.utils = Utils()

    def menu(self):
        op = -1
        imagem = cv2.imread("bat.jpg", cv2.IMREAD_GRAYSCALE)
        cv2.imshow("bat", imagem)
        cv2.waitKey(0)
        while op != 0:
            op = input("Digite a opcao:\n1. Filtro\n2. Transformada\n3. Morfologia\n")
            if op == 1:
                imagem = cv2.imread("bat.jpg", cv2.IMREAD_GRAYSCALE)
                matriz = np.array([[-1, -1, -1],
                                   [0, 0, 0],
                                   [1, 1, 1]])
                cv2.imshow("filtro", self.img.applyFilter(imagem,matriz))

                cv2.waitKey(0)
            if op == 2:
                imagem = cv2.imread("bat.jpg", cv2.IMREAD_GRAYSCALE)
                cv2.imshow("transformada", self.img.transformIntoFrequencyImage(imagem))

                cv2.waitKey(0)
            if op == 3:
                imagem = cv2.imread("bat.jpg", cv2.IMREAD_GRAYSCALE)
                kernel = np.array([[1, 1], [1, 2], [1, 3], [2, 2]])
                op2 = input("Digite a opcao:\n1. Dilatacao\n2. Erosao\n3. Abertura\n4. Fechamento\n")
                if op2 == 1:
                    cv2.imshow('dilatacao', self.img.applyMorphologicalOperator(imagem, kernel, 1))
                if op2 == 2:
                    cv2.imshow('erosao', self.img.applyMorphologicalOperator(imagem, kernel, 2))
                if op2 == 3:
                    cv2.imshow('abertura',self.img.applyMorphologicalOperator(imagem, kernel, 3))
                if op2 == 4:
                    cv2.imshow('fechamento',self.img.applyMorphologicalOperator(imagem, kernel, 4))

                cv2.waitKey(0)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def video(self):
        min = [110,50,50]
        max = [130,255,255]
        video = cv2.VideoCapture("minions.mp4")
        self.utils.trackingOfRegionOfInterest(video,min,max)

    def filtro(self):
        imagem = cv2.imread("bat.jpg", cv2.IMREAD_GRAYSCALE)
        cv2.imshow("bat", imagem)
        cv2.waitKey(0)
        imagem = cv2.imread("bat.jpg", cv2.IMREAD_GRAYSCALE)
        matriz = np.array([[0.1, 0.1, 0.1],
                           [0.1, 0.1, 0.1],
                           [0.1, 0.1, 0.1]])
        cv2.imshow("filtro", self.img.applyFilter(imagem,matriz))
        cv2.waitKey(0)





        cv2.destroyAllWindows()


main = Main()
main.filtro()
#main.menu()
