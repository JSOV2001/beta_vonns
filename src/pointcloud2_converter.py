#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import PointCloud2, LaserScan
from laser_geometry import laser_geometry 

def callback_function(my_message):
    pointcloud2_message = laser_projection.projectLaser(my_message)
    pointcloud2_converted_publisher.publish(pointcloud2_message)

if __name__ == "__main__":
    rospy.init_node("laserscan_to_pointcloud")

    pointcloud2_converted_publisher = rospy.Publisher("pointcloud2_converted", PointCloud2, queue_size=10)
    
    laser_projection = laser_geometry.LaserProjection()
    laserscan_subscriber = rospy.Subscriber("/scan", LaserScan, callback_function)
    rospy.spin()