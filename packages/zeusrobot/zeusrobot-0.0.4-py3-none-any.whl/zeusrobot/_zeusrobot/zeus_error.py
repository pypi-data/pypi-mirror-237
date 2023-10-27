# Define Application Level Error Type
ERR_ZERO_IO = 20
ERR_ZERO_SHM = 21
ERR_ZERO_POSITION = 22
ERR_ZERO_JOINT = 23
ERR_ZERO_COORDINATE = 24
ERR_ZERO_MOTIONPARAM = 25
ERR_ZERO_ROBOT = 26
ERR_ZERO_ROBOT_CRITICAL = 27

# Base Class
class ZeusException(Exception):
    type = 0
    """
    Zeus Exception class

    Examples :
        try:
            ...
        except Exception as e:
            ZeusException(6,1,move,e)
            ZeusException(method=move, exc_msg=e)
    """
    def __init__(self, type=0, code=0, method="{method_name}", exc_msg = None):
        self.class_name = self.__class__.__name__  # TEST용
        self.type = type
        self.code = code
        self.method = method
        self.exc_msg = exc_msg
        if (self.type, self.code) == (0,0):
            super().__init__(f'\n{self.class_name}.{self.method} : {str(self.exc_msg)}')
        elif self.exc_msg:
            super().__init__(f'\n{self._errtype()}{str(self.type).zfill(2)}{str(self.code).zfill(2)} : {self.class_name}.{self.method} : {self._errmsg()} : {str(self.exc_msg)}')
        else:
            super().__init__(f'\n{self._errtype()}{str(self.type).zfill(2)}{str(self.code).zfill(2)} : {self.class_name}.{self.method} : {self._errmsg()}')

    def _errtype(self):
        if (self.type, self.code) in _errcode:
            return "A"
        elif (self.type, self.code) in _sys_errcode:
            if self.type == 10:
                return "E"
            elif self.type == 11:
                return "C"
        elif (self.type, self.code) in _app_errcode:
            return "A"

    def _errmsg(self):
        if (self.type, self.code) in _errcode:
            return _errcode[(self.type, self.code)]
        elif (self.type, self.code) in _sys_errcode:
            return _sys_errcode[(self.type, self.code)]
        elif (self.type, self.code) in _app_errcode:
            return _app_errcode[(self.type, self.code)]


class ZeusRobotCriticalException(ZeusException):
    class_name = '_ZeusRobotCritical'
    type = ERR_ZERO_ROBOT_CRITICAL

class ZeusRobotException(ZeusException):
    class_name = '_ZeusRobot'
    type = ERR_ZERO_ROBOT


class ZeusIOException(ZeusException):
    class_name = '_ZeusIO'
    type = ERR_ZERO_IO


class ZeusSharedMemoryException(ZeusException):
    class_name = '_ZeusSharedMemory'
    type = ERR_ZERO_SHM


class ZeusPositionException(ZeusException):
    class_name = '_ZeusPosition'
    type = ERR_ZERO_POSITION


class ZeusJointException(ZeusException):
    class_name = '_ZeusJoint'
    type = ERR_ZERO_JOINT


class ZeusCoordinateException(ZeusException):
    class_name = '_ZeusCoordinate'
    type = ERR_ZERO_COORDINATE


class ZeusMotionParamException(ZeusException):
    class_name = '_ZeusMotionParam'
    type = ERR_ZERO_MOTIONPARAM

# (1,x), (2,x) : Python Level Error
# (3,x) : Robot Control System Error
# (4,x) : Robot Control System Error
# (5,x) : Robot Control System Error
# (20~,x) : API Level Error
# (10,x) : System Normal Error (E00~E99)
# (11,x) : System Critical Error (C00~C99)


