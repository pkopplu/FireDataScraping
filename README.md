Canada is burning. I ventured out to gather the data necessary for analysing the current wildfires. Canadian interagency forest fire centre(CIFFC) has done a brilliant job at showcasing the data on their website: https://ciffc.net/. I wondered if I could I scrape the data? and checked their robots.txt file for any restrictions. Thankfully they didnt restrict any part of their website for scraping/crawling.
Then I opened their website and inspected their html and got the necessary APIs needed to get the neessary data. The data was in a semi structured form: JSON. I used Pandas to convert this nested Json data into a structured table format and stored it in the form of excel sheets. You can access these files in the Datasets folder.

The aim of the project is to analyse the wildfires by Province, both historically and for the present year:2023 as CIFFC presents only the nation-wide view of wildfires.

The Dataset folder consists of two files:
1. Summary - This file consists of the fire details by province in the year 2023: consists of 1 Fact table and 4 dimension tables
    - fact_summary table -  captures the  facts : numer of fires and the area burned
    - dim_wildfireStatus -  explains the Status of the wildfire
    - dim_wildfire_Response - explains the response to the wildfire
    - dim_agency - explains the agencies/provinces managing the wildfires
    - dim_province_forest - gives the details about the forest area, reserved and unreserved forests in each province
2. history - This dataset consists of the historical record of the number of fires and the area burned by province since 1983 to the present day

Here is the ERD diagram for the above mentioned facts and dimensions in the Power BI desktop:

![image](https://github.com/pkopplu/FireDataScraping/assets/134582838/4d1953b9-bed7-4648-86ad-d4b148c40075)

I have merged the data from dim_agency and dim_province_forest into a single dim_provinces table using Power Query. I am trying to setup my datamodel so that it emulates a STAR schema. This is a live data feed which is being updated regularly on a daily basis, so its best if one can schedule refresh periodically.


References:
1. https://cwfis.cfs.nrcan.gc.ca/downloads/activefires/
2. https://ciffc.net/
