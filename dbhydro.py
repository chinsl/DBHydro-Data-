import requests
import pandas as pd
import subprocess


# Base URL for DBHYDRO water quality data
# Source: Page 84 of the DBHYDRO User's Guide
base_URL = "http://my.sfwmd.gov/dbhydroplsql/water_quality_data.report_full"

test_numbers = [
24,    # PHOSPHATE, ACID HYDRO, P
955,   # NITROGEN, AMMONIA AS NH4
61,    # CHLOROPHYLL-A
112,   # CHLOROPHYLL-A, CORRECTED
1000,  # CHLOROPHYLL-A, DRY WEIGHT
178,   # CHLOROPHYLL-A, SALINE
62,    # CHLOROPHYLL-B
113,   # CHLOROPHYLL-C
179,   # CHLOROPHYLL-A(LC)
180,   # CHLOROPHYLL-B (LC)
1020,  # CHLOROPHYLL-A ug/L -FIELD
8,     # DISSOLVED OXYGEN
83,    # NITROGEN, DISS. ORGANIC
4,     # DISSOLVED OXYGEN SATURATION
936,   # NITROGEN - N2
961,   # NITROGEN - N2
19,    # NITRITE-N
78,    # NITRATE-N
18,    # NITRATE+NITRITE-N
114,   # NITRATE+NITRITE-N
23,    # PHOSPHATE, ORTHO AS P
98,    # SALINITY
294,   # NITROGEN, TOTAL IN SOLIDS
26,    # PHOSPHATE, DISSOLVED AS P
185,   # TOTAL NITROGEN
81,    # NITROGEN, TOTAL ORGANIC
25,    # PHOSPHATE, TOTAL AS P
237,    # PHOSPHATE, TOT REACTIVE P
7,     # TEMPERATURE IN DEGREES CELCIUS
17,    # PH, LAB
10,    # PH, FIELD 
14,    # SP CONDUCTIVITY, LAB
9      # SP CONDUCTIVITY, FIELD 
]

test_query = f"({', '.join(map(str, test_numbers))})"

# print(test_query)

# Query parameters dictionary
# filter before 01/01/23 for select stations and tests
query_params = {

    "v_where_clause": f"""where station_id in (
        'C44SC24', 'C44SC23', 'C44SC19', 'C44SC14', 'C44IA1A', 'C44SC5', 'C44SC2', 'C44S80', 
        'C23S48', 'C24S49', 'SE+01', 'SE+02', 'SE+03', 'SE+06', 'SE+08B', 'SE+09', 'SE+11', 'SE+12', 
        'SE+13', 'S153', 'S404', 'S417E', 'S415E', 'HR1', 'GORDYRD', 'S308C'
    ) 
    
    and test_number in {test_query}

    and date_collected < '01-JAN-2023'
    and date_collected > '01-JAN-1993'""",     
    
    "v_target_code": "file_csv",  # CSV format for easy processing

    "v_exc_flagged": "Y",         # exclude flagged data

    "v_exc_qc": "Y"               # exclude field QCs
}

def download_dbhydro_data(base_url, params, output_file):
    """
    Retrieves water quality data from DBHYDRO and saves it as CSV.

    :base_url: DBHYDRO API endpoint
    :params: query parameters
    :output_file: output file name
    """
    response = requests.get(base_url, params=query_params)      #retrieve data based on URL+parameters
    
    if response.status_code == 200:
        with open(output_file, "wb") as file:                   #open new file in "write binary"
            file.write(response.content)                        #write raw data into output file
        print(f"Data successfully downloaded: {output_file}")

        # Load and display data
        df = pd.read_csv(output_file, low_memory=False)
        return df
    else:
        print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")
        return None

# Run the function and save to a CSV file
dataframe = download_dbhydro_data(base_URL, query_params, "/Users/metta/Documents/Research/extracted_dbhydro_data.csv")

file_path = "/Users/metta/Documents/Research/extracted_dbhydro_data.csv"  
subprocess.run(["open", file_path])