# **aud.io**
GAN-derived system for converting accents


<img src="https://github.com/sachaker/aud.io/blob/master/data/img/spectrogram.png" width="50%">
  

## What's new

<img src="https://github.com/sachaker/aud.io/blob/master/data/img/accents.png" width="50%">

> ###### Two clusters for 3,000 voices... I'm sure you can guess what the groups are

• built algorithm to scrape files from accent database (~3k files, ~300 accents)

• projected voices into a feature space in which voices cluster

• trained MelGAN-VC model

• found 6 other models to conduct voice transfer 

• found 8 alternative training datasets

## Getting started

### Installation

```$ git clone https://github.com/sachaker/aud.io```

### Run program

```$ pip install -r requirements.txt```

```$ python main.py```

## Authors
- **Sacha McElligott** — [email](mailto:sacha@nyu.edusubject=[GitHub]%20Source%20Han%20Sans), [LinkedIn](https://www.linkedin.com/in/sacha-mcelligott-136a78a9/), [website](https://sachaker.github.io)

## Acknowledgements
- [Marco Pasini](https://towardsdatascience.com/@marco.pasini)

## Resources
[MelGAN-VC paper](https://arxiv.org/pdf/1910.03713.pdf) | [Accent archive 1](http://accent.gmu.edu/soundtracks/) | [Accent archive 2](http://festvox.org/cmu_arctic/cmu_arctic/)
--- | --- | ---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
