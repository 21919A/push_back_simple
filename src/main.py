#!/usr/bin/env -S PYTHONPATH=../telemetry python3

from telemetry.config_log import *
from push_back.events import *

# Open log based on config
config_open_log()

calibrate_and_wait()


def driver_function():
    """Function for the driver part of a competition match"""

    log(("Competition", "competition"), "driver_begin")

    # Add driver logic here
    # Note that event handling is initialized outside of this function by init_event_handling()

    log(("Competition", "competition"), "driver_end")


def autonomous_function():
    """Function for the autonomous part of a competition match"""

    log(("Competition", "competition"), "autonomous_begin")

    robot_position.reset(Position(1200, 1200))
    reset_heading_to_aim(Position(1400, 1200), FORWARD)

    matchload.set(True)

    wait(1000, MSEC)

    flap.set(True)

    wait(1000, MSEC)

    conveyor.spin(FORWARD, FORWARD, FORWARD)

    trigger_mover.move(Position(1400, 1200), FORWARD)

    wait(6000, MSEC)
    conveyor.spin(STOP, STOP, STOP)
    flap.set(False)

    trigger_mover.move(Position(800, 1200), REVERSE)
    matchload.set(False)
    trigger_turner.turn(180, FRAME_HEADING_RELATIVE)

    conveyor.spin(FORWARD, REVERSE, FORWARD)





    log(("Competition", "competition"), "autonomous_end")


# Initialize event handling
init_event_handling()

# Register the competition functions
competition = Competition(driver_function, autonomous_function)
