import wpilib 
import phoenix5

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.motor = phoenix5.WPI_TalonSRX(17)

    def teleopPeriodic(self):
        self.motor.set(0.5)
        
class XboxController:
    port: int

    def execute(self):
        pass

    def setup(self):
        self.controller = wpilib.XboxController(self.port)

    def joysticks(self):
        return (
            self.controller.getLeftX(),
            self.controller.getLeftY(),
            self.controller.getRightX(),
            self.controller.getRightY(),
        )
    def x_pressed(self):
        return self.controller.getXButton()
    
    def y_pressed(self):
        return self.controller.getYButton()
