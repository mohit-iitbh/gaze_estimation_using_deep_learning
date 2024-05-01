# Gaze Estimation with Deep Learning

This project implements a deep learning model to predict eye region landmarks and gaze direction.
The model is trained on a set of computer generated eye images synthesized with UnityEyes [1]. This work is heavily based on [2] but with some key modifications. 
This model achieves ~14% mean angular error on the MPIIGaze evaluation set after training on UnityEyes alone.

### Demo Video

[![Watch the video](static/ge_screenshot.png)](https://drive.google.com/open?id=1WUUmd4quXq_YA5ANWDoUxqFGgguE_QJi)

### References

1. https://www.cl.cam.ac.uk/research/rainbow/projects/unityeyes/
2. https://github.com/swook/GazeML
3. https://github.com/princeton-vl/pytorch_stacked_hourglass
