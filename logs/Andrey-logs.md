## Week 1
* Create group chat
* Create github repo to track code/logs
* Visit [LASER World of PHOTONICS](https://world-of-photonics.com/en/) exhibition in Munich, research currently available sensors related to the project (3 hours) -- suprisingly, nothing of close resemblence was discovered. Biophotonics stands number was frustratingly low 🥺. 
* Research how the remote heart rate estimation is done - photoplethysmography (Remote-PPG) (~1 hour). 
* Explore the [state-of-the-art algrithms list](https://paperswithcode.com/task/heart-rate-estimation) (2 hours so far, in progress)
  * [Latest method](https://paperswithcode.com/paper/efficient-deep-learning-based-estimation-of). Uses images from frontal smartphone camera for heartate and SpO2 estimation. No code released yet. Will contact the paper authors.
  * [Deployable method](https://github.com/terbed/Deep-rPPG) - coulb be run on Nvidia Jetson nano (have to check performance).

## Week 2
* Contacted Taha Samavati regarding code for [method](https://paperswithcode.com/paper/efficient-deep-learning-based-estimation-of) from previous week. Got a positive answer. Will test the model this week.
* Read papers, presenting latest methods in heart rate estimation (7 hours): 
  * [Self-supervised Representation Learning Framework for Remote Physiological Measurement Using Spatiotemporal Augmentation Loss](https://arxiv.org/pdf/2107.07695v2.pdf)
    * comment: self-supervised method is not deployable.
  * [A Review of Deep Learning-Based Contactless Heart Rate
Measurement Methods](https://www.mdpi.com/1424-8220/21/11/3719/pdf).
    * comment: recent review paper. useful to understand the current field.
  * [Instantaneous Physiological Estimation using Video Transformers](https://arxiv.org/pdf/2202.12368v1.pdf)
    * comment: promising model, rgb input. plan to test this model next. [repo](https://github.com/revanurambareesh/instantaneous_transformer).
    * started running the docs to understand how to run the code. imported github repo to colab 
    * the requierements.txt and model weights are missing. Need to consult authors.
  * [Beat-to-Beat Cardiac Pulse Rate Measurement From Video](https://openaccess.thecvf.com/content/ICCV2021W/V4V/papers/Hill_Beat-To-Beat_Cardiac_Pulse_Rate_Measurement_From_Video_ICCVW_2021_paper.pdf)
    * comment: method participated in V4V challenge in Fall 21. no code released. will contact authors.  MAE 9.37 beats/min, faster inference. 
  * [Automatic region-based heart rate measurement using remote
photoplethysmography](https://openaccess.thecvf.com/content/ICCV2021W/V4V/papers/Kossack_Automatic_Region-Based_Heart_Rate_Measurement_Using_Remote_Photoplethysmography_ICCVW_2021_paper.pdf)
    * comment: method participated in V4V challenge in Fall 21.

## Week 3

* Probably useful later: [Arduino lib](https://github.com/oxullo/Arduino-MAX30100) for Maxim Integrated MAX30100 oximetry / heart rate sensor.
* Task of the week: get at least one Deep Learning model inference running.
* The most developed framework found so far: [Paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9044207/), [Repo](https://github.com/phuselab/pyVHR)
* Tried to run on Macbook: stuck at *Unsupported hardware* error :( (2 hours)
* Got results on [Colab](https://github.com/androbaza/Xsight-heart-rate/blob/main/resources/notebooks/XSight_pyVHR.ipynb)! (3 hours). Left figure: video from laptop webcam, sitting still. Right figure: sitting still in the beginning and then doing squats for a minute.

![result1](../resources/notebooks/bpm_demo.png)![result2](../resources/notebooks/pyVHR_exercise.png)

## Week 4

* Working with pyVHR on Colab is not efficient due to mandatory libs installation of 40-60 minutes every time. Sometimes the process is stuck. Lost of troubleshooting (3 hours spent, no real work progress)
* Read about Jetson Nano workflow (1.5 hours)
* Work on further project plan:
    * install ubuntu on jetson nano. (1-2 hours, finish before 21.05) 
    * install [pyVHR](https://github.com/phuselab/pyVHR) libs, and [Deep-rPPG](https://github.com/terbed/Deep-rPPG). (up to several days, finish before 25.05)
    * compare the stability of the two frameworks, chose the one to stick around with. (up to several days, finish before 29.05)
    * connect the camera to Jetson nano, learn to acquire a short video from it by pressing a button. (3-4 hours, finish before 01.06)
    * create pipeline for video feeding to the selected framework. (up to several days, finish before 08.06)
    * learn to read the framework output as text. connect screen, format the output to be corretly displayed. (finish before 15.06)
    * ----------------- MVP point - further developments are aimed at optimization ----------------
    * make the pipeline live.
      * estimate the minimal video length, at which the accuracy is adequate.

## Week 5
* While waiting for Haseeb to finish with the remote acceess setup on Jetson, I'll start with the "video recording and feeding to algorithm" pipeline (research, 3 hours).
* Pushbutton is easily connected to the Jetson: [video](https://www.youtube.com/watch?v=ehzrPl5cNCc), [tutorial](https://jetsonhacks.com/2015/12/29/gpio-interfacing-nvidia-jetson-tx1/). -- could have the button on on the jetson board itself 
* Reading Camera input [GStreamer tutorial (official method)](https://developer.ridgerun.com/wiki/index.php?title=GStreamer_Daemon_-_MP4_Video_Recording),
* [CV2 python code for short video recording to try](https://github.com/aarushi-nema/jetson-nano/blob/master/openCV003_save_read.py)).
* Very nice project for remote temperature measurement on Jetson nano [repo](https://github.com/tomek-l/ai-thermometer) -- bits and pieces could be useful.

## Week 6
* For some reason the Jetson nano refuses the connection via NoMachine for remote access. Troubleshooting (2h). Haseeb will set it up at Lichtwerkstatt for physical access.
* Looked more closely through [temperature measurement project](https://github.com/tomek-l/ai-thermometer) methods to understand the interacton with jetson hardware (2h).
    * Particularly interesting is [camera interaction scripts](https://github.com/tomek-l/ai-thermometer/blob/master/docs/camera_scripts/gstreamer_commands.md)
    * [Notebooks](https://github.com/tomek-l/ai-thermometer/tree/master/docs/notebooks) provide nice step-by-step guides on running a model similar to ours. 
