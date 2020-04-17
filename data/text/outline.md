# Project Outline

**Project name:** aud.io

**Project goal:** To build a modular system that can transfer accents or voice styles to users. The final product will be an iOS app or web interface in which the user uploads a video of themselves, selects an accent or voice style (e.g. Homer Simpson), and the output is the same video but speaking with a new voice.

## Broad objectives

- Successfully transfer specific voice styles from videos (must be high quality output)
- Deploy system via an iOS app or web interface

## Checklist for project completion

- [ ]  I must find the final product satisfactory
- [ ]  Timeline must be reasonable and agreed upon beforehand
- [ ]  System must allow for voice style transfer of **new** and **unseen** voice styles
- [ ]  Interface must be simple and easy-to-use 
- [ ]  Source code must be well commented and fully functional
- [ ]  Voice style transfer must be quick (on the order of seconds)
- [ ]  There must be no commercial or legal conflicts in the resources ultimately used

## Loose roadmap
1. Determine model
2. Determine training set
3. Successfully [project voices into feature spaces](https://github.com/resemble-ai/Resemblyzer) and show distinct clusters (proof-of-concept)
4. Use vector transformation to convert voices
5. Build app to allow custom uploads (testing should be fast, training to allow for a new voice style will be long)
6. Test it out on users of many voice types

## Relevant links
#### GitHub repos
- https://github.com/CorentinJ/Real-Time-Voice-Cloning
- https://github.com/resemble-ai/Resemblyzer
- https://github.com/andabi/deep-voice-conversion
- https://github.com/marcoppasini/MelGAN-VC

#### Language datasets
- https://keithito.com/LJ-Speech-Dataset/
- https://www.caito.de/2019/01/the-m-ailabs-speech-dataset/
- https://accent.gmu.edu/
- https://catalog.ldc.upenn.edu/LDC93S1
- https://psi.engr.tamu.edu/l2-arctic-corpus/ (commercial restrictions)
- http://festvox.org/cmu_arctic/cmu_arctic/packed/ (commercial restrictions)

#### Other
- https://www.youtube.com/watch?v=-O_hYhToKoA
- https://www.youtube.com/watch?v=gVehTbi6Ipc
- https://www.resemble.ai
