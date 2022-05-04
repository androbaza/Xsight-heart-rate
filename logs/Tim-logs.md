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
