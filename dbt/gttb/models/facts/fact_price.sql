{{ config(materialized='incremental') }}

select bhav_date, 
jsonb_array_elements(bhav_json_response) ->> 'scripCode' as scrip_code,
jsonb_array_elements(bhav_json_response) ->> 'close' as close_price
from {{ source('raw', 'raw_bhavcopy') }}