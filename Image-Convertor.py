import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QLabel, QMessageBox
from PIL import Image

class ImageConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Converter')
        self.setGeometry(100, 100, 500, 275)
        self.setFixedSize(500, 275)
        self.setStyleSheet('background-color:#e2e2e2;')

        self.title_label = QLabel('Image Converter', self)
        self.title_label.setGeometry(10, 10, 500, 50)
        font = QFont('Arial', 18, QFont.Bold)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet('color: #2a8c2a; text-align: center;')

        self.input_path_label = QLabel('Select input file:', self)
        self.input_path_label.setGeometry(10, 70, 300, 30)
        font = QFont('Arial', 9)
        self.input_path_label.setFont(font)
        self.input_path_label.setStyleSheet('color: #2a2a2a;')

        self.input_path_button = QPushButton('Browse', self)
        self.input_path_button.setGeometry(360, 70, 100, 30)
        font = QFont('Arial', 9)
        self.input_path_button.setFont(font)
        self.input_path_button.setStyleSheet('color: white; background-color: #2a80ff; border-radius: 5px;')
        self.input_path_button.clicked.connect(self.selectInput)

        self.output_path_label = QLabel('Select output folder:', self)
        self.output_path_label.setGeometry(10, 110, 300, 30)
        font = QFont('Arial', 9)
        self.output_path_label.setFont(font)
        self.output_path_label.setStyleSheet('color: #2a2a2a;')

        self.output_path_button = QPushButton('Browse', self)
        self.output_path_button.setGeometry(360, 110, 100, 30)
        font = QFont('Arial', 9)
        self.output_path_button.setFont(font)
        self.output_path_button.setStyleSheet('color: white; background-color: #2a80ff; border-radius: 5px;')
        self.output_path_button.clicked.connect(self.selectOutput)

        self.convert_button = QPushButton('Convert', self)
        self.convert_button.setGeometry(200, 160, 100, 40)
        font = QFont('Arial', 12)
        self.convert_button.setFont(font)
        self.convert_button.setStyleSheet('color: white; background-color: #2a80ff; border-radius: 5px;')
        self.convert_button.clicked.connect(self.convertImages)

        self.info_label = QLabel('This program converts JPG and PNG images to WEBP format.', self)
        self.info_label.setGeometry(10, 210, 480, 30)
        font = QFont('Arial', 10)
        self.info_label.setFont(font)
        self.info_label.setStyleSheet('color: #050505;')
        self.info_label.setAlignment(Qt.AlignCenter)

        self.designed_by_label = QLabel('Programmed by Mahdi Ziraki', self)
        self.designed_by_label.setGeometry(10, 250, 200, 20)
        font = QFont('Arial', 9)
        self.designed_by_label.setFont(font)
        self.designed_by_label.setStyleSheet('color: #d40000;')
        self.designed_by_label.setAlignment(Qt.AlignLeft)

        self.show()

    def selectInput(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select input file', '', 'All Files (*);;JPG Files (*.jpg);;PNG Files (*.png)', options=QFileDialog.Options())
        if file_name:
            self.input_path = file_name
            self.input_path_label.setText('Input file: ' + self.input_path)

    def selectOutput(self):
        folder_name = QFileDialog.getExistingDirectory(self, 'Select output folder')
        if folder_name:
            self.output_path = folder_name
            self.output_path_label.setText('Output folder: ' + self.output_path)

    def convertImages(self):
        if os.path.isfile(self.input_path):
            if self.input_path.endswith(('.jpg', '.png')):
                image = Image.open(self.input_path)
                new_file_name = os.path.splitext(os.path.basename(self.input_path))[0] + '.webp'
                new_image_path = os.path.join(self.output_path, new_file_name)
                image.save(new_image_path, 'webp')
            else:
                self.showError('Invalid input file format. Please select a file with JPG or PNG format.')
        else:
            for filename in os.listdir(self.input_path):
                if filename.endswith(('.jpg', '.png')):
                    image_path = os.path.join(self.input_path, filename)
                    image = Image.open(image_path)
                    new_file_name = os.path.splitext(filename)[0] + '.webp'
                    new_image_path = os.path.join(self.output_path, new_file_name)
                    image.save(new_image_path, 'webp')

        # show completion message
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText('Image conversion completed successfully.')
        msgBox.setWindowTitle('Success')
        msgBox.exec_()

    def showError(self, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText(message)
        msgBox.setWindowTitle('Error')
        msgBox.exec_()

if __name__ == '__main__':
    app = QApplication([])
    converter = ImageConverter()
    app.aboutToQuit.connect(converter.closeEvent)
    app.exec_()
