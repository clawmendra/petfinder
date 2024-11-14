# PetFinder API Data Collection and Analysis

This notebook collects and processes data on adoptable animals using the PetFinder API, focusing on data relevant for analysis, such as breed, age, and compatibility attributes. The data is fetched in multiple pages, covering a wide geographic area with flexible search criteria.

## Project Overview

The notebook performs the following tasks:

* **API Authentication**: Uses requests to authenticate with the PetFinder API by obtaining an access token with client credentials
* **Data Collection**: Queries the PetFinder API's animals endpoint with parameters such as location and search radius to fetch information on adoptable pets
  * Data is retrieved in pages, with a maximum of 8 pages to cover a wide range of animals
  * Extracts key information for each animal, including attributes like species, breed, age, color, temperament, and compatibility
* **Data Transformation**: Organizes the data into a Pandas DataFrame, ensuring fields are consistent and well-formatted for analysis
* **Data Analysis**: Prepares the data for visualization and analysis

## Columns Selected for Analysis

The following columns are kept in the DataFrame for analysis:

* `organization_id`
* `id`
* `species`
* `name`
* `age`
* `breed_mixed` (breed mix status)
* `color`
* `fixed` (spayed/neutered status)
* `house_trained`
* `good_with_children`
* `good_with_dogs`
* `good_with_cats`
* `gender`
* `distance` (from search location)
* `url` (link to the PetFinder page)

## Usage

To run this notebook:

1. Obtain a PetFinder API key and secret from PetFinder Developer Portal
2. Insert the API credentials in the `client_id` and `client_secret` fields in the notebook
3. Execute the cells to authenticate, collect, and view data on adoptable animals within the specified parameters

## Requirements and Libraries

* Python 3.x
* `requests`
* `pandas`
* `matplotlib`
* `seaborn`