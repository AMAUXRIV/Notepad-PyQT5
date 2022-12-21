from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

# membuat class menudemo
class MenuDemo(QMainWindow):
    # membuat fungsi __init__
    def __init__(self):    
        # memanggil fungsi __init__ dari class QMainWindow
        super(MenuDemo, self).__init__()

        # membuat menu bar
        layout = QHBoxLayout()
        bar = self.menuBar()
        # membuat menu file
        file = bar.addMenu("File")
        # membuat item new dengan shortcut ctrl+n
        new = QAction("New", self)
        new.setShortcut("Ctrl+N")
        file.addAction(new)

        # membuat item new window dengan shortcut ctrl+shift+n
        newwin = QAction("New Window", self)
        newwin.setShortcut("Ctrl+Shift+N")
        file.addAction(newwin)

        # membuat item open dengan shortcut ctrl+o
        open = QAction("Open", self)
        open.setShortcut("Ctrl+O")
        file.addAction(open)
        # membuat item save
        save = QAction("Save", self)
        # membuat shortcut ctrl+s
        save.setShortcut("Ctrl+S")
        file.addAction(save)
        # membuat item save as
        saveas = QAction("Save As", self)
        # membuat shortcut ctrl+shift+s
        saveas.setShortcut("Ctrl+Shift+S")
        file.addAction(saveas)
        # membuat item page setup
        file.addAction("Page Setup")
        # membuat item print
        file.addAction("Print")
        # membuat item exit
        exit = QAction("Exit", self)





        # membuat menu edit
        edit = bar.addMenu("Edit")
        # membuat item undo dengan shortcut ctrl+z
        undo = QAction("Undo", self)
        undo.setShortcut("Ctrl+Z")
        edit.addAction(undo)
        # membuat item cut dengan shortcut ctrl+x
        cut = QAction("Cut", self)
        cut.setShortcut("Ctrl+X")
        edit.addAction(cut)
        # membuat item copy dengan shortcut ctrl+c
        copy = QAction("Copy", self)
        copy.setShortcut("Ctrl+C")
        edit.addAction(copy)
        # membuat item paste dengan shortcut ctrl+v
        paste = QAction("Paste", self)
        paste.setShortcut("Ctrl+V")
        edit.addAction(paste)
        # membuat item delete dengan shortcut del
        delete = QAction("Delete", self)
        delete.setShortcut("Del")
        edit.addAction(delete)
        # membuat item search with bing dengan shortcut ctrl+e
        search = QAction("Search with Bing", self)
        search.setShortcut("Ctrl+E")
        edit.addAction(search)
        # membuat item find dengan shortcut ctrl+f
        find = QAction("Find", self)
        find.setShortcut("Ctrl+F")
        edit.addAction(find)
        # membuat item find next dengan shortcut f3
        findnext = QAction("Find Next", self)
        findnext.setShortcut("F3")
        edit.addAction(findnext)
        # membuat item find previous dengan shortcut shift+f3
        findprevious = QAction("Find Previous", self)
        findprevious.setShortcut("Shift+F3")
        edit.addAction(findprevious)
        # membuat item replace dengan shortcut ctrl+h
        replace = QAction("Replace", self)
        replace.setShortcut("Ctrl+H")
        edit.addAction(replace)
        # membuat item go to dengan shortcut ctrl+g
        goto = QAction("Go To", self)
        goto.setShortcut("Ctrl+G")
        edit.addAction(goto)
        # membuat item select all dengan shortcut ctrl+a
        selectall = QAction("Select All", self)
        selectall.setShortcut("Ctrl+A")
        edit.addAction(selectall)
        # membuat item time/date dengan shortcut f5
        timedate = QAction("Time/Date", self)
        timedate.setShortcut("F5")
        edit.addAction(timedate)

        # membuat menu format
        format = bar.addMenu("Format")
        # membuat item word wrap checkbox
        wordwrap = QAction("Word Wrap", self)
        wordwrap.setCheckable(True)
        format.addAction(wordwrap)

        # membuat item font dengan menyanmbungkan fungsi font
        font = QAction("Font", self)
        format.addAction(font)
        font.triggered.connect(self.select_font)

        #membuat windows baru
        br= QAction("Kalkulator",self)
        format.addAction(br)
        self.bangun = bangunruang()
        br.triggered.connect(self.bangun.show)
        

        

        # membuat menu view
        view = bar.addMenu("View")
        # membuat item zoom dengan sub item zoom in dan zoom out , restore default zoom
        zoom = view.addMenu("Zoom")
        zoom.addAction("Zoom In")
        zoom.addAction("Zoom Out")
        zoom.addAction("Restore Default Zoom")
        # membuat item status bar dengan checkbox
        statusbar = QAction("Status Bar", self)
        statusbar.setCheckable(True)
        statusbar.setChecked(True)
        view.addAction(statusbar)
        
        # membuat menu help
        help = bar.addMenu("Help")
        # membuat item view help
        help.addAction("View Help")
        # membuat item send feedback
        help.addAction("Send Feedback")
        # membuat item about notepad
        help.addAction("About Notepad")

        # membuat quit action
        quit = QAction("Quit", self)
        file.addAction(quit)
        file.triggered[QAction].connect(self.processtrigger)

        self.setLayout(layout)
        self.setWindowTitle("AMAUX REAV")

        # menambahkan QtextEdit
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        
        



    # membuat fungsi untuk menampilkan quit
    def processtrigger(self, q):
        if q.text() == "Quit":
            # membuat pesan konfirmasi
            pesan = QMessageBox.question(self, "Konfirmasi", "Apakah anda yakin ingin keluar?", QMessageBox.Yes | QMessageBox.No)
            # jika pesan yes
            if pesan == QMessageBox.Yes:
                # menghentikan aplikasi
                qApp.quit()

    def select_font(self):
        # Show a font selection dialog and apply the selected font to the text edit
        font, ok = QFontDialog.getFont()
        if ok:
            self.text_edit.setFont(font)

