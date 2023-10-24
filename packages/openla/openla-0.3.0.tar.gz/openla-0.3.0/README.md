# OpenLA: open-source library for e-book log analysis 

[![PyPI Latest Release](https://img.shields.io/pypi/v/OpenLA.svg)](https://pypi.org/project/OpenLA/)
[![Coverage](https://limu.ait.kyushu-u.ac.jp/~openLA/_images/coverage.svg)](https://github.com/limu-research/openla/)
[![Package Status](https://img.shields.io/pypi/status/OpenLA.svg)](https://pypi.org/project/OpenLA/)
[![License](https://img.shields.io/pypi/l/OpenLA.svg)](https://github.com/limu-research/openla/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/personalized-badge/OpenLA?period=month&units=international_system&left_color=black&right_color=orange&left_text=PyPI%20downloads%20per%20month)](https://pepy.tech/project/OpenLA)
[![Documentation](https://img.shields.io/badge/api-reference-blue.svg)](https://limu.ait.kyushu-u.ac.jp/~openLA/)

## Introduction

OpenLA is an open-source library for e-book log analysis.

This Python library helps reduce redundant development when preprocessing e-book logs:
calculating reading times for each learner, counting up operations, page-wise summary of student behavior, etc.

![OpenLA concept](https://github.com/limu-research/openla/raw/main/source/images/OpenLA_concept.jpg?openla=2022-04-12)

## API concept

Four preprocessing processes are essential and common in e-book log analysis: getting course information, converting the log into a form suitable for analysis, extracting the required information, and visualizing the data.

In order to improve efficiency and reduce reiteration in these processes, OpenLA provides the corresponding four modules: Course Information, Data Conversion, Data Extraction, and Data Visualization.

![Preprocessing flow](https://github.com/limu-research/openla/raw/main/source/images/OpenLA_structure.jpg?openla=2022-04-12)

## Installation

OpenLA is [available on PyPi](https://pypi.org/project/OpenLA/). You can install it with `pip`.

```sh
pip install OpenLA
```

OpenLA works on python 3.7, 3.8, 3.9 and 3.10.

Below are the versions of OpenLA's main dependencies we use for testing, but you probably do not need to worry about this.

- python 3.7: matplotlib 3.5.2, numpy 1.21.6, pandas 1.3.5
- python 3.8 or newer: matplotlib 3.5.2, numpy 1.22.3, pandas 1.4.2

## Datasets for OpenLA

The dataset used in this library has the same structure as the open source ones used to conduct [Data Challenge Workshops in LAK19 and LAK20](https://sites.google.com/view/lak20datachallenge).

We target [BookRoll](https://www.let.media.kyoto-u.ac.jp/en/project/digital-teaching-material-delivery-system-bookroll/) logs, but logs from other systems can be adapted.

The dataset may include up to four types of files.

### Course\_#\_EventStream.csv

- Data of the logged activity data from learners' interactions with the BookRoll system
- Columns: `userid`, `contentsid`, `operationname`, `pageno`, `marker`, `memo_length`, `devicecode`, and `eventtime`

### Course\_#\_LectureMaterial.csv

- Information about the length of the lecture materials used
- Columns: `lecture`, `contentsid`, and `pages`

### Course\_#\_LectureTIme.csv

- Information about the schedule of the lectures
- Columns: `lecture`, `starttime`, and `endtime`

### Course\_#\_QuizScore.csv

- Data on the final score for each student
- Columns: `userid` and `score`

Note: from version 0.2.1, OpenLA can treat grading data, which was not present in the LAK19 and LAK20 datasets.

### Course\_#\_GradePoint.csv

- Data on the final grade for each student
- Columns: `userid` and `grade`

Where `#` is the course id. BookRoll is an e-book system to record learning activities.

If you need a sample dataset, please contact openla@limu.ait.kyushu-u.ac.jp .

## Documentation

[Read the docs](https://limu.ait.kyushu-u.ac.jp/~openLA/) for detailed information about all the modules, and for code examples.

For more information about BookRoll and the learning analytics platform on which the data was collected, please refer to the following:

- Brendan Flanagan, Hiroaki Ogata, Integration of Learning Analytics Research and Production Systems While Protecting Privacy, Proceedings of the 25th International Conference on Computers in Education (ICCE2017), pp.333-338, 2017.
- Hiroaki Ogata, Misato Oi, Kousuke Mohri, Fumiya Okubo, Atsushi Shimada, Masanori Yamada, Jingyun Wang, and Sachio Hirokawa, Learning Analytics for E-Book-Based Educational Big Data in Higher Education, In Smart Sensors at the IoT Frontier, pp.327-350, Springer, Cham, 2017.
