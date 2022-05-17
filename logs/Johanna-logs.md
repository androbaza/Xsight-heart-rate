## Week 1
* 20 min organisation of meeting, contacting supervisors, setting up Trello group, writing down tasks (see screenshots [1](https://github.com/androbaza/Xsight-heart-rate/blob/2cc0a0850e370eeeeaecdf9214cf0927e0c806ca/resources/screenshots/Trello1.PNG) and [2](https://github.com/androbaza/Xsight-heart-rate/blob/2cc0a0850e370eeeeaecdf9214cf0927e0c806ca/resources/screenshots/Trello2.PNG))
* 30 min looking for publications on the method in general, 4 interesting papers found
https://downloads.hindawi.com/journals/js/2021/9995871.pdf, 
https://www.sciencedirect.com/science/article/abs/pii/S1746809414000421, 
https://www.scitepress.org/Papers/2020/97932/97932.pdf, 
https://www.rouast.com/pdf/rouast2016remote_a.pdf
* 25 min collecting the found papers, share them with the group members and sum up the topic 
* 60 min reading papers more in detail, writing down some important information (see [PDF](resources/notes/notes_26_04.pdf))
* 105 min research on automatic face tracking, found good tutorials on how to implement face tracking software using OpenCV, implementation depends on the hardware, so we should decide for the hardware next 
(https://towardsdatascience.com/automatic-vision-object-tracking-347af1cc8a3b,
https://github.com/Mjrovai/OpenCV-Object-Face-Tracking,
https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)![image](https://user-images.githubusercontent.com/104530052/165629559-d5d6a4ae-f907-4828-b9f6-5f4b90f0eda7.png)

## Week 2
* 1 h reading the results and progress of my team mates and fixing the goal for this week: hardware decisions. We need to look for available hardware to prepare for the discussion with our mentors on Thursday and order soon 
* [list](https://github.com/androbaza/Xsight-heart-rate/blob/2cc0a0850e370eeeeaecdf9214cf0927e0c806ca/resources/screenshots/Hardware_%20list%20auf%20Weekly%20Tasks%20_%20Trello.pdf) of necessary hardware components
* 2 h detailed research on hardware components: display, energy supply and buttons (details and thoughts on [Trello card](https://github.com/androbaza/Xsight-heart-rate/blob/2cc0a0850e370eeeeaecdf9214cf0927e0c806ca/resources/screenshots/Hardware_%20display,%20battery,%20button%20auf%20Weekly%20Tasks%20_%20Trello.pdf))
* 1 h thinking about the design, looking for examples of other portable devices: if we can fit the hardware in it would be cool to have it in the shape of a non-contact [thermometer](https://www.lazada.sg/products/new-version-forehead-thermometer-infrared-thermometer-non-contact-thermometers-with-fever-alarm-handheld-temperature-measurement-device-multifunction-digital-temperature-measuring-tool-i717568214.html) or we use a shape which allows to have more space for the electronics like [this](https://bauer-pk.net/Honeywell-EDA60K-1D-USB-BT-WLAN-Num.-Kit-USB-Android-EDA60K-0-N223ENEOK/EDA60K-0-N223ENEOK?utm_term=&utm_campaign=Shopping&utm_source=adwords&utm_medium=ppc&hsa_acc=7131830189&hsa_cam=6492203989&hsa_grp=123134659109&hsa_ad=528040447138&hsa_src=g&hsa_tgt=pla-1462500942442&hsa_kw=&hsa_mt=&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQjwpcOTBhCZARIsAEAYLuWo6ObPPawsN4fILLCh_C1MukY_Kr8it-KKvBIeNc8WZrnYdj353PYaAmyEEALw_wcB). We could use Blender as a software to make a model and print the case. If we have the possibility it would be nice to have some kind of soft material for the hold. We need to think about how to connect the case with the electronics.

* To do for next week: we will discuss our progress on Thursday afternoon and hopefully decide to order some hardware components. After that we can start with the implementation of the software.

## Week 3
* in last weeks meeting we decided that I will work on the design and hardware components of our prototype 
* goal for this week: choose a CAD software and get familiar with it
* 1/2 h looking at different software (Tinkercad, Fusion 360, AutoCAD, Blender); I read some articles about the possibilities and advantages and decided to go for Fusion 360 which is for free for students and used in industry for mechanical design
* 1 h creating account, installation process: Fusion 360 offers an online version I wanted to use (due to some error on the website I couldn't and also the verification of my university account took longer than expected; overall a bit annoying, but at least the download version did work in the end)
* 1/2 h watching introduction videos to [Fusion 360](https://help.autodesk.com/view/fusion360/ENU/courses/AP-GET-STARTED-OVERVIEW)
* found this useful list of [shortcuts](https://defkey.com/autodesk-fusion-360-shortcuts?orientation=portrait&filter=false&cellAlternateColor=%23d6ffef&showPageNumber=true&showPageNumber=false&pdf=True)
* 1 h looking for tutorials on case design + watching this [tutorial](https://www.youtube.com/watch?v=E0NVC8xhf3I) on how to fit a case to a Raspberry Pi, this can be easily adapted to any hardware
* as we will maybe be using an NVIDIA Jetson Nano, CAD models can be found here: [GrabCAD](https://grabcad.com/library/tag/jetson); there are also some case models, we could use as a starting point
* 1/2 h finding important aspects for case design:
  * all parts have to fit in exactly, so that they can't move
  * in- and output channels
  * air flow, cooling
  * possibility to open the case
  * could also have a simple inner case to prevent damage to the electronics like [this](https://grabcad.com/library/nvidia-jetson-nano-case-1) and an outer well-designed case for handling
* 1/2 h gettig familiar with fusion 360, trying the basics from tutorials myself
* To do for next week: as the hardware is not totally fixed I will start to design an outer case first, which can be later adapted to the exact components

## Week 4
* 1/2 h working on Gantt shart for the presentation regarding design questions
* 1/2 h importing a [CAD model](https://grabcad.com/library/nvidia-jetson-nano-development-board-1) of Jetson Nano in Fusion 
* 
