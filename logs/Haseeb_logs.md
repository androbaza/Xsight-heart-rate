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

![Logs](https://github.com/androbaza/Xsight-heart-rate/blob/51ae68385d27b7b830f5b3130e17f253fc52355b/resources/etc/empty.JPG)
