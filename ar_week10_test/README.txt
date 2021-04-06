Code developed by  Mateusz Hawrot  

200197582 | m.g.hawrot@se20.qmul.ac.uk

-------------------------------------------

To run the package:

1) Unzip the ar_week10_test.zip
2) build and source the workspace	
3) Make nodes exacutable
4) Run the Rviz
5) Run the quare_size_generator.py
6) Run the move_panda_square.py
7) Run the rqt_plot

----------------------------------------------------

Commands

1) To build the package:  catkin_make

2) To source the package: source ~/catkin_ws/devel/setup.bash

3) To run the rviz: roslaunch panda_moveit_config demo.launch

4) Run the python files: rosrun ar_week10_test square_size_generator.py    rosrun ar_week10_test move_panda_square.py

5) To run the rqt_plot : rosrun rqt_plot


----------------------------------------------------

Steps taken: 

1) Generated the package with dependencies (rospy, movieit_commander, moveit_msg, std_msgs)
2) Generated additional folder
3) Generated the message
4) Clone the git repo specified in the coursework instructions
5) Created a node with generates a random value
6) Created a 'move_panda_square.py' which subscribes to node 1
7) Made scripts executable
8) Builded and sourced the package
9) Run the code 
