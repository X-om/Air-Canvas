Hello.. , Hackathon Crakers 

This repo will contain all the modules and instructions to run the "Air Canvas" on your end / system 

# Before Making Any Pull Request, Please Install Following Requirements 

1. Python (Version 3.11)
   - Since mediapipe is not supported for Python 3.11 version, do not install Python 3.12, the latest market version.

2. Create Virtual Environment (venv)
   - To create a venv, run this command in terminal/cmd:
     ```
     python3.11 -m venv myenv 
     ```
     (myenv is a name for venv)
     
     After myenv folder is created, navigate to the folder path/to/myenv/bin/pyhton.
     Copy the path.
     The copied path will be the interpreter path for the project.

# Run this command before installing libraries:

     - Linux: source path/to/myenv/bin/activate
     - Windows: path/to/myenv/bin/activate
       
       Replace path/to/myenv with your actual path to myenv.

# Libraries Installation 

After running the above commands, your environment will be activated in terminal/cmd.

1. opencv-python
    pip install opencv-python

2. mediapipe
    pip install mediapipe


To check if libs are installed or not, run:
    pip show opencv-python
        output :
            (myenv) om@Oms-MacBook-Pro python % pip show opencv-python
            Name: opencv-python
            Version: 4.9.0.80
            Summary: Wrapper package for OpenCV python bindings.
            Home-page: https://github.com/opencv/opencv-python
            Author:
            Author-email:
            License: Apache 2.0
            Location: /opt/homebrew/Cellar/python@3.11/3.11.8/bin/myenv/lib/python3.11/site-packages
            Requires: numpy, numpy, numpy, numpy, numpy, numpy
            Required-by:
    
    pip show mediapipe
        output :
            (myenv) om@Oms-MacBook-Pro python % pip show mediapipe
            Name: mediapipe
            Version: 0.10.9
            Summary: MediaPipe is the simplest way for researchers and developers to build world-class ML solutions and applications for mobile, edge, cloud and the web.
            Home-page: https://github.com/google/mediapipe
            Author: The MediaPipe Authors
            Author-email: mediapipe@google.com
            License: Apache 2.0
            Location: /opt/homebrew/Cellar/python@3.11/3.11.8/bin/myenv/lib/python3.11/site-packages
            Requires: absl-py, attrs, flatbuffers, matplotlib, numpy, opencv-contrib-python, protobuf, sounddevice
            Required-by:


# Before Pushing Any Commits to the master/main Branch, Do Consider Discussing the Changes First 

# Thank You      
