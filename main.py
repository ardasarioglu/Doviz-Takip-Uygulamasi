import sys, os ,sqlite3, requests
from PyQt5.QtWidgets import QWidget, QTextEdit, QFileDialog,QApplication, QCheckBox, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QAction, qApp, QMainWindow
from bs4 import BeautifulSoup


class Doviz():
    def __init__(self):
        self.url="https://www.doviz.com/"
        self.baslik={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        response=requests.get(self.url, headers=self.baslik)
        self.html_icerigi=response.content
        self.soup=BeautifulSoup(self.html_icerigi, "html.parser")

        self.degerler = [["Gram Altın", ""], ["Dolar", ""], ["Euro", ""], ["Sterlin", ""], ["BIST100", ""], ["Bitcoin", ""], ["Gram Gümüş", ""], ["Brent", ""]]    
        sayac=0

        for i in self.soup.find_all("span", {"class": "value"}):
            self.degerler[sayac][1]=i.text
            sayac+=1
            
class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.doviz=Doviz()
        
        self.init_ui()
    
    def init_ui(self):
        self.textarea1=QLabel()
        self.textarea2=QLabel()
        self.textarea3=QLabel()
        self.textarea4=QLabel()
        self.textarea5=QLabel()
        self.textarea6=QLabel()
        self.textarea7=QLabel()
        self.textarea8=QLabel()

        v_box=QVBoxLayout()
        v_box.addWidget(self.textarea1)
        v_box.addWidget(self.textarea2)
        v_box.addWidget(self.textarea3)
        v_box.addWidget(self.textarea4)
        v_box.addWidget(self.textarea5)
        v_box.addWidget(self.textarea6)
        v_box.addWidget(self.textarea7)
        v_box.addWidget(self.textarea8)

        self.textarea1.setText(f"{self.doviz.degerler[0][0]}: {self.doviz.degerler[0][1]}")
        self.textarea2.setText(f"{self.doviz.degerler[1][0]}: {self.doviz.degerler[1][1]}")
        self.textarea3.setText(f"{self.doviz.degerler[2][0]}: {self.doviz.degerler[2][1]}")
        self.textarea4.setText(f"{self.doviz.degerler[3][0]}: {self.doviz.degerler[3][1]}")
        self.textarea5.setText(f"{self.doviz.degerler[4][0]}: {self.doviz.degerler[4][1]}")
        self.textarea6.setText(f"{self.doviz.degerler[5][0]}: {self.doviz.degerler[5][1]}")
        self.textarea7.setText(f"{self.doviz.degerler[6][0]}: {self.doviz.degerler[6][1]}")
        self.textarea8.setText(f"{self.doviz.degerler[7][0]}: {self.doviz.degerler[7][1]}")

        self.setLayout(v_box)

        self.setWindowTitle("Doviz")
        self.setGeometry(100,100,500,500,)
        self.show()
            

app=QApplication(sys.argv)
pencere=Pencere()
pencere.show()
sys.exit(app.exec_())