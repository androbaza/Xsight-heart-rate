## Week 1
* Create group chat
* Create github repo to track code/logs
* Visit [LASER World of PHOTONICS](https://world-of-photonics.com/en/) exhibition in Munich, research currently available sensors related to the project (3 hours) -- suprisingly, nothing of close resemblence was discovered. Biophotonics stands number was frustratingly low 🥺. 
* Research how the remote heart rate estimation is done - photoplethysmography (Remote-PPG) (~1 hour). 
* Explore the [state-of-the-art algrithms list](https://paperswithcode.com/task/heart-rate-estimation) (2 hours so far, in progress)
  * [Latest method](https://paperswithcode.com/paper/efficient-deep-learning-based-estimation-of). Uses images from frontal smartphone camera for heartate and SpO2 estimation. No code released yet. Will contact the paper authors.
  * [Deployable method](https://github.com/terbed/Deep-rPPG) - coulb be run on Nvidia Jetson nano (have to check performance).

## Week 2
* Contacted Taha Samavati regarding code for [method](https://paperswithcode.com/paper/efficient-deep-learning-based-estimation-of) from previous week. No answer so far.
* Read papers, presenting latest methods in heart rate estimation (5 hours): 
  * [Self-supervised Representation Learning Framework for Remote Physiological Measurement Using Spatiotemporal Augmentation Loss](https://arxiv.org/pdf/2107.07695v2.pdf)
    * comment: self-supervised method is not deployable.
  * [Instantaneous Physiological Estimation using Video Transformers](https://arxiv.org/pdf/2202.12368v1.pdf)
    * comment: promising model, rgb input. plan to test this model next. [repo](https://github.com/revanurambareesh/instantaneous_transformer).
  * [Beat-to-Beat Cardiac Pulse Rate Measurement From Video](https://openaccess.thecvf.com/content/ICCV2021W/V4V/papers/Hill_Beat-To-Beat_Cardiac_Pulse_Rate_Measurement_From_Video_ICCVW_2021_paper.pdf)
    * comment: method participated in V4V challenge in Fall 21. no code released. will contact authors.
  * [Automatic region-based heart rate measurement using remote
photoplethysmography](https://openaccess.thecvf.com/content/ICCV2021W/V4V/papers/Kossack_Automatic_Region-Based_Heart_Rate_Measurement_Using_Remote_Photoplethysmography_ICCVW_2021_paper.pdf)
    * comment: method participated in V4V challenge in Fall 21. MAE 9.37 beats/min, faster inference. 
  * [A Review of Deep Learning-Based Contactless Heart Rate
Measurement Methods](https://www.mdpi.com/1424-8220/21/11/3719/pdf).
    * comment: recent review paper. useful to understand the current field.
