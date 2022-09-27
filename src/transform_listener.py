#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import PointCloud2
import tf2_ros
from tf2_sensor_msgs import tf2_sensor_msgs 

def callback_function(message):
    try:
        current_transformation = transform_buffer.lookup_transform("laser", "link", rospy.Time(0,0), rospy.Duration(10.0))
        link_pointcloud2 = tf2_sensor_msgs.do_transform_cloud(message, current_transformation)

        pointcloud2_publisher.publish(link_pointcloud2)
    except:
        return

if __name__ == "__main__":
    rospy.init_node("tf_listener")

    link_pointcloud2 = PointCloud2()
        
    transform_buffer = tf2_ros.Buffer()
    transform_listener = tf2_ros.TransformListener(transform_buffer)

    pointcloud2_converted_subscriber = rospy.Subscriber("/pointcloud2_converted", PointCloud2, callback_function)

    pointcloud2_publisher = rospy.Publisher("/pointcloud2", PointCloud2, queue_size= 10)

    rospy.spin()