class bangunruang (QWidget) :
    def __init__(self):
        super(bangunruang,self).__init__()
        self.setupUi()
    
    def setupUi(self):
        self.resize(400, 200)
        self.move(400, 300)
        self.setWindowTitle('Form Luas Volume')
        self.setStyleSheet('background-color:#006884')
        
        self.label1 = QLabel()
        self.label1.setText('Jari Jari')
        self.label1.setStyleSheet('color:white;') 
        self.numberEdit1 = QLineEdit()
        self.numberEdit1.setStyleSheet('QLineEdit{background-color:#00909E;color:white;}') 
        self.numberEdit1.setValidator(QDoubleValidator(0.99,99.99,2))
        
        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.label1)
        vbox1.addWidget(self.numberEdit1)
        
        self.label2 = QLabel()
        self.label2.setText('Tinggi')
        self.label2.setStyleSheet('color:white;') 
        self.numberEdit2 = QLineEdit()
        self.numberEdit2.setStyleSheet('QLineEdit{background-color:#00909E;color:white;}') 
        self.numberEdit2.setValidator(QDoubleValidator(0.99,99.99,2))
        
        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.label2)
        vbox2.addWidget(self.numberEdit2)

            #Radioedit
        
        self.radioedit=QRadioButton("Luas")
        self.radioedit.setStyleSheet('color:white;') 
        
        self.radioedit2=QRadioButton("Volume")
        self.radioedit2.setStyleSheet('color:white;') 
        
        vboxrad= QHBoxLayout()
        vboxrad.addWidget(self.radioedit)
        vboxrad.addWidget(self.radioedit2)

       

        
    

        self.label3 = QLabel()
        self.label3.setText('Hasil        :')
        self.label3.setStyleSheet('color:white;') 
        self.resultEdit = QLineEdit()
        self.resultEdit.setStyleSheet('QLineEdit{color:white;}')
        self.resultEdit.setReadOnly(True)
        
        vbox3 = QHBoxLayout()
        vbox3.addWidget(self.label3)
        vbox3.addWidget(self.resultEdit)

        vbox4 = QVBoxLayout()
        vbox4.addLayout(vbox1)
        vbox4.addLayout(vbox2)
        vbox4.addLayout(vboxrad)
        vbox4.addLayout(vbox3)
        vbox4.addStretch()

        
        self.print = QPushButton('Print')
        self.print.setStyleSheet('QPushButton{color:white;}') 
        vbox5 = QVBoxLayout()

        self.label = QLabel()
        self.label.setText('Maulana Rizki Pratama\n          21010026\n\n')
        self.label.setStyleSheet('color:white;') 
        vbox5.addWidget(self.label)
        vbox5.addStretch()
        vbox5.addWidget(self.print)
        vbox5.addStretch()
        
        layout  = QHBoxLayout()
        layout.addLayout(vbox4)
        verticalLine = QFrame();
        verticalLine.setFrameShape(QFrame.VLine)
        verticalLine.setFrameShadow(QFrame.Sunken)
        layout.addWidget(verticalLine)
        layout.addLayout(vbox5)
        self.setLayout(layout)
        
        self.print.clicked.connect(self.btnstate)
        
        
    def calculate(self,operator):
        a = float(self.numberEdit1.text())
        b = float(self.numberEdit2.text())
        if operator == 'ok':
            c = 2*3.14*a*(a+b)
            self.resultEdit.setText(str(c))
        elif operator == 'okk':
            c = 3.14*a*a*b
            self.resultEdit.setText(str(c))

    def btnstate(self):
        if self.radioedit.isChecked():
            self.calculate('ok')
        elif self.radioedit2.isChecked:
            self.calculate('okk')



    
         

# membuat fungsi main
def main():
    # membuat objek app
    app = QApplication([])
    # membuat objek form
    form = MenuDemo()
    # menampilkan form
    form.show()
    # menghentikan aplikasi
    app.exec_()
# menjalankan fungsi main
if __name__ == '__main__':
    main()
