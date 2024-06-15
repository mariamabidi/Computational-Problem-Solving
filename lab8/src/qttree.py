__author__ = 'MA'
"""
CSCI-603 Lab 8: Image Viewer 

A program to view images from compressed and uncompressed file.

Author: Mariam Abidi
"""
import math
from qtnode import QTNode
from qtexception import QTException


class QTTree:
    """
    Quadtree Data Structure class.
    """
    __slots__ = "root", "current_level_nodes"
    _root = 'QTNode'

    def __init__(self, value: 'QTNode' = None):
        """
        Constructor
        """
        self.root = value

    def get_root(self):
        """
        Getter for root
        """
        return self.root

    def set_root(self, value: 'QTNode'):
        """
        Setter for root
        """
        self.root = value

    def uncompressed_file(self, filename: str) -> tuple[list[list[int]], int]:
        """
        A function to read the uncompressed file and make a 2d array.

        @param filename The name file to read
        """

        filename = "../images/uncompressed/" + filename
        baseRawImageFile = list()
        rawImageFile = list()
        try:
            with open(filename) as f:
                for lines in f:
                    lines = lines.strip()
                    baseRawImageFile.append(int(lines))
            length_of_file = len(baseRawImageFile)

            power = int(length_of_file**0.5)
            if type(power) is not int:
                raise QTException("Image Size not a square")

            for pixels in range(0, len(baseRawImageFile), power):
                row = baseRawImageFile[pixels:pixels+power]
                rawImageFile.append(row)
            return rawImageFile, power

        except FileNotFoundError:
            raise QTException("FILE NOT FOUND!")
        except QTException as e:
            print(e)
        except Exception as e:
            raise QTException(f"An error occurred: {e}")

    def reconstruct_matrix(self, arr, size):
        """
        A function to reconstruct the list of rawImage list.

        @param arr The list to reconstruct
        @param size The size of the image.
        """

        if size == 1:
            return [[arr.pop(0)]]

        new_size = size // 2
        ul = self.reconstruct_matrix(arr, new_size)  # Upper Left
        ur = self.reconstruct_matrix(arr, new_size)  # Upper Right
        ll = self.reconstruct_matrix(arr, new_size)  # Lower Left
        lr = self.reconstruct_matrix(arr, new_size)  # Lower Right

        return ([ul_row + ur_row for ul_row, ur_row in zip(ul, ur)] +
                [ll_row + lr_row for ll_row, lr_row in zip(ll, lr)])

    def compressed_file(self, filename: str):
        """
        A function to read the compressed file, make a quadtree
         then make a rawImageFile and then turn it into a 2d array.

        @param filename The name file to read
        """

        filename = "../images/compressed/" + filename
        rawImageFile = list()
        baseRawImageFile = list()
        try:
            with open(filename) as f:
                number_of_pixels = int(f.readline())
                if number_of_pixels > 0 and (number_of_pixels
                                             & (number_of_pixels - 1)) == 0:
                    for lines in f:
                        baseRawImageFile.append(int(lines.strip()))
                else:
                    raise QTException("IMAGE SIZE IS NOT A SQUARE!")

                tree = self.makeQT(baseRawImageFile, 1, 0)[0]
                print("Quadtree:", tree.preorder(tree))
                oldrawImage = self.qt_to_rawImage(tree, number_of_pixels, [])[1]
                power = int(int(len(oldrawImage)) ** 0.5)
                if type(power) is not int:
                    raise QTException("Image Size not a square")
                rawImageFile = self.reconstruct_matrix(oldrawImage, power)

                return rawImageFile, power

        except QTException as e:
            print(e)
        except FileNotFoundError:
            raise QTException("FILE NOT FOUND!")

    def makeQT(self, compressedFileList: list, i, level):
        """
        A function to make a quadtree out of a compressed image file list.

        @param compressedFileList The compressed image file list.
        @param i
        @param level
        """

        newNode = QTNode(compressedFileList[0], level = level)
        level += 1
        if i < len(compressedFileList):
            if compressedFileList[i] != -1:
                newNode.set_upper_left(QTNode(compressedFileList[i],level = level))
                i += 1
            else:
                rec, m = self.makeQT(compressedFileList[i:], 1,level = level)
                newNode.set_upper_left(rec)
                i = i+m

        if i < len(compressedFileList):
            if compressedFileList[i] != -1:
                newNode.set_upper_right(QTNode(compressedFileList[i],level = level))
                i += 1
            else:
                rec, m = self.makeQT(compressedFileList[i:], 1, level = level)
                newNode.set_upper_right(rec)
                i = i+m

        if i < len(compressedFileList):
            if compressedFileList[i] != -1:
                newNode.set_lower_left(QTNode(compressedFileList[i],level = level))
                i += 1
            else:
                rec, m = self.makeQT(compressedFileList[i:], 1,level = level)
                newNode.set_lower_left(rec)
                i = i+m

        if i < len(compressedFileList):
            if compressedFileList[i] != -1:
                newNode.set_lower_right(QTNode(compressedFileList[i],level = level))
                i += 1
            else:
                rec, m = self.makeQT(compressedFileList[i:], 1, level = level)
                newNode.set_lower_right(rec)
                i = i+m

        if compressedFileList[0] != -1:
            return QTNode(compressedFileList[0],level = level)
        else:
            self.root = newNode
            return self.root, i

    def qt_to_rawImage(self, tree: 'QTNode', pixels: int, elements: list):
        """
        A function to read a quadtree into a list.
        """
        level = int(math.log(pixels, 4))
        if tree is not None:
            if (tree.get_upper_left() is None and tree.get_upper_right() is None
                    and tree.get_lower_left() is None and tree.get_lower_right() is None):
                deno = 4**tree.get_level()
                times = pixels//deno
                for _ in range(times):
                    elements.append(tree.get_value())

            if tree.get_level() <= level:
                self.qt_to_rawImage(tree.get_upper_left(), pixels, elements)
                self.qt_to_rawImage(tree.get_upper_right(), pixels, elements)
                self.qt_to_rawImage(tree.get_lower_left(), pixels, elements)
                self.qt_to_rawImage(tree.get_lower_right(), pixels, elements)

        return tree, elements

    def preorder(self, tree):
        """
        A function to do preorder traversal of a tree.

        @param tree The tree to traverse.
        """
        
        newlist = self.root.preorder(tree)
        return newlist













