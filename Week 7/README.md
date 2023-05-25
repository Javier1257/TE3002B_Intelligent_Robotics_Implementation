<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/ManchesterRoboticsLtd/TE3002B_Intelligent_Robotics_Implementation/blob/main/Misc/Logos/Logotipo%20Vertical%20Bco_Transparente.png">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/ManchesterRoboticsLtd/TE3002B_Intelligent_Robotics_Implementation/blob/main/Misc/Logos/Logotipo%20Vertical%20Azul%20transparente.png">
  <img alt="Shows ITESM logo in black or white." width="160" align="right">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/ManchesterRoboticsLtd/TE3002B_Intelligent_Robotics_Implementation/blob/main/Misc/Logos/MCR2_Logo_White.png">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/ManchesterRoboticsLtd/TE3002B_Intelligent_Robotics_Implementation/blob/main/Misc/Logos/MCR2_Logo_Black.png">
  <img alt="Shows MCR2 logo in black or white." width="150" align="right">
</picture>

---
# TE3002B Week 7: Neural Networks.
---
 
 This week will introduce the basics of Neural Networks and its implementation on the Puzzlebot.
 
  ## Files for this session
  * [activities and instal files](my.sharepoint.com/:f:/g/personal/mario_mtz_manchester-robotics_com/EqsMKMm4UqJCmhnUHEI-xE0B6J-UlYj9kd1KGNxGt3T5AQ?e=kehrqy)
  * [ultralitics git](https://github.com/ultralytics/yolov5)
  * [nvidia jetson nano](https://github.com/dusty-nv/jetson-inference/tree/master)

  ## Session 1
  *	Introduction to neural networks
  * Activity 1: Deploy a CNN into a ROS to perform image classification.
  
  ## Session 2
  * Traffic sign detection vs Traffic sign classification.
  * Activity 2: Test one of the prebuild AI solutions in the jetson Nano and implement it In a ROS node.
  *	Activity 3: Deploy the sign detection model in ROS.
  *	AI in edge devices, model optimisation for jetson Nano.


  ## Mini Challenge
  * 

  Please note: This repository contains all the neccesary files and presentations given during this session and the instructions for each one of the activities of the session.

---

## YouTube Video
[Line Following Video](https://www.youtube.com/watch?v=Ah8C9yeG8Eg)

[OpenCV Video](https://www.youtube.com/watch?v=xrpC3FEfINw)

---

### Useful Links: 
#### Machine Learning
  * [NVIDIA Deep Learning Institute](https://www.nvidia.com/en-us/training/)
  * [Machine Learning Course](https://www.tensorflow.org/resources/learn-ml?gad=1&gclid=Cj0KCQjwjryjBhD0ARIsAMLvnF_DOVyienJaRisWCaPayBboZh7kgRr7XokSHVn3_y1Q03SAy70fJbcaAvosEALw_wcB)
  * [Machine Learning Book](https://developers.google.com/machine-learning/crash-course/ml-intro)
  * [Deep Learning for Large-Scale Traffic-Sign Detection and Recognition](https://arxiv.org/abs/1904.00649)
  * [Machine Learning: A Probabilistic Perspective](http://noiselab.ucsd.edu/ECE228/Murphy_Machine_Learning.pdf)
  * [Neural Networks Fundamentals Video](https://www.youtube.com/watch?v=aircAruvnKk&t=143s)
  * [CNN Fundamentals Video](https://www.youtube.com/watch?v=QzY57FaENXg&t=260s)
  * [Deep Learning Book](https://www.deeplearningbook.org/)


#### OpenCV and Robot Vision
 * [Robot Vision](https://mitpress.mit.edu/9780262537377/robot-vision/)
 * [Computer Vision Book](https://www.cs.ccu.edu.tw/~damon/tmp/SzeliskiBook_20100903_draft.pdf)
 * [Computer Vision Book 2](https://doc.lagout.org/science/0_Computer%20Science/2_Algorithms/Concise%20Computer%20Vision_%20An%20Introduction%20into%20Theory%20and%20Algorithms%20%5BKlette%202014-01-20%5D.pdf)
 * [Camera Models](https://web.stanford.edu/class/cs231a/course_notes/01-camera-models.pdf)
 * [Blurs and Filters Video](https://www.youtube.com/watch?v=C_zFhWdM4ic)
 * [Morphologiclal Operators](https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html)
 * [Sobel Operator](https://en.wikipedia.org/wiki/Sobel_operator)
 * [Sobel Operator Video](https://www.youtube.com/watch?v=uihBwtPIBxM&t=1s)
 * [Blob detection](https://en.wikipedia.org/wiki/Blob_detection#:~:text=In%20computer%20vision%2C%20blob%20detection,color%2C%20compared%20to%20surrounding%20regions.)
 * [OpenCV BlobDetection](https://docs.opencv.org/3.4/d0/d7a/classcv_1_1SimpleBlobDetector.html)
 * [Canny Detector Tutorial](https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html)
 * [Canny Edge Detector Video](https://www.youtube.com/watch?v=sRFM5IEqR2w)


#### Robotics and Control
* [Introduction to Autonomous Mobile Robots](https://ieeexplore.ieee.org/book/6267528)
* [PID Control](https://ieeexplore.ieee.org/document/1453566)
* [Closed Loop Control](https://www.electronics-tutorials.ws/systems/closed-loop-system.html)
* [Nonlineraities and robustness](https://ieeexplore.ieee.org/document/8603065)
* [Open loop control Tutorial](https://www.electronics-tutorials.ws/systems/open-loop-system.html)
* [Open Loop Control Tutorial](https://www.electronicshub.org/open-loop-system/)
* [Open Loop Control Book](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Signal_Processing_and_Modeling/Introduction_to_Linear_Time-Invariant_Dynamic_Systems_for_Students_of_Engineering_(Hallauer)/14%3A_Introduction_to_Feedback_Control/14.02%3A_Definitions_and_Examples_of_Open-Loop_Control_Systems)


#### ROS
 * [ROS Installation](http://wiki.ros.org/noetic/Installation/Ubuntu)
 * [ROS book](https://www.cse.sc.edu/~jokane/agitr/)
 * [ROS Packages](http://wiki.ros.org/ROS/Tutorials/CreatingPackage)
 * [ROS Workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)
 * [Publisher and Subscribers](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)
 * [Roslaunch](http://wiki.ros.org/roslaunch)
 ---
