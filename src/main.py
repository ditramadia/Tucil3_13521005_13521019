# Import Modules
import Controller as ct

controller = ct.Controller()

controller.start()
while(controller.isRunning()):
    
    controller.readAlgorithm()
    
    if True:
        controller.stop()