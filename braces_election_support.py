from PyQt5.QtWidgets import QTabWidget, QLabel, QVBoxLayout, QWidget, QTextEdit
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor
from qgis.gui import QgsMapToolIdentify
from qgis.utils import iface
import os
import webbrowser
import winsound
from . import playsound


class SelectTool(QgsMapToolIdentify):
    def __init__(self, canvas):
        QgsMapToolIdentify.__init__(self, canvas)
        #self.canvas = canvas
        self.setCursor(Qt.ArrowCursor)
    def canvasReleaseEvent(self, event): # mouse release
        l = iface.activeLayer()
        if l is None:
            return
        results = self.identify(event.x(), event.y(), [l], QgsMapToolIdentify.TopDownStopAtFirst)
        selected = [f.id() for f in l.selectedFeatures()]
        if len(results) > 0:
            for r in results:
                id = r.mFeature.id()
                if not id in selected:
                    selected.append(id)
                else:
                    selected.remove(id)
        else:
            selected = []
        l.selectByIds(selected)
        self.printFeatures(l)
    def printFeatures(self, layer):
        selection = layer.selectedFeatures()
        for f in selection:
            print(f.attributes())

class InfoTabs(QTabWidget):
    def __init__(self, parent=None):
        super(InfoTabs, self).__init__(parent)
        tab1 = QWidget()
        tab2 = QWidget()
        self.addTab(tab1, "Tallying")
        self.addTab(tab2, "State Info")
        #
        self.toolLabel = QLabel("State Information")
        layout1 = QVBoxLayout()
        layout1.addWidget(self.toolLabel)
        tab1.setLayout(layout1)
        #
        self.toolText = QTextEdit("<b>Voting Results</b>")
        layout2 = QVBoxLayout()
        layout2.addWidget(self.toolText)
        tab2.setLayout(layout2)
    def getToolLabel(self):
        return self.toolLabel
    def getToolText(self):
        return self.toolText
        
class SelectTool2(SelectTool):
    def __init__(self, canvas, labelwidget, textwidget, cursor=Qt.ArrowCursor):
        SelectTool.__init__(self, canvas)
        self.labelwidget = labelwidget
        self.textwidget = textwidget
        self.setCursor(cursor)
    def printFeatures(self, layer):
        selection = layer.selectedFeatures()     
        vote_num = 0
        winner = 'State: \n'
        results = ''
        for f in selection:
            vote_num += f.attributes()[1]
            winner += 'Mr. Squiggly Brace has won ' + str(f.attributes()[0]) + '\n' + str(f.attributes()[0]) + ' Electoral Votes: ' + str(f.attributes()[1]) + '\n' + '\n'
            results = 'Mr. Squiggly Braces Total Votes: ' + str(vote_num) + '\n'

        #play sound
        if vote_num >= 270:
            results += ' YOU WON!!!!!!!!!'

            mypath = os.path.dirname(__file__) + '\\victorysound.wav'
            playsound.playsound(mypath, False)

            #playsound alternatives
            #winsound.PlaySound('testsound.wav', winsound.SND_ASYNC)
            #webbrowser.open('https://youtu.be/9FLRHejWAo8')
            #os.system("start \"\" https://youtu.be/9FLRHejWAo8")

        #self.labelwidget.setTextColor(QColor('red'))    
        self.labelwidget.setText(results)
        self.textwidget.setTextColor(QColor('blue'))
        self.textwidget.setText(winner)