_errcode = {(1, 1): "Unable to allocate memory.",
            (1, 2): "Invalid descriptor",
            (2, 1): "Unable to connect to external device.",
            (2, 2): "Invalid command (CMD) key",
            (2, 3): "Invalid code data type",
            (2, 4): "Program is out of range.",
            (2, 5): "Invalid parameter key",
            (2, 6): "Invalid parameter data type",
            (2, 7): "Invalid data format",
            (2, 8): "Invalid parameter array type",
            (3, 0): "No error",
            (3, 1): "Robot operation not permitted.",
            (3, 2): "Parameter out of range.",
            (3, 3): "Invalid parameters",
            (3, 4): "Unable to change parameters.",
            (3, 10): "Robot motion planning error",
            (3, 11): "Position is outside of robot joint's moving ranges.",
            (3, 12): "Unreachable point error",
            (3, 13): "Exceeded robot joint's moving ranges during operations.",
            (3, 14): "Exceeded robot joint's maximum speed.",
            (3, 15): "Emergency Stop",
            (3, 16): "Paused",
            (3, 17): "Command (CMD) error occurred during operation.",
            (3, 18): "unable to obtain authorization for robot operation.",
            (3, 19): "CommandList buffer overflow",
            (3, 20): "Unable to save parameter.",
            (3, 21): "Unable to stop within specified time.",
            (3, 22): "Unable to calculate pulse offset",
            (3, 23): "Number of motion CMD overflow",
            (3, 24): "No force sensor",
            (3, 25): "No response from force sensor",
            (3, 26): "Frame error 1 with force sensor",
            (3, 27): "Frame error 2 with force sensor",
            (3, 28): "Invalid data from force sensor",
            (3, 29): "Unknown status of force sensor",
            (3, 30): "Invalid gain of force sensor",
            (3, 31): "Joint buffer is full",
            (3, 32): "Unable to access shared memory",
            (3, 33): "Unable to map shared memory",
            (3, 34): "(Reserved)",
            (3, 35): "User home position is not defined.",
            (3, 36): "(Reserved)",
            (3, 37): "Motion command exceeded speed limit.",
            (3, 99): "Robot control system error",
            (4, 1): "Invalid data type",
            (4, 2): "Parameter out of range",
            (4, 3): "Invalid parameter key",
            (4, 4): "Invalid parent object",
            (4, 5): "Exceeded the operable range.",
            (4, 6): "Communication error with the robot manipulator.",
            (4, 7): "Unable to initialize the robot.",
            (4, 8): "File not found.",
            (4, 9): "Unable to execute a robot program in Teaching mode.",
            (4, 10): "Robot operation not permitted.",
            (4, 11): "Index out of range",
            (4, 12): "Key not found.",
            (4, 13): "Unable to access shared memory",
            (4, 14): "Too many argument",
            (4, 15): "Data length is too much",
            (4, 16): "Invalid points at Area_Box, same position.",
            (4, 17): "(ForceSensor) Unable to set zeus offset",
            (4, 18): "(ForceSensor) Unable to read data",
            (4, 19): "Communication error",
            (4, 20): "Invalid Points at Area_Box, determinant equals 0",
            (4, 21): "Unable to start user program in error state",
            (4, 22): "Unable to start user program in invalid mode",
            (4, 23): "Unable to register to System manager",
            (4, 24): "sleep api must be called in main thread",
            (4, 25): "hook api must be called in main thread",
            (4, 26): "Teachdata is already opened.",
            (4, 27): "Unable to open during Teach mode.",
            (4, 28): "teach_data is too old! Please convert it.",
            (4, 29): "unsupported teachdata version!",
            (4, 30): "teach_data is not opened.",
            (4, 31): "teach_data is not opened with R/W.",
            (4, 32): "Invalid file name.",
            (4, 33): "teach_data is already opened by another process.",
            (4, 34): "Upgrade is not needed.",
            (4, 35): "Invalid teach_data format",
            (4, 36): "Unable to open file",
            (4, 37): "Unable to R/W open file",
            (4, 38): "Unable to use RobSys class with i611Robot class",
            (4, 98): "Unprocessed error",
            (4, 99): "Unprocessed error",
            (5, 1): "Emergency stop",
            (5, 2): "Stopped by the terminate instruction.",
            (5, 3): "Error in the robot control program.",
            (5, 4): "Error in the system program.",
            (5, 5): "ABS lost",
            (5, 6): "Timeout in emergency stop process",
            (5, 7): "Stopped by force sensor detection.",
            (5, 99):"Unprocessed error"}

