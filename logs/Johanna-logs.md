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
* 1/2 h working on Gantt chart for the presentation regarding design questions: (full Gantt chart see presentation)
   * week 5 (25.05.): plan how all technical components can be put together/ are connected / decide for shape and size of outer case
   * week 6 (01.06.): design outer case (consider in- and output, opening structures, heat, handling, material, air flow)
   * week 7 (08.06.): plan the inner structure to hold the components
   * week 8 (15.06.): test print and finalize the printing parts of the case
   * week 9 (22.06.): aluminium structures to prevent heat damage
   * week 10 (28.06.): print final case 
   * week 11 (06.07.): put everything together/test devide
   * week 12 (13.07.): preparation of final presentation


* 1/2 h importing a [CAD model](https://grabcad.com/library/nvidia-jetson-nano-development-board-1) of Jetson Nano in Fusion 
* 1 h working on a simple case around the Jetson to get more hands-on experience with the tools provided by Fusion (modelling, fillet, section analysis), similar to the tutorial mentioned above; needs to be continued as I felt I should learn more basics about CAD software first
* 2 h learning how to make an easy snap fit box with this [tutorial](https://www.youtube.com/watch?v=VVmOtM60VWw) and doing it myself. This has helped me a lot learning about useful tools and hints to simplify work with Fusion (see notes).
* [first snap box](https://github.com/androbaza/Xsight-heart-rate/blob/8ea660b65d5e8e71695e3d14473406fa6aa5a327/resources/screenshots/first%20snap%20box.PNG)

* notes on working with Fusion:
   * 'change parameters' is very useful to fix dimensions and adapt them quickly later
   * construction lines help to find center points and align objects / fix their relative positions (use horizontal/vertical alignment function)
   * creating central plane and mirror function to copy symmetrical aspects
   * section analysis tool helps to see if everything fits together

## Week 5 
* 4 h working on [CAD model](https://github.com/androbaza/Xsight-heart-rate/blob/b3a9464a52f9e3416458cf3a1d4398d84b18be7d/resources/screenshots/first%20case.PNG) for case (including search for the dimensions and existing CAD models of our chosen components; not finished yet as I spent a lot of time on looking up how to do it smart
   * I paid attention on making a smart model which can be adapted quickly to changes in dimensions and shapes
   * example: only changing the main dimensions of the case is enough to quickly adapt the top cover, th click system and the position of the cut outs for display and camera 
 * next week: finish the basic model and maybe print first attempt in small size to check the click system for the top cover

## Week 6 
* 4 h working on hold and click system [CAD model](https://github.com/androbaza/Xsight-heart-rate/blob/21af6cc33f77ef1603e016488aaee0ae038a5ad7/resources/screenshots/first%20snap%20box2.PNG)
   *  idea: put the power bank inside the hold and charge it via bottom cap
   *  therefore: elliptical shpae and elliptical shaped click system
   *  used [this](https://www.youtube.com/watch?v=iF_P5ie_b8o) tutorial for the click system
   *  I wanted to fix the position of hold and case right away, but this caused some troubles with the techniques used in the tutoial -> spent a lot of time on       looking for other ways to do the click system
   *  still have troubles with the mirror method ([see cross section analysis](https://github.com/androbaza/Xsight-heart-rate/blob/21af6cc33f77ef1603e016488aaee0ae038a5ad7/resources/screenshots/click%20problem.PNG)), needs to be fixed next week
   *  so far only used simple shapes to maximize space for components, final shape should look nicer
* next week: finish the basic model and maybe print first attempt in small size to check the click system for the top cover

## Week 7
* 2 h (with Tim in the Lichtwerkstatt) preparing a small version of the upper part of our case for the printer:
   * separating case and lid and placing them in different files
   * slice the models for the printer
   * print the case
* notes: case is quite stable, the click system works but is a little bit to stiff 
* future: make the click system less stiff, try different materials
