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
  * Lathe for metal Drehbank
  * Milling machine - also for metal
  * Everything else that a workshop has (drills, saws, etc.)
* notes from meeting with Jan, Michael and Maria last week (1h)
  * no PLA for camera holder --> too hot (maybe use an active cooler)
  * to do: assemble a list of stuff we need --> then ask the guys from Xsight or Lichtwerkstatt
  * to do: write a project plan --> Which tools? Gantt chart (lucid chart, Canva), Kanban with Trello
* having a look at all of the hardware stuff, which is available in the Makerspace (0.5h)
* preparing a project plan with our so far taken notes and the thoughts provided by the others (1.5h)

# Week 5
* notes from meeting with Michael and Jan (1h):
  * SLA printer produces more temperature stable parts
  * hint: try to print some stuff on the 3D printer directly --> learning
  * camera has standard C-mount --> [this is the camera](https://www.alliedvision.com/en/products/alvium-configurator/alvium-1800-c/158/#_configurator) (there is also the STEP data)
  * operational distance: 1m - 1.5m
  * Temron objective - around 5cm long
  * current medical devices: in normal case: 2 min data acqusition, in emergency situations: couple of seconds possible
* before the meeting we had a short preparational conversation as a team (0.5h)
* after the meeting  I tested the laser-cutting device for another 1h (because we had the lecture on this topic before the meeting :)
* that's all I did for this week because there was a holiday and I took some time off ;)

# Week 6
* Regarding the display we found one in the Makerspace of the Lichtwerkstatt - we will use this one :)
* For the battery we will most probably go for a power bank (the Raspberry Pi battery packs are not compatible to the Jetson Nano).
* I picked up the camera (mentioned above) from the Xsight Optics team at the TIP in Jena - handed it over to Haseeb so that he can plug it into the Jetson Nano and install the drivers (1h)
* had a conversation with Julian and Darius on their project to understand their problems at the moment and tried to help with some suggestions (1h)
* watched some introduction videos into Fusion 360 and the GPIO connectors on the Jetson Nano (inspired by Andrey's and Johanna's log) (2h)

# Week 7
* After the lecture last week we had again a meeting with Jan and Michael for feedback on our progress so far - very useful (1h)
* right after the lecture Johanna and I started the first attempt of printing a case of the handheld "medical tricoder" (1h) (at this point thanks to Johanna - she already prepared a very nice case design)
* on the next day I picked up the case - the clickable mechanism does indeed work *-* (that is what we wanted to see with this first print) (0.5h)
* on the weekend I installed Fusion 360 on my laptop and Johanna created a Team so we both can work on the design of the case (1h)
* spent some time on learning how to use Fusion 360 (1h)

# Week 8
* Unfortunately I was sick the whole week and could not do anything for the project.

# Week 9
* I am back again :)
* spent 1h with Johanna in the Lichtwerkstatt to print the next case design - picked it up and cleaned it the next day (0.5h)
* after being in the Lichtwerkstatt I spent 2.5 hours on preparing something for the project presentation - is still secret, but will hopefully be cool :D
* helped Darius and Julian by cutting their cylindrical lens - introduced them to the workshop in the ACP (1.5h)
