import wpilib 
import phoenix5

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.motor = phoenix5.WPI_TalonSRX(17)

    def teleopPeriodic(self):
        self.motor.set(0.5)