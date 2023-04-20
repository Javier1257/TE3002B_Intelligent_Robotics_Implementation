#!/usr/bin/env python
import rospy

class DeadReckon:
    def __init__(self):
        print("Constructor")

        #Set the parameters of the system

        # Setup Variables to be used

        # Declare the output Messages

        # Declare the input Message

        # Setup the Subscribers

        #Setup de publishers


    #Define the callback functions (if required)


    #Define the main RUN function
    def run (self):
        print("Running")


    #Define Other functions
    def Other(self):
        print("Other")



    #Stop Condition
    def stop(self):
    #Setup the stop message (can be the same as the control message)
        print("Stopping")



if __name__=='__main__':

    #Initialise and Setup node
    rospy.init_node("Puzzlebot_Pose_Estimator")
 
    # Configure the Node
    loop_rate = rospy.Rate(100)

    #Node Running
    print("The Estimator is Running")

    try:
    #Run the node
        while not rospy.is_shutdown():
            loop_rate.sleep() 
    except rospy.ROSInterruptException:
        pass