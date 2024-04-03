
# This software and its documentation are created by Houssem-eddine Lahmer
# Feel free to use, modify, and distribute them for any purpose.



from GUI_Master import RootGUI, ComGui
from Serial_Com_ctrl import SerialCtrl
from Data_Com_ctrl import DataMaster
# Initiate the Root class that will manage the other classes
MySerial = SerialCtrl()
MyData = DataMaster()
RootMaster = RootGUI(MySerial, MyData)
# Initiate the Communication Master class that will manage all the other GUI classes
ComMaster = ComGui(RootMaster.root, MySerial, MyData)

# Start the Graphic User Interface
RootMaster.root.mainloop()
