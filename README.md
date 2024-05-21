# Streamflow Data Processor

This project processes streamflow data from an Excel file, chunks the data into specified intervals, and generates plots for each chunk. The processed data and plots are saved into a specified directory.

## Features

- Load and process streamflow data from an Excel file.
- Chunk the data into intervals specified by the user.
- Save each chunk as an Excel file.
- Generate and save plots for each chunk.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/damilola-yinusa/streamflow-data-processor.git

Navigate to the project directory:

cd streamflow-data-processor

Install the required dependencies:

pip install -r requirements.txt


Usage
Place your streamflow data Excel file in the project directory.
Update the file_path variable in the script to point to your data file.
Run the script:

python streamflow_data_processor.py

File Structure
streamflow_data_processor.py: The main script to process the data.
requirements.txt: The list of dependencies required for the project.
README.md: This file.
Output
The processed data chunks and their corresponding plots are saved in the specified output directory.

License
This project is licensed under the MIT License - see the LICENSE file for details.
