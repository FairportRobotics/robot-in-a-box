import wpilib
import phoenix5
from subsystems.hopper import HopperSubsystem

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        #self.motor = phoenix5.WPI_TalonSRX(17)
        self.hopper = HopperSubsystem(phoenix5.WPI_TalonSRX(17))
        

    def teleopPeriodic(self):
        #self.motor.set(0.5)
        pass
