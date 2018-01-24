#####################
# views\View.py #
#####################
from PyQt4 import QtGui
from gen.Second import Ui_Second 

class Second(QtGui.QMainWindow):

    #### properties for widget value ####

    #### properties for widget enabled state ####

    def __init__(self, model, main_ctrl):
        self.model = model
        self.main_ctrl = main_ctrl
        super(Second, self).__init__()
        self.build_ui()
        # register func with model for model update announcements
        self.model.subscribe_update_func(self.update_ui_from_model)

    def build_ui(self):
        self.ui = Ui_Second()
        self.ui.setupUi(self)

        #### set Qt model for compatible widget types ####

        #### connect widget signals to event functions ####

    def update_ui_from_model(self):
        print 'DEBUG: update_ui_from_model called'
        #### update widget values from model ####

    #### widget signal event functions ####


###########################
# controllers\Controller.py #
###########################
from PyQt4 import QtGui

class SecondController(object):

    def __init__(self, model):
        self.model = model

    #### widget event functions ####


##################
# model\Model.py #
##################
from PyQt4 import QtGui

class Model(object):

    #### properties for value of Qt model contents ####

    def __init__(self):
        self._update_funcs = []
        self.config_section = 'settings'
        self.config_options = (
        )

        #### create Qt models for compatible widget types ####

        #### model variables ####

    def subscribe_update_func(self, func):
        if func not in self._update_funcs:
            self._update_funcs.append(func)

    def unsubscribe_update_func(self, func):
        if func in self._update_funcs:
            self._update_funcs.remove(func)

    def announce_update(self):
        for func in self._update_funcs:
            func()


##########
# App.py #
##########
import sys
from PyQt4 import QtGui
from model.Model import SecondModel
from controllers.SecondController import SecondController
from views.SecondView import SecondView

class App(QtGui.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = SecondModel()
        self.main_ctrl = SecondController(self.model)
        self.main_view = SecondView(self.model, self.main_ctrl)
        self.main_view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())


