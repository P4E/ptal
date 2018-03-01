import sys
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, qApp, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSlider, QGridLayout, QFileDialog

class Accueil(QMainWindow):
    def __init__(self):
        super().__init__()
        self.afficherGUI()

    def afficherGUI(self):
        
        self.resize(1000, 300)
        self.setWindowTitle("Mirror")
        bar = self.menuBar()
        fileMenu = bar.addMenu("Fichier")
        parametersMenu = bar.addMenu("Paramètres")
        helpMenu = bar.addMenu("Aide")

        quit = QAction("Quitter", self)
        quit.setShortcut("Ctrl+Q")
        fileMenu.addAction(quit)
        quit.triggered.connect(qApp.exit)
        
        mode = QAction("Basculer entre le mode simple et avancé", self)
        mode.setShortcut("Ctrl+M")
        parametersMenu.addAction(mode)

        summary = QAction("Sommaire", self)
        summary.setShortcut("Ctrl+S")
        helpMenu.addAction(summary)

        about = QAction("À propos", self)
        about.setShortcut("Ctrl+A")
        helpMenu.addAction(about)
        
        # File selection
        label = QLabel("Fichier source")
        fileField = QLineEdit()
        openFileButton = QPushButton("…", self)
        openFileButton.clicked.connect(self.selectFile)
        #QObject.connect(openFileButton, SIGNAL("clicked()"), self.selectFile)
        hboxFile = QHBoxLayout()
        hboxFile.addWidget(label)
        hboxFile.addWidget(fileField)
        hboxFile.addWidget(openFileButton)

        # Sentence source
        label = QLabel("Texte à paraphraser") # mettre éventuellement le label en « placeholder » du champ texte
        inputField = QTextEdit()
        hboxInput = QHBoxLayout()
        hboxInput.addWidget(label)
        hboxInput.addWidget(inputField)

        # Paramètres : similarité
        label = QLabel("Similarité de la paraphrase")
        slider = QSlider(Qt.Horizontal, self)
        hboxSimilarity = QHBoxLayout()
        hboxSimilarity.addWidget(label)
        hboxSimilarity.addWidget(slider)
        hboxSimilarity.addStretch(0)
        #hboxSimilarity.addSpacing(300)
        # Paramètres : personnalité
        opennessLabel = QLabel("Ouverture")
        opennessSlider = QSlider(Qt.Horizontal, self)
        conscientiousnessLabel = QLabel("Caractère consciencieux")
        conscientiousnessSlider = QSlider(Qt.Horizontal, self)
        extroversionLabel = QLabel("Extraversion")
        extroversionSlider = QSlider(Qt.Horizontal, self)
        agreeablenessLabel = QLabel("Agréabilité")
        agreeablenessSlider = QSlider(Qt.Horizontal, self)
        neuroticismLabel = QLabel("Névrosisme")
        neuroticismSlider = QSlider(Qt.Horizontal, self)

        grid = QGridLayout()
        grid.addWidget(opennessLabel, 1, 1)
        grid.addWidget(opennessSlider, 1, 2)
        grid.addWidget(conscientiousnessLabel, 1, 3)
        grid.addWidget(conscientiousnessSlider, 1, 4)
        grid.addWidget(extroversionLabel, 1, 5)
        grid.addWidget(extroversionSlider, 1, 6)
        grid.addWidget(agreeablenessLabel, 2, 1)
        grid.addWidget(agreeablenessSlider, 2, 2)
        grid.addWidget(neuroticismLabel, 2, 3)
        grid.addWidget(neuroticismSlider, 2, 4)
                
        #vboxParameters = QVBoxLayout()
        #vboxParameters.addWidget(similarityLabel)
        #vboxParameters.addWidget(similaritySlider)
        #vboxParameters.addWidget(opennessLabel)
        #vboxParameters.addWidget(opennessSlider)
        #vboxParameters.addWidget(conscientiousnessLabel)
        #vboxParameters.addWidget(conscientiousnessSlider)
        #vboxParameters.addWidget(extroversionLabel)
        #vboxParameters.addWidget(extroversionSlider)
        #vboxParameters.addWidget(agreeablenessLabel)
        #vboxParameters.addWidget(agreeablenessSlider)
        #vboxParameters.addWidget(neuroticismLabel)
        #vboxParameters.addWidget(neuroticismSlider)

        # Texte en sortie
        label = QLabel("Résultat")
        outputField = QTextEdit()
        outputField.setReadOnly(True)
        hboxOutput = QHBoxLayout()
        hboxOutput.addWidget(label)
        hboxOutput.addWidget(outputField)

        vbox = QVBoxLayout()
        vbox.addLayout(hboxFile)
        vbox.addLayout(hboxInput)
        vbox.addLayout(hboxSimilarity)
        vbox.addLayout(grid)
        vbox.addLayout(hboxOutput)

        normalMode = QWidget()
        normalMode.setLayout(vbox)
        self.setCentralWidget(normalMode)
        self.show()

    def selectFile(self):
        file = str(QFileDialog.getOpenFileName(self, "Sélectionner un fichier"))
        return file

appli = QApplication(sys.argv)
W = Accueil()
sys.exit(appli.exec_())
