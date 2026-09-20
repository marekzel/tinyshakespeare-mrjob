# TinyShakespeare MapReduce & Analysis

A lightweight Big Data prototyping project that processes Shakespeare's vocabulary using an Apache Hadoop MapReduce simulation in Python and generates insights using Pandas and Plotly.

## Project Structure

*   `process_tshk.py` - The MapReduce job powered by `mrjob`. It filters out empty lines and character scene headers (e.g., `MARCIUS:`), counts word frequencies, and outputs raw CSV data.
*   `analyze_tshk.py` - The data analysis script that reads the generated CSV, applies text metrics, and displays an interactive Plotly scatter plot mapping Word Length vs. Usage Frequency.

## Dataset Credits

This project uses the **tinyshakespeare** dataset, which consists of 1 Megabyte of clean text from Shakespeare's plays. 

Special thanks to **Andrej Karpathy** for collecting and making this dataset widely accessible. The original file was obtained from his repository:
*   [karpathy/char-rnn (GitHub)](https://github.com)

## Prerequisites

Make sure you have Python 3.11+ installed. Install the required dependencies:

```bash
pip install mrjob pandas plotly setuptools
```

> *Note: `setuptools` is required on newer Python versions to provide the `distutils` module fallback used by `mrjob`.*

## How to Run

### 1. Run the MapReduce Job
Execute the MapReduce script locally against the `tinyshakespeare.txt` file and redirect the output to a CSV file named `out.csv`:

```bash
python process_mr.py tinyshakespeare.txt > out.csv
```

### 2. Analyze and Visualize the Data
Run the analysis script to load the data into a Pandas DataFrame and view the interactive Plotly data visualization:

```bash
python analyze_tshk.py
```

## Data Output
The generated `out.csv` uses a raw layout format suitable for quick database imports and instant Pandas parsing:
```csv
word,count
```
