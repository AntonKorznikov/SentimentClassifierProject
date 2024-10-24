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
- Python 3.8+
- Git

## Usage

### Using Makefile

1. **Install Dependencies**
```bash
make prereqs
```
2. **Build Executables**
```bash
make build
```

3. **Run Tests**
```bash
make test
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
- `scripts/`: Utility scripts for running the entire pipeline.
