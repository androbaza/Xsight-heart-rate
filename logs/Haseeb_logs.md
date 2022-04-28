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
- Need to find a way to workaround the effect of Melanin on heart rate estimation. Don't want the device to be racist, heh.
