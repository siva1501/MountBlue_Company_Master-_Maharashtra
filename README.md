# Company Master – Maharashtra

## Project Description

This project analyzes company registration data from Maharashtra.

The project uses Python and CSV files to analyze company registrations based on:

* Registration year
* District
* Business activity
* Authorized capital

The results are displayed as both **console output** and **bar plots**.

## Project Structure

Company_Master_Maharashtra/
│
├── data/
│   ├── company_master_data_2026-09-12.csv
│   └── zip_code_MH.csv
│
├── problems/
│   ├── 1_*.py
│   ├── 2_company_registration_by_year.py
│   ├── 3_company_registration_by_district.py
│   ├── 4_grouped_bar_plot.py
│   └── ...
│
├── bar_plots.py
├── requirements.txt
├── README.md
└── .gitignore


## Technologies Used

* Python
* CSV module
* Matplotlib
* Git
* GitHub

## Setup

### 1. Clone the Repository

bash
git clone https://github.com/siva1501/MountBlue_Company_Master-_Maharashtra.git


### 2. Open the Project Folder

bash
cd Company_Master_Maharashtra


### 3. Create a Virtual Environment
bash
python -m venv Company_Master_Maharashtra


### 4. Activate the Virtual Environment

For Windows PowerShell:

powershell
Company_Master_Maharashtra\Scripts\activate


### 5. Install Dependencies

powershell
pip install -r requirements.txt


## Run the Programs

Run each problem from the project root.

### Problem 2 - Company Registration by Year

powershell
python problems\2_company_registration_by_year.py


### Problem 3 - Company Registration in 2015 by District

powershell
python problems\3_company_registration_by_district.py


### Problem 4 - Grouped Bar Plot

powershell
python problems\4_grouped_bar_plot.py


Each program prints the result in the terminal and displays the corresponding plot.

## Common Plotting

The project uses a common `bar_plots.py` file for plotting.

It contains:

* `bar_plot()` for normal bar charts
* `grouped_bar_plot()` for grouped bar charts

This avoids repeating Matplotlib plotting code in every problem.

## Data Files

### Company Data

`company_master_data_2026-09-12.csv` contains company information such as:

* Company Name
* Company Registration Date
* Company Category
* Company Class
* Authorized Capital
* Paidup Capital
* Company Address
* Pin Code
* Company State
* Company Status
* Company Industrial Classification

### PIN Code Data

`zip_code_MH.csv` contains Maharashtra PIN code information used to identify the district from a PIN code.

## Analysis Problems

The project includes analysis such as:

1. Company registration analysis
2. Company registration by year
3. Company registration in 2015 by district
4. Company registration by business activity for the last 10 years
5. Companies grouped by authorized capital

## Code Quality

The project follows Python coding standards and is checked using linting tools such as `flake8` and `pylint`.

## Author

Sivashankara Reddy

## Repository

GitHub:

https://github.com/siva1501/MountBlue_Company_Master-_Maharashtra.git