_sys_errcode = {(10, 1): '"init.py" not found.',
               (10, 2): 'Error in "init.py"',
               (10, 3): "Unable to execute the robot program.",
               (10, 4): "No robot program was set.",
               (10, 5): "Robot program was in an unexecutable mode.",
               (10, 6): "Robot motion API was called before the i611Robot class's open ( ) was called.",
               (10, 7): "Robot program was executed while the ABS lost.",
               (10, 8): "Robot program terminated abnormally.",
               (10, 9): "i611Robot class's open() was called while emergency stop.",
               (10, 10): "i611Robot class's open() was called while servo off.",
               (10, 11): "unable to obtain authorization for robot operation.",
               (10, 12): "Robot program failed to communicate with the system manager.",
               (10, 13): "Exception of emergency stop was not caught.",
               (10, 14): "Robot program's exit() terminated abnormally.",
               (10, 15): "Robot program terminated with an exception.",
               (10, 16): "Exception of deceleration stop was not caught.",
               (10, 17): "System's terminating process was not completed properly.",
               (10, 18): "Unable to access the memory I/O.",
               (10, 19): "i611Robot class's instance was made multiple times in a process.",
               (10, 20): "i611Robot class's open() was called multiple times in a process.",
               (10, 21): "Invalid call of API from another thread occurred.",
               (10, 22): "Invalid call of API while emergency stop.",
               (10, 23): "Invalid call of API while servo off.",
               (10, 24): "PC's Shared Memory was not updated. Please execute ZSP Program and open ZSP Server",
               (10, 40): "Teaching Program terminated abnormally.",
               (10, 50): "Force sensor API was called before the force sensor's open() was called.",
               (10, 51): "Exception of the force sensor event was not caught.",
               (10, 52): "Unable to access the force sensor's device.",
               (10, 53): "Used size under /home/i611usr exceeds limit",
               (10, 99): "Other error",
               (11, 1): "Unable to start the system manager.",
               (11, 2): "System manager terminated abnormally.",
               (11, 3): "System manager failed to communicate with the control.",
               (11, 4): "Error occurred during Jog mode.",
               (11, 5): "Control manager terminated abnormally.",
               (11, 6): "Not enough free space on storage.",
               (11, 10): "(Joint) Circuit error",
               (11, 11): "(Joint) Current over",
               (11, 12): "(Joint) Brake error",
               (11, 13): "(Joint) Torque over",
               (11, 14): "(Joint) Overload error for motor",
               (11, 15): "(Joint) Driving voltage decreased",
               (11, 16): "(Joint) Power unit error",
               (11, 17): "(Joint) Servo motor error",
               (11, 18): "(Joint) Error occurred at servo motor On check 1",
               (11, 19): "(Joint) Error occurred at servo motor On check 2",
               (11, 20): "(Joint) ABS  lost: Over speed error during power shut-off",
               (11, 21): "(Joint) ABS  lost: ABS's home position was not saved",
               (11, 22): "(Joint) ABS  lost: Encoder detection error",
               (11, 23): "(Joint) ABS  lost: Encoder detector error",
               (11, 24): "(Joint) ABS  lost: ABS lost occurred due to human factors.",
               (11, 25): "(Joint) Cannot change state",
               (11, 26): "Error occurred at the top I/O.",
               (11, 27): "Error occurred at the force sensor.",
               (11, 28): "Error occurred in the internal monitor process.",
               (11, 29): "Cooling fan stopped.",
               (11, 30): "Regenerative resistor error 1 occurred.",
               (11, 31): "Main circuit relay breakdown.",
               (11, 32): 'Wiring error in "emergency stop circuit"',
               (11, 33): 'Wiring error in "mode circuit"',
               (11, 34): "Control power supply error",
               (11, 35): "The rush prevent resistor occurred a heat error",
               (11, 36): "Regenerative resistor error 2",
               (11, 37): "Regenerative resistor error 3",
               (11, 38): "Safety circuit error",
               (11, 39): "Ethercat communication lost",
               (11, 40): 'Duplication signal inconsistency in the "door circuit."',
               (11, 41): 'Duplication signal inconsistency in the "mode circuit."',
               (11, 42): "Slave state unmatch error",
               (11, 43): "Communication error occurred for interrupt.",
               (11, 44): "Slave error occurred in over speed.",
               (11, 47): "Positioning error",
               (11, 48): "ArmI/O power error",
               (11, 58): "SPI circuit error",
               (11, 59): "Robot system file corrupted.",
               (11, 60): "Task error",
               (11, 61): "(Joint) Parameter error",
               (11, 89): "Ethercat communication error",
               (11, 90): "Motion error",
               (11, 91): "(Joint) Motion limit error",
               (11, 92): "(Joint) Parameter error",
               (11, 93): "ENC error",
               (11, 94): "Board error",
               (11, 95): "Ethercat Sync0-PDI error",
               (11, 96): "Ethercat Sync0-PWM error",
               (11, 98): "Unexpected power shutdown.",
               (11, 99): "Other types of error"}

