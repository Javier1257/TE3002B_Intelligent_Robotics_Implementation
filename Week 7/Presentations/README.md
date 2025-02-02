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
# Week 7: Presentations.

  * In this folder you will find the presentation used during this course

---
  ## Presentations
  
   ### MCR2_

  ## Installation Instructions
  
  ### Tensorflow

	sudo apt update

	sudo apt install python3-dev python3-pip python3-venv

	pip3 install --user --upgrade tensorflow # install in $HOME 
  

  ### Pycharm, Torchvision and onnx 

	Step 0 
		Copy yolo_rec into you catkin_make
		Open a terminal in src/yolov5
	Step 1 
		sudo apt update
		sudo apt install -y python3-pip
		pip3 install --upgrade pip
	Step 2
		cd yolov5
		sudo apt install -y libfreetype6-dev
		pip3 install -r requirements.txt
	Step 3 
		cd ~
		sudo apt-get install -y libopenblas-base libopenmpi-dev
		wget https://nvidia.box.com/shared/static/fjtbno0vpo676a25cgvuqc1wty0fkkg6.whl -O torch-1.9.0-cp36-cp36m-linux_aarch64.whl
		pip3 install torch-1.9.0-cp36-cp36m-linux_aarch64.whl
	Step 4
		sudo apt install -y libjpeg-dev zlib1g-dev
		git clone --branch v0.9.0 https://github.com/pytorch/vision torchvision
		cd torchvision
		sudo python3 setup.py install
	Step 5 
		# Download pip wheel from location mentioned above
		$ wget https://nvidia.box.com/shared/static/jy7nqva7l88mq9i8bw3g3sklzf4kccn2.whl -O onnxruntime_gpu-1.10.0-cp36-cp36m-linux_aarch64.whl
		$ pip3 install onnxruntime_gpu-1.10.0-cp36-cp36m-linux_aarch64.whl
