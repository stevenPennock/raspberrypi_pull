import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class WebcamPublisher(Node):
    def __init__(self):
        super().__init__('webcam_publisher')
        self.publisher_ = self.create_publisher(Image, '/webcam_topic', 10)
        self.timer_ = self.create_timer(0.1, self.publish_webcam_frame)
        self.bridge_ = CvBridge()
        self.cap_ = cv2.VideoCapture(5)

    def publish_webcam_frame(self):
        ret, frame = self.cap_.read()
        if ret:
            image_msg = self.bridge_.cv2_to_imgmsg(frame, encoding='bgr8')
            self.publisher_.publish(image_msg)

def main(args=None):
    rclpy.init(args=args)
    webcam_publisher = WebcamPublisher()
    rclpy.spin(webcam_publisher)
    webcam_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()