_app_errcode = {(20, 1): 'Invalid Parameter',
                (20, 2): 'Failed to open IO',
                (20, 3): 'Failed to close IO',
                (20, 4): 'IO wait Error',
                (20, 5): 'Digital Output Error',
                (20, 6): 'Digital Input Error',
                (20, 7): 'Delay Out Error',
                (20, 99): 'Unkown Error',

                (21, 1): 'Invalid Parameter',
                (21, 2): 'Invalid Address',
                (21, 3): 'Failed to open SharedMemory',
                (21, 4): 'Failed to close SharedMemory',
                (21, 5): 'Socket failed to read shared memory',
                (21, 6): 'Socket failed to write shared memory',
                (21, 7): 'Socket failed to write shared memory (system area)',
                (21, 99): 'Unkown Error',

                (22, 1): 'Invalid Parameter',
                (22, 2): 'Failed to transform Position data to list',
                (22, 99): 'Unkown Error',

                (23, 1): 'Invalid Parameter',
                (23, 2): 'Failed to transform Joint data to list',
                (23, 99): 'Unkown Error',

                (24, 1): 'Invalid Parameter',
                (24, 2): 'Parent is not a type of _BASE or _ParentContainer',
                (24, 3): 'Failed to transform world coordinate to base coordinate',
                (24, 4): 'Failed to transform base coordinate to world coordinate',
                (24, 5): 'Failed to get inverse matrix',
                (24, 6): 'Invalid Parameter',
                (24, 7): 'Invalid Parameter',
                (24, 8): 'Invalid Parameter',
                (24, 9): 'Invalid Parameter',
                (24, 10): 'Invalid Parameter',
                (24, 99): 'Unkown Error',

                (25, 1): 'Invalid Parameter',
                (25, 2): 'Failed to clear MotionParam',
                (25, 3): 'Faield to set MotionParam',
                (25, 99): 'Unkown Error',

                (26, 1): 'Invalid Parameter',
                (26, 2): 'Robot Controller is in Error state',
                (26, 3): 'Failed to open system control RobotClient',
                (26, 4): 'Failed to open RobotClient',
                (26, 5): 'Failed to close RobotClient',
                (26, 6): 'Failed to get MotionParam',
                (26, 7): 'Failed to clear MotionParam',
                (26, 8): 'Failed to move_arc : posture of two points must be given and same as current posture',
                (26, 9): 'Socket failed to connect RobotClient',
                (26, 10): 'Unable to open rblib',
                (26, 11): 'Socket failed to close RobotClient',
                (26, 12): 'ZSP system state is not ready yet',
                (26, 99): 'Unkown Error',
                }
