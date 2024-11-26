import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from iterator import MyIterator
from PyQt5.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self)->None:
        """
        make window and layout grid
        """
        super().__init__()
        self.setWindowTitle("Image Viewer")
        self.setGeometry(500, 300, 600, 400)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.main_text = QLabel("Images", self)
        self.main_text.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.main_text)

        self.image_label = QLabel(self)
        self.image_label.setFixedSize(650, 300)
        self.image_label.setScaledContents(True)
        layout.addWidget(self.image_label)

        button_layout = QHBoxLayout()
        self.btn_open = QtWidgets.QPushButton("Select Folder", self)
        self.btn_open.clicked.connect(self.open_folder_dialog)
        button_layout.addWidget(self.btn_open)

        self.btn_right = QtWidgets.QPushButton("->", self)
        self.btn_right.clicked.connect(self.show_next_image)
        button_layout.addWidget(self.btn_right)

        layout.addLayout(button_layout)

        self.err_text = QLabel("", self)
        self.err_text.setStyleSheet("color: red;")
        self.err_text.hide()
        layout.addWidget(self.err_text)

        self.image_iterator = None
        self.current_image = None


    def open_folder_dialog(self)->None:
        """
        get name folder from file dialog
        :return: None
        """
        folder_name = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_name:
            self.image_iterator = MyIterator(folder_name)
            self.current_image = next(self.image_iterator)
            if self.current_image:
                self.display_image(self.current_image)
                self.err_text.hide()
            else:
                self.err_text.setText("No images found in the selected folder.")
                self.err_text.show()


    def display_image(self, image_path)->None:
        """
        show pictures
        :param image_path: image path
        :return:None
        """
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(self.image_label.size(), aspectRatioMode=1)
        self.image_label.setPixmap(scaled_pixmap)


    def show_next_image(self)->None:
        """
        display next image in main window
        :return: None
        """
        if self.image_iterator:
            try:
                self.current_image = next(self.image_iterator)
                self.display_image(self.current_image)
            except StopIteration:
                self.err_text.setText("No more images.")
                self.err_text.show()


def application()->None:
    """
    make window
    :return: None
    """
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
