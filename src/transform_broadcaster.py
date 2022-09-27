#!/usr/bin/env python3
import rospy
import tf2_ros
from tf_conversions import transformations 
from geometry_msgs.msg import TransformStamped
import serial
import math

def send_transform(angle):
    transform_broadcaster = tf2_ros.TransformBroadcaster()
    transformation_data = TransformStamped()

    #Se define los frames en cuestion
    transformation_data.header.frame_id = "laser"
    transformation_data.child_frame_id = "link"
    
    #Se define cuando se toma la ultima transformacion del frame
    transformation_data.header.stamp = rospy.Time.now()
    
    #Se definen los datos de la traslacion
    transformation_data.transform.translation.x = 0.0
    transformation_data.transform.translation.y = 0.0
    transformation_data.transform.translation.z = 0.0
    
    #Se definen los datos de la rotacion
    quaternions = transformations.quaternion_from_euler(0.0, math.radians(angle), 0.0)
    transformation_data.transform.rotation.x = quaternions[0]
    transformation_data.transform.rotation.y = quaternions[1]
    transformation_data.transform.rotation.z = quaternions[2]
    transformation_data.transform.rotation.w = quaternions[3]

    transform_broadcaster.sendTransform(transformation_data)

if __name__ == "__main__":
    rospy.init_node("transform_broadcaster_tf2")
    transform_broadcaster = tf2_ros.TransformBroadcaster()

    lidar_port = '/dev/ttyACM0'
    arduino_port = '/dev/ttyUSB0'
    with serial.Serial(arduino_port, 9600, timeout=1) as my_serial_port:
        print(f"LiDAR port: {lidar_port}")
        print(f"Arduino port: {arduino_port}")
        print("Start printing angles!")

        angle_string = ""
        angle_int = 0
        while not rospy.is_shutdown():
            angle_byte = my_serial_port.readline() #Se lee el angulo del Arduino

            if angle_byte.decode("utf-8") == "":
                continue
            else:
                angle_string = angle_byte.decode("utf-8").strip('\n').strip('\r') #Se transforma el angulo en entero
                angle_int = int(angle_string)
            print(f"Angle: {angle_int}°")
            
            send_transform(angle_int)
            
            if angle_int == 44:
                break
            