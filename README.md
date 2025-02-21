# Purpose

**dbhydro.py** is script that downloads csv files with water quality data from South Florida Water Management District's DBHydro database. Required inputs are station IDs and sample test numbers.

# Summary

### Inputs

The web API used to request water quality data is defined as *base_URL* (line 8). Sample test numbers are stored in an array called *test_stations* (line 10). Each element is then joined as a string for the *query_params* dictionary (line 46), which is later used to construct the specific web API URL with appropriate paramater definitions. Station IDs are also stored in this dictionary. 

### Download Mechanism

The function download_dbhydro_data takes the base URL, parameters, and output file path as inputs and returns a dataframe with the requested data. It is called and returned into *dataframe* (line 95). This is where the download file path should be edited.

Finally, the *subprocess* library is used to automatically open the file at the specified path stored in *file_path* (line 98). This may be commented out if undesired.

# Instructions

### Define Sample Test Numbers

Edit the *test_numbers* array (line 8) to include the appropriate water quality sample tests. Sample test numbers can be referenced at [this](https://my.sfwmd.gov/dbhydroplsql/show_dbkey_info.show_data_type_info) DBHydro metadata webpage.

```
test_numbers = [
24,    # PHOSPHATE, ACID HYDRO, P
955,   # NITROGEN, AMMONIA AS NH4
61,    # CHLOROPHYLL-A

...

10,    # PH, FIELD 
14,    # SP CONDUCTIVITY, LAB
9      # SP CONDUCTIVITY, FIELD 
]
```

### Define Station IDs

To select stations, edit the *"v_where_clause"* key of the *query_params* dictionary (line 52) to include station IDs of interest:

```
query_params = {

    "v_where_clause": f"""where station_id in (
        'C44SC24', 'C44SC23', 'C44SC19', 'C44SC14', 'C44IA1A', 'C44SC5', 'C44SC2', 'C44S80', 
        'C23S48', 'C24S49', 'SE+01', 'SE+02', 'SE+03', 'SE+06', 'SE+08B', 'SE+09', 'SE+11', 'SE+12', 
        'SE+13', 'S153', 'S404', 'S417E', 'S415E', 'HR1', 'GORDYRD', 'S308C'
    ) 

...

}
```

### Define Timespan

The time span can be selected within the *and data_collected* parameter with the DD-MON-YYYY format:

```
query_params = {

    and date_collected < '01-JAN-2023'
    and date_collected > '01-JAN-1993'""",  

...

}
```
### Define File Save Path

Edit the *output_file* parameter of the *download_dbhydro_data* function to specify the appropriate file save path:

```
dataframe = download_dbhydro_data(base_URL, query_params, "/Users/metta/Documents/Research/extracted_dbhydro_data.csv")
```
# Resources

DBHydro documentation can be found [here](https://www.sfwmd.gov/sites/default/files/dbhydro_browser_user_documentation.pdf).

The DBHydro browser web page can be found [here](https://my.sfwmd.gov/dbhydroplsql/show_dbkey_info.main_menu).








