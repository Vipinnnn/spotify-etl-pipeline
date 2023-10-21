# SpotifyEtl
# Spotify Data ETL with Airflow

## Project Overview

The **Spotify Data ETL with Airflow** project is an end-to-end data pipeline designed to automate the extraction, transformation, and loading of data of artists from Spotify. It integrates with the Spotify API, extracts data, processes it, and allows you to choose a destination for storage, which can include Amazon S3, Google Cloud Storage, or other storage solutions.

## Architecture

<img width="646" alt="image" src="https://github.com/Vipinnnn/spotify-etl-pipeline/assets/71926172/662cf626-1538-4ea1-9f0d-ec687e6558ca">


## Project Components

This project is comprised of several key components, with each playing a crucial role in ensuring the data of Spotify Artists is efficiently processed and organized. The main components include:

- **Data Extraction:** For my project, I've used (https://kworb.net/itunes/) website to scrape names of top Global Artists and the used the Spotify Api to extract artists details like their genre, followers and popularity.

- **Data Transformation:** The extracted data is transformed into a structured format suitable for analysis. 

- **Data Loading:** Once the data is prepared, you can choose the destination for storage. In my project, I have configured data to be stored in an Amazon S3 bucket.

- **Airflow Integration:** This project is integrated with Apache Airflow, allowing for scheduled or trigger-based ETL jobs. This integration has been instrumental in automating and orchestrating the entire pipeline.


## Project Goals

The primary goals of this project include:

- Automating the collection of data of Spotify Artists.

- Ensuring the collected data is clean, structured, and ready for analysis.

- Allowing flexibility in choosing the destination for storing the data. My project's setup stores data in an Amazon S3 bucket, and it's adaptable to other cloud storage solutions.

- Implementing an efficient and reliable ETL process that can be scheduled and monitored. I have incorporated scheduling using Apache Airflow.

- Providing a framework for expanding the ETL process and customizing it as per specific requirements.


## Conclusion

The **Spotify ETL with Airflow** project offers a comprehensive solution for automating the extraction, transformation, and loading of data of Spotify Artists. By leveraging the Spotify API and integrating with Apache Airflow, I have created a powerful tool that can streamline data collection and prepare it for analysis.

The core advantages of this project are its flexibility and adaptability. You can easily configure it to collect data from other Artists, apply custom data transformations, and choose your preferred data storage solution. The Apache Airflow integration makes it easy to schedule ETL jobs and monitor their execution.

## Final Output
<img width="646" alt="image" src="https://github.com/Vipinnnn/spotify-etl-pipeline/assets/71926172/04808457-f71a-4d70-a2c0-4bbfeb0c7d6f">




