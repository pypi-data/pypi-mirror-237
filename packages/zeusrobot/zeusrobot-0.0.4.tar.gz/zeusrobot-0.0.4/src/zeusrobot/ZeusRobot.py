""" Zeus Robot API for Python"""

from ._zeusrobot import zeus_io, zeus_common, zeus_rblib
from ._zeusrobot.zeus_error import ZeusRobotException, ZeusIOException, ZeusSharedMemoryException, \
ZeusPositionException, ZeusJointException, ZeusCoordinateException, ZeusMotionParamException, ZeusRobotCriticalException

# # for module check
# from _zeusrobot import zeus_io, zeus_common, zeus_rblib
# from _zeusrobot.zeus_error import ZeusRobotException, ZeusIOException, ZeusSharedMemoryException, \
# ZeusPositionException, ZeusJointException, ZeusCoordinateException, ZeusMotionParamException, ZeusRobotCriticalException

_BASE = zeus_rblib._BASE

# # import this function if you want to save printed messages to log file
# def print(*args, **kwargs):
#     zeus_common.print(*args, **kwargs)

print("========== ZeusRobot API has been loaded ==========")

#region Zeus Robot API Class
class ZeusIO(zeus_io._ZeusIO):
    pass


class ZeusSharedMemory(zeus_common._SharedMemory):
    pass


class ZeusRobot(zeus_rblib._ZeusRobot):
    pass


class Position(zeus_rblib._Position):
    pass


class Joint(zeus_rblib._Joint):
    pass


class Coordinate(zeus_rblib._Coordinate):
    pass


class MotionParam(zeus_rblib._MotionParam):
    pass
#endregion

if __name__ == "__main__":
    # sample code
    rb = ZeusRobot()

    p = Position()
    p = Position(100,-20,10,90,0,180)
    j = Joint(1,2,3,4,5,6)
    c = Coordinate(1,2,3,4,5,6)
    mp = MotionParam(jnt_speed = 50)

    rb.open(check_servo=False)
    io = ZeusIO()
    io.open()
    
    rb.move(Joint(0,0,90,0,90,0))
    rb.move(Joint(0,0,45,0,45,0))

    # print(rb.acq_permission())

    # MOTIONPARAM
    # print(rb.set_motionparam(50,50,0.2,0.2,1,1,0.5,50,10,0x11000000))
    # print(rb.get_motionparam().mp2list())
    # print(rb.clear_motionparam())
    # print(rb.get_motionparam().mp2list())

    # # QUEUE METHODS
    # print(rb.async_motion(1))
    # print(rb.wait_motion())
    # print(rb.stop())
    # print(rb.pause(5))
    # print(rb.resume())
    # print(rb.async_motion(2))

    # SETTING METHODS
    # print(rb.set_servo_off())
    # print(rb.set_tooloffset(1, 1,1,1,1,1,1))
    # print(rb.change_tool(1))
    # print(rb.change_tool(0))
    # print(rb.set_mdo(1, 23, 0 ,1, 30))
    # print(rb.set_mdo(8, 23, 1 ,2, 10))
    # print(rb.enable_mdo(129))
    # print(rb.disable_mdo(129))

    # GET POSITION or JOINT
    # print(rb.get_position().pos2list())
    # print(rb.get_joint().jnt2list())
    # print(rb.Joint2Position(rb.get_joint()).pos2list())
    # j1 = Joint(0,0,90,0,90,0)
    # j2 = Joint(0,0,0,0,0,0)
    # p1 = rb.Joint2Position(j1)
    # p2 = rb.Joint2Position(j2)
    # print(p2.pos2list())
    # print(rb.Position2Joint(p1).jnt2list())

    # ADJUST_MT
    # j1 = Joint(0, 0, 90, 0, 90, 0)
    # p1 = rb.Joint2Position(j1)
    # p1_val = p1._position()
    # p1_str = [str (round(x,2)) for x in p1_val[0:6]]
    # new_mt = rb.adjust_mt(p1, p1_str[0],p1_str[1],p1_str[2],p1_str[3],p1_str[4],p1_str[5])
    # print(new_mt)
    # p1_str += [str (p1_val[7]), "0x%06X" % new_mt]
    # print("Position String : %s"%p1_str)

    # OVERRIDE
    # print(rb.set_motionparam(lin_speed=200, jnt_speed=20))
    # print(rb.override(100))

    # MOTION METHODS
    # print(rb.home())
    # print(rb.move(Joint(0, 0, 90, 0, 90, 0)))
    # print(rb.move(Position(100,-370,570,90,0,180,7)))
    # print(rb.move_line(Position(110,-370,570,90,0,180,7)))
    # print(rb.move_line(Position(300, -370, 570, 90, 0, 180, 7)))
    # print(rb.move_optline(Position(100, -370, 570, 90, 0, 180, 7)))
    # print(rb.move_rel_tool(1,1,1,1,1,1))
    # print(rb.move(Joint(0,0,90,0,90,0)))
    # print(rb.move_rel_jnt(1,1,1,1,1,1))
    # print(rb.move(Joint(0,0,90,0,90,0)))
    # print(rb.move_rel_line(1,1,1,1,1,1))

    # MOVE_ARC
    # print(rb.move(Joint(0,0,90,0,90,0)))
    # p1 = Position(100,-320,570,90,0,180,_BASE,7)
    # p2 = Position(600,-370,570,90,0,180,_BASE,7)
    # print(rb.move_arc(p1, p2, 0))

    # MOVE (multiple args)
    # mp1 = MotionParam(lin_speed=100, jnt_speed=20, overlap=30)
    # mp2 = MotionParam(lin_speed=100, jnt_speed=10, overlap=30)
    # mp3 = MotionParam(lin_speed=100, jnt_speed=30, overlap=30)
    # j1 = Joint(0,0,90,0,90,0)
    # p1 = Position(200,-370,570,90,0,180, _BASE, 7)
    # p2 = Position(200,-370,670,90,0,180, _BASE, 7)
    # p3 = Position(100,-370,670,90,0,180, _BASE, 7)
    # print(rb.async_motion(1))
    # print(rb.move(mp1,j1,p1,p2,mp2,p3))
    # print(rb.wait_motion())
    # print(rb.move(mp1,j1,p1,p2,mp2,p3))
    # print(rb.async_motion(2))
    # print(rb.rel_permission())

    rb.close()




