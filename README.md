# Urban Planning Tool: Integrating Public Transportation and Air Quality Data

## Overview
This tool integrates public transportation usage data with air quality metrics to assist urban planners in making informed decisions that enhance infrastructure and public health. The tool allows users to visualize transportation patterns alongside air quality data, facilitating the assessment of environmental impacts and the optimization of transit systems.

## Prerequisites
- Python 3.x
- Pandas
- Matplotlib
- JSON data handling knowledge

## Installation
1. Ensure you have Python 3.x installed on your machine.
2. Install the required packages using pip:
   bash
   pip install pandas matplotlib
   

## Usage
1. Download the datasets:
   - Public Transportation Usage: `Public_Transportation_Usage.csv`
   - Air Quality Data: `Air_Quality_Data.json`

2. Place the datasets in the same directory as your script.

3. Run the script:
   bash
   python integrate_datasets.py
   

4. The script will output a scatter plot visualizing the correlation between peak transportation usage and air quality metrics (PM2.5 and NO2 levels).

5. Review the printed correlation analysis to understand the relationship between transportation usage and air quality.

## Key Features
- **Data Integration**: Merges public transportation and air quality datasets for comprehensive analysis.
- **Visualization**: Displays correlations between transportation usage and pollutant levels in an easy-to-understand scatter plot.
- **Insights Generation**: Provides correlation analysis to inform urban planning decisions.

## Contribution
Contributions are welcome! Please submit a pull request with your changes or open an issue to discuss improvements.

## License
This project is licensed under the MIT License.
