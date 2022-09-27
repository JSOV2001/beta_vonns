#!/usr/bin/env python3
import roslib
roslib.load_manifest('laser_assembler')
import rospy
from laser_assembler.srv import AssembleScans2
from sensor_msgs.msg import PointCloud2

if __name__ == "__main__":
    rospy.init_node("pointcloud2_assembler_client")
    rospy.wait_for_service("/assemble_scans2")

    assemble_scans2 = rospy.ServiceProxy('/assemble_scans2', AssembleScans2)
    rviz_publisher = rospy.Publisher("/pointcloud2_assembled", PointCloud2, queue_size=10)

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        try:
            #Se asume la respuesta de la solicitud del ROS Client.
            pointcloud2_response = assemble_scans2(rospy.Time(0,0), rospy.get_rostime())

            rviz_publisher.publish(pointcloud2_response.cloud)
            
            rate.sleep()
            
        except rospy.ServiceException:
            print("Point clouds failed to assemble")