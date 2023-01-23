import sys
import time
import math

sys.path.append('../lib/python/amd64')
import robot_interface as sdk

if __name__ == '__main__':

    HIGHLEVEL = 0xee
    LOWLEVEL  = 0xff

    udp = sdk.UDP(HIGHLEVEL, 8080, "192.168.12.1", 8082)

    cmd = sdk.HighCmd()
    state = sdk.HighState()
    udp.InitCmdData(cmd)

    motiontime = 0
    while True:
        time.sleep(0.002)
        motiontime = motiontime + 1

        udp.Recv()
        udp.GetRecv(state)


        cmd.mode = 0      # 0:idle, default stand      1:forced stand     2:walk continuously
        cmd.gaitType = 0
        cmd.speedLevel = 0
        cmd.footRaiseHeight = 0
        cmd.bodyHeight = 0
        cmd.euler = [0, 0, 0]
        cmd.velocity = [0, 0]
        cmd.yawSpeed = 0.0
        cmd.reserve = 0
        
        if(motiontime > 0 and motiontime < 2000):
            cmd.mode = 2
            cmd.gaitType = 4
            cmd.velocity = [0.5, 0]
            print("step1", end='\r')
            
        if(motiontime > 2500 and motiontime < 3500):
            cmd.mode = 2
            #cmd.velocity = [0.5,0]
            cmd.yawSpeed = 1
            print("step2", end='\r')

        if(motiontime > 3500 and motiontime < 4700):
            cmd.mode = 2
            cmd.gaitType = 4
            cmd.velocity = [0.5, 0]
            print("step3", end='\r')

        if(motiontime > 4700 and motiontime < 5500):
            cmd.mode = 2
            #cmd.velocity = [0.5,0]
            cmd.yawSpeed = 1
            print("step4", end='\r')

        if(motiontime > 5700 and motiontime < 7500):
            cmd.mode = 2
            cmd.gaitType = 4
            cmd.velocity = [0.5, 0]
            print("step5", end='\r')
        
        if(motiontime > 7500 and motiontime < 8500):
            cmd.mode = 2
            #cmd.velocity = [0.5,0]
            cmd.yawSpeed = 1
            print("step6", end='\r')
        
        if(motiontime > 8500 and motiontime < 11000):
            cmd.mode = 2
            cmd.gaitType = 4
            cmd.velocity = [0.5, 0]
            print("step7", end='\r')

        if(motiontime > 11000 and motiontime < 12000):
            cmd.mode = 2
            #cmd.velocity = [0.5,0]
            cmd.yawSpeed = 1
            print("step8", end='\r')

        udp.SetSend(cmd)
        udp.Send()