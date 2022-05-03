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
* Read papers, presenting latest methods in heart rate estimation (3 hours): 
  * Self-supervised Representation Learning Framework for Remote Physiological Measurement Using Spatiotemporal Augmentation Loss https://arxiv.org/pdf/2107.07695v2.pdf
    * comment: self-supervised method is not deployable.
  * Instantaneous Physiological Estimation using Video Transformers https://arxiv.org/pdf/2202.12368v1.pdf
    * comment: promising model, rgb input. plan to test this model next.
  * Beat-to-Beat Cardiac Pulse Rate Measurement From Video https://openaccess.thecvf.com/content/ICCV2021W/V4V/papers/Hill_Beat-To-Beat_Cardiac_Pulse_Rate_Measurement_From_Video_ICCVW_2021_paper.pdf
    * comment: great paper. no code released. will contact authors.
