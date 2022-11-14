from PyQt5 import QtCore, QtGui, QtWidgets
from branch import *
from utils import *
from utils_b import solve

class Ui(object):

    def __init__(self, window):
        # circuit branches
        self.circuit_branches = []

        # Branch sequence tracking
        self.sequence = 0

        window.setObjectName("mainWindow")
        window.resize(707, 562)
        self.central_widget = QtWidgets.QWidget(window)
        self.central_widget.setObjectName("central_widget")

        # Labels
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        self.message_label = QtWidgets.QLabel(self.central_widget)
        self.message_label.setGeometry(QtCore.QRect(10, 10, 201, 20))
        self.message_label.setFont(font)
        self.message_label.setObjectName("message_label")

        self.starting_node_label = QtWidgets.QLabel(self.central_widget)
        self.starting_node_label.setGeometry(QtCore.QRect(10, 50, 141, 20))
        self.starting_node_label.setFont(font)
        self.starting_node_label.setObjectName("starting_node_label")

        self.ending_node_label = QtWidgets.QLabel(self.central_widget)
        self.ending_node_label.setGeometry(QtCore.QRect(10, 110, 141, 20))
        self.ending_node_label.setFont(font)
        self.ending_node_label.setObjectName("ending_node_label")

        self.voltage_source_label = QtWidgets.QLabel(self.central_widget)
        self.voltage_source_label.setGeometry(QtCore.QRect(10, 170, 141, 20))
        self.voltage_source_label.setFont(font)
        self.voltage_source_label.setObjectName("voltage_source_label")

        self.current_source_label = QtWidgets.QLabel(self.central_widget)
        self.current_source_label.setGeometry(QtCore.QRect(10, 230, 141, 20))
        self.current_source_label.setFont(font)
        self.current_source_label.setObjectName("current_source_label")

        self.resistance_label = QtWidgets.QLabel(self.central_widget)
        self.resistance_label.setGeometry(QtCore.QRect(10, 290, 141, 20))
        self.resistance_label.setFont(font)
        self.resistance_label.setObjectName("resistance_label")

        self.jb_label = QtWidgets.QLabel(self.central_widget)
        self.jb_label.setGeometry(QtCore.QRect(40, 370, 1000, 150))
        self.jb_label.setFont(font)
        self.jb_label.setObjectName("jb_label")

        self.vb_label = QtWidgets.QLabel(self.central_widget)
        self.vb_label.setGeometry(QtCore.QRect(40, 420, 1000, 150))
        self.vb_label.setFont(font)
        self.vb_label.setObjectName("vb_label")

        # Text boxes

        self.text_boxes = []

        self.starting_node_text_box = QtWidgets.QTextEdit(self.central_widget)
        self.starting_node_text_box.setGeometry(QtCore.QRect(130, 40, 81, 41))
        self.starting_node_text_box.setObjectName("starting_node_text_box")
        self.starting_node_text_box.setFont(font)
        self.text_boxes.append(self.starting_node_text_box)

        self.ending_node_text_box = QtWidgets.QTextEdit(self.central_widget)
        self.ending_node_text_box.setGeometry(QtCore.QRect(130, 100, 81, 41))
        self.ending_node_text_box.setObjectName("ending_node_text_box")
        self.ending_node_text_box.setFont(font)
        self.text_boxes.append(self.ending_node_text_box)

        self.voltage_source_text_box = QtWidgets.QTextEdit(self.central_widget)
        self.voltage_source_text_box.setGeometry(QtCore.QRect(130, 160, 81, 41))
        self.voltage_source_text_box.setObjectName("voltage_source_text_box")
        self.voltage_source_text_box.setFont(font)
        self.text_boxes.append(self.voltage_source_text_box)

        self.current_source_text_box = QtWidgets.QTextEdit(self.central_widget)
        self.current_source_text_box.setGeometry(QtCore.QRect(130, 220, 81, 41))
        self.current_source_text_box.setObjectName("current_source_text_box")
        self.current_source_text_box.setFont(font)
        self.text_boxes.append(self.current_source_text_box)

        self.resistance_text_box = QtWidgets.QTextEdit(self.central_widget)
        self.resistance_text_box.setGeometry(QtCore.QRect(130, 280, 81, 41))
        self.resistance_text_box.setObjectName("resistance_text_box")
        self.resistance_text_box.setFont(font)
        self.text_boxes.append(self.resistance_text_box)

        # Buttons

        self.run_button = QtWidgets.QPushButton(self.central_widget)
        self.run_button.setGeometry(QtCore.QRect(500, 350, 91, 31))
        self.run_button.setObjectName("run_button")
        self.run_button.clicked.connect(self.run_clicked)

        self.next_button = QtWidgets.QPushButton(self.central_widget)
        self.next_button.setGeometry(QtCore.QRect(60, 350, 91, 31))
        self.next_button.setObjectName("next_button")
        self.next_button.clicked.connect(self.next_clicked)

        # Extras

        window.setCentralWidget(self.central_widget)
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 21))
        self.menubar.setObjectName("menubar")
        window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)

        self.re_translate_ui(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def re_translate_ui(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("mainWindow", "Electrical Circuit Analysis"))
        self.message_label.setText(_translate("mainWindow", "Enter branch " + chr(65 + self.sequence) + " details:"))
        self.starting_node_label.setText(_translate("mainWindow", "Starting Node"))
        self.ending_node_label.setText(_translate("mainWindow", "Ending Node"))
        self.voltage_source_label.setText(_translate("mainWindow", "Voltage Source"))
        self.current_source_label.setText(_translate("mainWindow", "Current Source"))
        self.resistance_label.setText(_translate("mainWindow", "Resistance"))
        self.next_button.setText(_translate("mainWindow", "Add Branch"))
        self.run_button.setText(_translate("mainWindow", "Run"))
        self.jb_label.setText(_translate("mainWindow", "Jb = "))
        self.vb_label.setText(_translate("mainWindow", "Vb = "))

    def next_clicked(self):
        # Validation check
        # if value is not digit, set it as 0
        for text_box in self.text_boxes:
            text_box.setText(text_box.toPlainText().strip())
            if not text_box.toPlainText().isdigit():
                text_box.setText('0')

        # Create a branch
        new_branch = Branch(self.sequence,
                            self.starting_node_text_box.toPlainText(),
                            self.ending_node_text_box.toPlainText(),
                            self.voltage_source_text_box.toPlainText(),
                            self.current_source_text_box.toPlainText(),
                            self.resistance_text_box.toPlainText())

        # Add new branch to branches list
        self.circuit_branches.append(new_branch)

        for text_box in self.text_boxes:
            text_box.clear()
        self.sequence += 1
        self.message_label.setText("Enter branch  " + chr(65 + self.sequence) + " details:")

    def run_clicked(self):
        tree_branches, links = tree(self.circuit_branches)
        for branch in tree_branches:
            print(branch)
        print('0000000000000000000-------------------0000000000000000')
        for branch in links:
            print(branch)

        # Calculate V_b, J_b
        v_b, j_b = solve(self.circuit_branches)
        # generate graph for tree/co-tree
        
        #Call generating graph function.
        generate_graph (tree_branches=tree_branches, links=links, vb=v_b, jb=j_b)

        
        self.vb_label.setText("V_B: " + str(v_b))
        self.jb_label.setText("J_B: " + str(j_b))

