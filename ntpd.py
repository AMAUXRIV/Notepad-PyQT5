# from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         menubar = self.menuBar()

#         # Membuat menu "Zoom"
#         zoomMenu = menubar.addMenu("Zoom")

#         # Membuat sub menu "In" di dalam menu "Zoom"
#         inMenu = QMenu("In", self)
#         zoomMenu.addMenu(inMenu)

#         # Membuat sub item "25%" di dalam sub menu "In"
#         in25Action = QAction("25%", self)
#         inMenu.addAction(in25Action)

#         # Membuat sub item "50%" di dalam sub menu "In"
#         in50Action = QAction("50%", self)
#         inMenu.addAction(in50Action)

#         # Membuat sub menu "Out" di dalam menu "Zoom"
#         outMenu = QMenu("Out", self)
#         zoomMenu.addMenu(outMenu)

#         # Membuat sub item "25%" di dalam sub menu "Out"
#         out25Action = QAction("25%", self)
#         outMenu.addAction(out25Action)

#         # Membuat sub item "50%" di dalam sub menu "Out"
#         out50Action = QAction("50%", self)
#         outMenu.addAction(out50Action)

#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle("Sub Item")
#         self.show()

# if __name__ == "__main__":
#     app = QApplication([])
#     window = MainWindow()
#     app.exec_()


from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

# membuat class menudemo
class MenuDemo(QMainWindow):
    # membuat fungsi __init__
    def __init__(self, parent=None):    # sourcery skip: avoid-builtin-shadow
        # memanggil fungsi __init__ dari class QMainWindow
        super(MenuDemo, self).__init__(parent)

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
        # membuat item font
        format.addAction("Font")

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
        self.text = QTextEdit(self)
        self.setCentralWidget(self.text)

        
        



    # membuat fungsi untuk menampilkan quit
    def processtrigger(self, q):
        if q.text() == "Quit":
            # membuat pesan konfirmasi
            pesan = QMessageBox.question(self, "Konfirmasi", "Apakah anda yakin ingin keluar?", QMessageBox.Yes | QMessageBox.No)
            # jika pesan yes
            if pesan == QMessageBox.Yes:
                # menghentikan aplikasi
                qApp.quit()
    
            

           

# membuat fungsi main
def main():
    # membuat objek app
    app = QApplication(sys.argv)
    # membuat objek form
    form = MenuDemo()
    # menampilkan form
    form.show()
    # menghentikan aplikasi
    app.exec_()
# menjalankan fungsi main
if __name__ == '__main__':
    main()









        