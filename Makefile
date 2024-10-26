.PHONY: prereqs build clean test test_preprocessing run_all docker


PREPROCESS_DIR=preprocessing
PROCESS_DIR=processing
POSTPROCESS_DIR=postprocessing

# Install Python dependencies
prereqs:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

# Build executables
build:
	@echo "Building preprocess"
	g++ -std=c++17 -o preprocessing.o $(PREPROCESS_DIR)/preprocessing.cpp

# Clean binary files
clean:
	rm preprocessing.o

# Run tests
test:
	@echo "Running preprocessing tests..."
	python -m unittest $(PREPROCESS_DIR)/tests/test_preprocessing.py
	@echo "Running processing tests..."
	python -m unittest $(PROCESS_DIR)/tests/test_processing.py
	@echo "Running postprocessing tests..."
	python -m unittest $(POSTPROCESS_DIR)/tests/test_postprocessing.py

test_preprocessing:
	@echo "Running preprocessing tests..."
	python -m unittest $(PREPROCESS_DIR)/tests/test_preprocessing.py


run_all:
	@echo "Running preprocessing..."
	#python preprocessing/preprocessing.py
	./preprocessing.o
	@echo "Running processing..."
	python $(PROCESS_DIR)/processing.py
	@echo "Running postprocessing..."
	python $(POSTPROCESS_DIR)/postprocessing.py
	@echo "All steps completed."
