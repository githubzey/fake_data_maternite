# Fake Data Maternité

This repository contains scripts and configuration files for generating fake data related to French maternity services.

## Overview

- **`fake_data_generator.py`**: This script includes a function to generate fake data for a single year as well as code to generate data for multiple years as specified. The generated data simulates records commonly found in French maternity services.
  
- **`config.yaml`**: This configuration file defines the columns that require specific lists of values and includes constant values for other columns used in the data generation process.

- **`parse.py`**: This script is used to parse the generated data, specifically extracting the first 192 characters from each record.

## Usage

To generate fake data, adjust the configurations in `config.yaml` as needed, and then run `fake_data_generator.py`. If you need to parse the generated data, use the `parse.py` script.
