import wpilib 
import phoenix5

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.motor = phoenix5.WPI_TalonSRX(17)
        self.controller = wpilib.XboxController(0)

    def teleopPeriodic(self):
        speed = self.controller.getLeftY()
        self.motor.set(speed)
    