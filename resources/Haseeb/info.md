# Folder details

This folder is for dropping any resource I find interesting or useful before I organize it into different folders. My ongoing effort would also be recorded here sometimes. Digital version of desk clutter, basically.

## USS Enterprise, Captain's log, April 28th, 2022, 18:30: 
- Doppler radar looks fire! Nice paper I found [here](A_Review_on_Recent_Advances_in_Doppler_Radar_Sensors_for_Noncontact_Healthcare_Monitoring.pdf)
- [Doppler radar chip](https://www.seeedstudio.com/Grove-Doppler-Radar-BGT24LTR11-p-4572.html) Can be used with Arduino. Available on Mouser for 61 EUR. Need to check more into it. 

## USS Enterprise, Captain's log, May 13th, 2022, 19:10: 
- Started working on Jetson Nano - PyVHR. Here goes nothing................

Installed Pip3
Installed Archiconda for Jetson nano, since no Anaconda with Jetpack 4.6
To recreate the installation
```bash
sudo apt update
sudo apt upgrade
sudo apt install python3-h5py libhdf5-serial-dev hdf5-tools python3-matplotlib python3-pip libopenblas-base libopenmpi-dev
wget https://github.com/Archiconda/build-tools/releases/download/0.2.3/Archiconda3-0.2.3-Linux-aarch64.sh
sudo sh Archiconda3-0.2.3-Linux-aarch64.sh
conda create -n xsight python=3.6
```
