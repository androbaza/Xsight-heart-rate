# Week 1

* went through the slides of the lecture and the notes of my team-mates (1h)
* looking up some stuff on the web and doing some internet research on the topic (1h)
* had a look into [openCV](https://opencv.org/) - discovered that they also sell cameras for face recognition: [OpenCV AI Kit: OAK—1](https://store.opencv.ai/products/oak-1)
  * could be used for tracking of the face...
  * question: What is our budget? How much can we spend?
* short cost estimation for prototype: 70€ Raspberry Pi 4 with equipment, 150€ camera, 10€ battery, + cables and other stuff <img src="https://render.githubusercontent.com/render/math?math=\approx"> 300€

# Week 2
* medical term for our task: remote Photoplethysmography (rPPG) = contactless method that is used to detect volumetric changes in blood in vessels beneath the skin (see [A Review of Deep Learning-Based Contactless Heart RateMeasurement Methods](https://mdpi-res.com/d_attachment/sensors/sensors-21-03719/article_deploy/sensors-21-03719.pdf)) - further informations from this paper:
 * deep learning methods perform better than the conventional methods (see chapter 4.2)
 * the publicly available code _PhysNet_ performed the best and measured the heart rate with best precision (mean absolute error value of 2.57 beats per minute)
 * the code for _PhysNet_ was introduced by [this paper](https://arxiv.org/pdf/1905.02419.pdf) - they were able to do real time video analysis, but with the use of an [NVIDIA Tesla P100 GPU](https://www.nvidia.com/de-de/data-center/tesla-p100/) (not portable at all...) --> computational power will be a big problem
* further research led me to this page: [Deep-rPPG: Camera-based pulse estimation using deep learning tools](https://github.com/terbed/Deep-rPPG) - there they did the computation on an [NVIDIA Jetson Nano](https://developer.nvidia.com/embedded/jetson-nano) - this code was written for a Master thesis which is also uploaded in this GitHub repo ;)

# Week 3
* in last weeks meeting we decided that I will have a closer look onto the camera we will use in our "medical tricoder"
* take-home messages from the talk with Michael from XSight Optics: (1.5 h)
  * Raspberry Pi Camera does not work --> to noisy ([this one](https://www.raspberrypi.com/products/camera-module-v2/))
  * good camera is very power consuming --> heat sink 
  * postpone question regarding battery
  * Display: shows user some guidance --> e.g. some LCD with text messages
  * camera: image stabilization on hardware side would be good
* before the chat with Michael we already decided - based on all of our research - to use an [NVIDIA Jetson Nano](https://developer.nvidia.com/embedded/jetson-nano) as computation basis - this thought was welcomed by Michael :) (discussion together 1 h)
* there is also another [high quality camera for raspberry pis](https://www.raspberrypi.com/products/raspberry-pi-high-quality-camera/) --> could be already sufficient
* name of the camera connector for the Jetson Nano: MIPI CSI-2 --> a lot of camera sensors with this connector can be found [here](https://www.vision-components.com/en/products/oem-embedded-vision-systems/mipi-camera-modules/#c5082)
* as far as I remember I saw such a camera lying around in the Makerspace --> task for myself: look up the type to see if this one could work as wel (advantage: no ordering process which takes us time)
* if one wants to know more about this MIPI connector there is [this short article](https://www.linkedin.com/pulse/what-mipi-camera-how-does-work-e-con-systems/)
* time for this research and the log (1.5 h)

# Week 4
* I got an introduction into the workshop in the ACP from Daniel Füßel (1h) - maybe we can do some useful stuff there later. Devices that are available there:
  * Lathe for metal
  * Milling machine - also for metal
  * Everything else that a workshop has (drills, saws, etc.)
* notes from meeting with Jan, Michael and Maria last week (1h)
  * no PLA for camera holder --> too hot (maybe use an active cooler)
  * to do: assemble a list of stuff we need --> then ask the guys from Xsight or Lichtwerkstatt
  * to do: write a project plan --> Which tools? Gantt chart (lucid chart, Canva), Kanban with Trello
* having a look at all of the hardware stuff, which is available in the Makerspace (0.5h)
* preparing a project plan with our so far taken notes and the thoughts provided by the others (1.5h)
