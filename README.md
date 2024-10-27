# SentimentClassifier

## Overview

**SentimentClassifier** is a lightweight neural network tool designed to perform sentiment analysis on textual data. It highlights the sentiment of input texts using a pretrained model from HuggingFace. The project includes preprocessing, processing, and postprocessing steps to deliver human-presentable results.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Using Makefile](#using-makefile)
  - [Using Docker](#using-docker)
- [Examples](#examples)
- [Testing](#testing)
- [Project Structure](#project-structure)

## Installation

### Requirements

- Make
- Docker
- Python 3.9+

## Usage

### Cloning repository

```bash
git clone https://github.com/AntonKorznikov/SentimentClassifierProject.git
```
### Using Makefile

1. **Install Dependencies**
```bash
make prereqs
```
2. **Build Executables**
```bash
make build
```
3. **Clean Executables**
```bash
make clean
```
4. **Run Tests**
```bash
make test
```
5. **Run Project**
```bash
make run_all
```

### Using Docker

1. **Build Docker Image**
```bash
docker build -t sentimentclassifier:latest .
```

2. **Run Docker Container**
```bash
docker run -v $(pwd)/examples/input_raw:/input_raw -v $(pwd)/examples/output:/output sentimentclassifier:latest
```

## Examples

Sample input files are provided in the `examples/input_raw/` directory. After running the preprocessing, processing, and postprocessing steps, the results can be found in the `examples/output/` directory.

example of input_raw/sample_input.txt :
```
I love this product!
This service is terrible.
The quality is just okay.
Absolutely fantastic experience!
Not worth the investment at all.
```

example of output/sample_input.txt :
```
Sentiment: POSITIVE, Score: 0.9998855590820312
Sentiment: NEGATIVE, Score: 0.999573290348053
Sentiment: POSITIVE, Score: 0.9998542070388794
Sentiment: POSITIVE, Score: 0.9998812675476074
Sentiment: NEGATIVE, Score: 0.999803364276886
```

## Testing

Run all tests using the Makefile:
```bash
make test
```

## Project Structure

- `preprocessing/`: Contains scripts and tests for data preprocessing.
- `processing/`: Contains scripts and tests for running the sentiment analysis model.
- `postprocessing/`: Contains scripts and tests for processing the model's output.
- `examples/`: Contains example input and output files.
