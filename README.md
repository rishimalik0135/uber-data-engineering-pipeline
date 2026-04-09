# Uber NYC Taxi Data Engineering Pipeline

## Project Overview
End-to-end data engineering pipeline built on Google Cloud Platform to analyse 
100K+ NYC taxi trips. Designed to surface fare patterns across rate codes, 
payment types, and pickup locations.

## Architecture
Raw Data (CSV) → Google Cloud Storage → Mage AI (GCE) → BigQuery → Looker Studio
![architecture](https://github.com/user-attachments/assets/f0b2cc10-2693-47e2-ba99-5a0b3d72948e)

## Dataset Used
TLC Trip Record Data Yellow and green taxi trip records include fields capturing pick-up and drop-off dates/times, pick-up and drop-off locations, trip distances, itemized fares, rate types, payment types, and driver-reported passenger counts.
More info about dataset can be found here:

Website - https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
Data Dictionary - https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf

## Tech Stack
- Python + Pandas — data transformation
- Google Cloud Storage — raw data lake
- Google Compute Engine — pipeline hosting
- Mage AI — ETL orchestration
- Google BigQuery — data warehouse
- Looker Studio — dashboard and visualisation

## Data Model
Designed a star schema with 1 fact table and 7 dimension tables:
- fact_trips
- dim_datetime
- dim_passenger_count
- dim_trip_distance
- dim_pickup_location
- dim_dropoff_location
- dim_rate_code
- dim_payment_type

![data_model_uber](https://github.com/user-attachments/assets/1dec88ce-19e1-446e-9823-4d878d789c6f)

## Key Findings
- Airport routes (Nassau/Westchester, Newark, JFK) generate avg fares of 
  $65–90 vs $15 for standard rate trips
- Airport routes represent less than 3% of total trip volume (2,800 of 100K trips)
  but command 4–6x higher fares
- Credit card is the dominant payment method (18) vs cash (13)
- Total revenue across 100K trips: $1.64M | Avg fare: $16.39 | Avg distance: 3.03 miles

## Dashboard
[View Live Dashboard](https://lookerstudio.google.com/reporting/9d7facb5-4ab1-48f2-b683-313e26c3c956)


