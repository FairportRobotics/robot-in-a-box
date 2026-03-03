import commands2

class HopperSubsystem(commands2.Subsystem):
    def __init__(self, motor) -> None:
        super().__init__()
        # Initialize your hopper subsystem here
        self.motor = motor

    def periodic(self) -> None:
        """This method is called once per scheduler run."""
        # You can put background tasks here, like updating SmartDashboard values
        pass

    def set_speed(self, speed) -> None:
        # Set the speed of the hopper motor
        self.motor.set(speed)

    def stop(self) -> None:
        # Stop the hopper motor
        self.motor.set(0)




    