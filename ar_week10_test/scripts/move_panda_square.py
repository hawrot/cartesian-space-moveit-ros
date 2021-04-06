#!/usr/bin/env python
import sys
from math import pi
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import time
from ar_week10_test.msg import square

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_panda_square', anonymous=True)


robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
move_group = moveit_commander.MoveGroupCommander('panda_arm')
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=20)

def callback(data):
    try:
        print '---- Recieved the squares ---'
        start_config = [0, -pi/4, 0, -pi/2, 0, pi/3, 0] # Start config specified on the coursework
        move_group.go(start_config, wait=True) # Move the robot to the configuration
        move_group.stop()

        print '---- Planing Trajectory ---'
        waypoints = []

        pos = move_group.get_current_pose().pose

        pos.position.y += data.size
        waypoints.append(copy.deepcopy(pos))

        pos.position.x += data.size
        waypoints.append(copy.deepcopy(pos))

        pos.position.y -= data.size
        waypoints.append(copy.deepcopy(pos))

        pos.position.x -= data.size
        waypoints.append(copy.deepcopy(pos))

        plan, fraction = move_group.compute_cartesian_path(waypoints, 0.01, 0.0) # waypoints, eef_step, jump_threshold

	traj_duration = plan.joint_trajectory.points[-1].time_from_start + rospy.Duration(1.0)
	rospy.sleep(traj_duration)

        display_trajectory = moveit_msgs.msg.DisplayTrajectory()
        display_trajectory.trajectory_start = robot.get_current_state()
        display_trajectory.trajectory.append(plan)
     
        print '---- Display Trajectory ---'
        display_trajectory_publisher.publish(display_trajectory)
        rospy.sleep(traj_duration)
       
        print '---- Execute Trajectory ---'
	move_group.execute(plan, wait = True)
        move_group.stop()
	move_group.clear_pose_targets()

    except rospy.ServiceException, e:
        print("Service call failed: %s" % e)




sub = rospy.Subscriber('size', square, callback)
rospy.spin()
