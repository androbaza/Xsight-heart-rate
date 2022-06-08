# Week 1 (21.04 to 27.04)

## Preliminary study

- **(1 hour)** Basic biology study and literature review was done to get some rudimentary knowledge about how the biology behind heart rate detection works and to understand how to ideally implement and deploy a handheld solution for contact-less heart rate detection. 
- **(1.5 hour)** Checked out available state-of-the-art and competitor solutions and the underlying motivation and their product offerings. Also looked at available open source codes/programs to implement heart rate estimation. One [particular repository](https://github.com/natalialmg/IR_iHR) was especially well written and helpful to understand how to proceed with face detection, signal denoising and final estimation.
- **(1 hour)** Contemplated and looked at the choice of hardware and the efficiency of each approach. A lot more study and understanding is needed to finalize the choice of hardware and electronics involved.
- **(30 minutes)** Finalizing next week's tasks and detailing log

## Next week tasks

- Hardware selection and discussion
- Deciding the face detection and tracking implementation - Dataset, capture, storage and processing
- Signal denoising for high SNR - implentation and available methods (Maybe after next week?)
- Budget discussion, financial aspect of the project

## Notes

- Papers compiled by Johanna were especially helpful in understanding the biology a little bit. An in-depth study is needed to fully understand what other parameters can be estimated using the facial image of a human.
- OpenCV would be the most lightweight and easy to implement and deploy, but if training and high accuracy with large datasets is considered, Tensorflow/PyTorch implementation in tandem with OpenCV would be beneficial to increase system accuracy over time
- No idea what material we can should use for casing/material of the handheld solution.
- Hardware selection to be discussed and easy integration with other harware in the future to be considered.
  - Jetson Nano looks promising, but let's see if we can go for cheaper processing station
  - ESP32 Cam for dirt-cheap facial capture but processing needs to be done on a server station/main computer (Don't know how efficient we can make this)
  - Raspberry Pi - The go-to device for this but let's try to make the implementation a bit modular so that if we need to change the harware, it could be easily done so.
- Need to check out if just ears/earlobes/nose/forehead can be used to estimate heartbeat. Would eliminate the need for recording faces. 
- Need to find a way to workaround the effect of Melanin on heart rate estimation. Don't want the device to be racist, heh. Can already imagine lawsuits XD


# Week 2 (28.04 to 04.05)

- As others focused researching on methods using OpenCV/camera based method to detect changes in blood in vessels beneath the skin (remote Photoplethysmography (rPPG)), I looked for other methods that could be alternative approaches to the same problem. (7h)
- Best method: Using Doppler radar. [Reference](A_Review_on_Recent_Advances_in_Doppler_Radar_Sensors_for_Noncontact_Healthcare_Monitoring.pdf)
  - [Doppler radar chip](https://www.seeedstudio.com/Grove-Doppler-Radar-BGT24LTR11-p-4572.html) Can be easily used with Arduino
  - Available on [Mouser](https://www.mouser.de/ProductDetail/Seeed-Studio/109020021?qs=sGAEpiMZZMu3sxpa5v1qrgqRbH4gaXhh5TsRi2%2F21j0%3D) for 61 EUR. Need to check other alternatives, if available.
  - Uses the Infineon technologies' **BGT24LTR11N16** MMIC. Datasheet [here](https://www.infineon.com/dgdl/Infineon-BGT24LTR11N16-DataSheet-v01_03-EN.pdf?fileId=5546d4625696ed7601569d2ae3a9158a) 
  - No research/code available on internet for this specific module, since no one used it before for remote heartbeat estimation.
  - If this specific chip is used, the challenge at hand is to write an Arduino library to simplify working with Arduino compatibility layer. This would make it even more efficient.
  - Studied the datasheet and realized this is a pretty well-suited chip for the task at hand.
  - Need to look more into other development boards for better implementation
- Looked at the hardware needed and made a quick list.
  - Arduino (Available in Lichtwerkstatt)
  - Power supply for arduino (Available in Lichtwerkstatt)
  - Doppler radar module (if this is agreed upon in hardware discussion meeting)

## Next week tasks
- Hardware finalization
- Begin implementation

## Notes
- Papers highlighted by Andrey and Tim were extremely helpful, helped me understand how effective rPPG can be and saved me a lot of time from searching and filtering results from the web.
- Most of the heardware needed (Jetson Nano, Raspberry Pi, Power sources, battery bank) is already available in Lichtwerkstatt. Any buttons or casing can be 3D printed using the printers at Lichtwerkstatt.
- It is nice to have multiple approaches to a problem and choose the best suited one.

# Week 3 (05.05 to 11.05)

- Last week, individual project roles were decided. While Andrey focused on implementing a solution that uses 'Deep learning', I was supposed to implement something that had a more classical approach - plain old image processing and statistics.
- This [repo](https://github.com/natalialmg/IR_iHR), as mentioned in previous logs, was a straight forward way to implement rPPG that utilizes classical image processing and statistical denoising for high SNR. But this one uses an IR camera as the source to capture images. Efficacy and result of implementing this same code with an RGB camera is unknown. Tried running this on my PC, but ran into various system errors. Shall try again from scratch with a fresh Linux installation. Since an IR camera is not readily available, I shall put this one aside for now and work on it in the next week. More on this in the Notes section.
- As highlighted by Andrey a few days ago, [this](https://github.com/phuselab/pyVHR) is a pretty impressive framework to implement rPPG. Moreover, this framework enables the choice of using classical methods as well as Deep Learning methods as Modus Operandi. The choice of dataset is also left to the user. Its more like mix-and-match to see what works and what doesn't for a specific user. Well documented framework too. Doesn't use IR camera like the previous repo.
- I shall try running this framework on the Jetson Nano and try to get some rudimentary results in the next week.

## Next week tasks
- Implementing [this](https://github.com/phuselab/pyVHR) (PyVHR) framework on Jetson Nano
- Retry [this](https://github.com/natalialmg/IR_iHR) on my PC - More on this in Notes section
- Try to finalize the choice of the implementation method.

## Notes
- An IR camera is needed to try implementing [this](https://github.com/natalialmg/IR_iHR). I'm not sure if we have an IR camera readily available. I shall discuss with the team and try ordering a very cheap IR camera, if not available at Lichtwerkstatt. Since it would take time for the said order to arrive, I shall work on PyVHR framework and test it on Jetson. I also will compare both the frameworks and choose the most efficient one in terms of ease of implementation and computational burden.
- Did some comparison and stopped here - RGB camera or IR? I guess this depends on what framework we choose to go with and which implementation would work the best. I'll have to compare both frameworks in detail and justify the choice of one over the other. (*Insert Big Brain Time meme here*)
- Things to consider: 
  - Ease of implementation and usage
  - Computational burden
  - Compatibility with chosen hardware
  - Ability to add more feature in the future
  - Error and standard deviation from the specific implementation on the specific hardware
  - Economical factors - choosing the cheapest one if both are comparable in results and error obtained?
  - Not sure, to be honest..... *sigh*

# Week 4 (12.05 to 18.05)
- Started working on setting up Jetson Nano and running PyVHR (5 hours)
- Ran into compatibility issues but managed to resolve them. Details in Notes section (3 hours)

## Next week tasks
- Successfully install PyVHR on Jetson and start working on the classical approaches for rPPG using the available datasets and models with PyVHR
- Make Jetson available through remote desktop client so anyone can access and work on it

## Project Timeline - Project Management (for presentation):
![image](https://github.com/androbaza/Xsight-heart-rate/blob/cb28ad9c6befb89b203a237ca5d1a1530ab5df91/resources/Haseeb/project_timeline.JPG)

### Problems faced:
- Biggest problem: Running PyVHR on Jestson Nano. There's no pre-built binaries/cmake files for PyVHR for Jetson Nano. Have to build it from source. Installing all the dependencies and making them work in tandem is time-consuming. Once this is done, implementation gets a lot fun and easy, hopefully!

## Notes
- Set up Jetson Nano with Jetpack 4.6 (Linux Ubuntu 18.04 Gnome flavor, CUDA 10.2, TensorRT 8.2.1, cuDNN 8.2.1, OpenCV 4.1.1, VisionWorks 1.6)
- Installed important prerequisite packages - Pip3, libhdf5, libopenblas, libblas, libfortran and others
- PyVHR makes use of Conda, but since Jetson Nano comes with Python 3.6, no Conda version is available for Aarch64 devices like Jetson Nano. So, had to install Archiconda, an alternative to Anaconda
- To recreate the installation: (Go line-by-line)
```bash
sudo apt update
sudo apt upgrade
sudo apt install python3-h5py libhdf5-serial-dev hdf5-tools python3-matplotlib python3-pip libopenblas-base libopenmpi-dev
wget https://github.com/Archiconda/build-tools/releases/download/0.2.3/Archiconda3-0.2.3-Linux-aarch64.sh
sudo sh Archiconda3-0.2.3-Linux-aarch64.sh
conda create -n NAME_OF_ENVIRONMENT python=3.6
```
- If there are any write permission issues,
```bash
sudo chown 1000:1000 /ARCHICONDA_DIRECTORY/
```
- and then recreate the environment

- Now, open bashrc file
```bash
gedit ~/.bashrc
```
- And append this
```bash
export OPENBLAS_CORETYPE=ARMV8
```
- Now install Pytorch after entering the newly created environment
```bash
conda activate NAME_OF_ENVIRONMENT
wget https://nvidia.box.com/shared/static/9eptse6jyly1ggt9axbja2yrmj6pbarc.whl -O torch-1.9.0-cp36-cp36m-linux_aarch64.whl
pip install torch-1.9.0-cp36-cp36m-linux_aarch64.whl
```
Once this is done, check your Pytorch installation by opening python3 interpreter and importing torch

Next TO-DO:
- Install Numba (here)
- Install Cupy and CuSignal
- Install Kaleido
- Install PyTables
- Install PyVHR and check if it works

# Week 5 (19.05 to 25.05)
- Continued installing the required dependencies to run PyVHR. Lots of problems faced, detailed in the 'problems faced' section (6 to 7 hours)
- Reinstalled Jetpack 4.6 (Jetson OS) and PyTorch on the new Jetson Nano we took (stole XD) from Johannes (2 hours). Why? This newer Nano had a USB-C input rather than the barrel jack for power, so makes it easier to directly connect a power bank as the power source. Hence, no need to think more about power delivery circuits and battery options for the project. This new Jetson also has a Noctua fan attached to the heatsink of the Nano, so cooling would also be taken care of, for now.
- Couldn't install remote desktop client to give access to Andrey since I was stuck with the PyVHR installation, so postponed it to next week

## Problems faced:
- 'Numba' dependency needs a different version of 'Conda' package manager. Archiconda doesn't work for some unknown reason. Tried multiple installation methods to make it work. Compiled from source using cmake too, but in vain (*insert crying face emoji*)
- Had to remove Archiconda to install Numba. What I totally forgot about - removing Conda also removed the virtual environment I installed PyTorch in. (*facepalm*)
- Installed the conda supported by Numba. Then recreated virtual environment to install Pytorch. What I didn't realize - I also mistakenly updated the Python version globablly and not just in the virtual env. And this is where I started to pull my hairs out. Everything installed perfectly, but Pytorch doesn't run any sample programs. After debugging and checking for more than an hour, I checked the local libraries and Python interpreter version. Then found out that it got upgraded somewhere down the line and wasn't supposed to be upgraded.
- Now, how to downgrade Python after the new libraries were hardcoded into the system? Either create a new environment with the older version within all that mess OR REINSTALL THE JETSON OS!! The latter was a lot simpler because at this point I had lost my patience 5 times over the weekend. 
- Cleared the SD card and reinstalled the Jetpack. Glad that I logged all my code and commands from the bash_history. Reinstalled all that stuff again, but this time being very careful with the Python version.
- Finally installed Numba, Cupy and CuSignal dependencies. Since I rolled back to the original python that came with Jetpack 4.6, CUDA libraries were intact and this made Cupy and CuSignal installation a lot easier. 

## Next week tasks
- Make Jetson available through remote desktop client so anyone can access and work on it
- Take the High-Res camera from the Xsight team and make it work with the Jetson
- Move the project files to the new Jetson
- Check the display usng the GPIO pins

## Notes
- (Will log my bash commands here later on to continue the 'Recreate Installation' from last week's log)

- **With all the logging and messy problems in Week 5, I think I missed updating my log here on Github. I honestly thought I logged it locally AND on Github, but clearly, I forgot doing it here on Github. Apologies!!**

# Week 6 (26.05 to 01.06)
- Almost done installing PyVHR - stuck at some compatibility issues. (2 hours) Would be hopefully cleared by this weekend. Logging EVERY SINGLE command so I can restore my progress until this checkpoint in case I mess up something in the future. 
- Tried enabling Remote desktop client - again lots of problems faced, detailed in the 'problems faced' section (3.5 to 4 hours - pointlessly wasted time)
- Started setting up the camera provided by Xsight team (1 hour) - read the datasheet and application notes
- New Jetson up and running with the copied project files and dependencies (1 hour)

## Problems faced:
- Remote desktop in Jetson is not straight-forward due to its processor (ARMv8) and network architecture. No teamviewer or Anydesk support for Jetson Nano. Found a few alternatives - Remmina desktop sharing, VNC desktop sharing and No Machine desktop sharing.
- Remmina is not available for Windows and Mac. Only Linux systems. So we would need to have a laptop running Ubuntu to use Remmina
- Using VNC on Jetson needed a lot of command lines and a some networking knowledge. Not good at that. I'm an introvert, so networking is not really my strong suit. Bad joke, but seriously, I'm not good with networking.
- NoMachine was a good and fairly easy-to-implement alternative - or so I thought. After somehow weaving my way through the nuances of remote desktop connection, compatibility issues, desktop environment errors and losing my patience 3 more times, I was able to run desktop sharing, but only on the Local network or LAN. Global network access will need some adjustments on my router like port-forwarding or something or maybe I should look more into the documentation from NoMachine website to make it work.
- Discussed this with Andrey and unanimously decided it is a waste of time. Better to just make it physically available somewhere instead of breaking our heads with remote networks. Maybe I'll ask Johannes for some help with this. He might have used remote desktop on Nano at some point with his previous projects.

## Next week tasks
- Make Jetson available for Andrey, either by setting it up in Lichtwerkstatt or somehow magically making remote desktop work!
- Get the PyVHR framework up and running
- Get the camera running so Andrey can test video-capture pipeline
- Get the small screen connected to the Jetson GPIO pins and include it as a second display in the Jetson configuration or write a small Python script? Don't know yet.

## Notes
- (Again, will log my bash commands here later on to continue the 'Recreate Installation' from last week's log)
- **Once again, with all the logging and messy problems in Week 5, I think I missed updating my log here on Github. I honestly thought I logged it locally AND on Github, but clearly, I forgot doing it here on Github. Apologies!!**

# Week 7 (02.06 to 08.06)
- In the process of setting up the Allied Vision camera with the new Jetson. Facing some issues, will fix them by next week possibly. If this takes too much time, I shall ask for help from XSight team (3 to 4h)
- PyVHR almost done. Will hopefully start working with the camera and PyVHR by the next week.
- Didn't put in a lot of work this week since I had put a lot of time on this in the last two weeks. Needed to focus some time on other courses.

## Next week tasks
- Set up the new Jetson at Lichtwerkstatt
- Get the PyVHR framework up and running with the camera
- Set up the mini display to work with Jetson GPIO.

# Week 8 (09.06 to 05.06)

![Logs](https://github.com/androbaza/Xsight-heart-rate/blob/51ae68385d27b7b830f5b3130e17f253fc52355b/resources/etc/empty.JPG)
