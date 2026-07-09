# 01 - Local ETL Pipeline

A production-style ETL pipeline built in Python to demonstrate clean software architecture, data validation, reporting, and data loading principles.

The project is intentionally modular so that each stage of the ETL process has a single responsibility. It serves as the foundation for future projects involving APIs, Google Cloud Storage, BigQuery, and distributed data processing.

---

## Project Architecture

```
                main.py
                    │
                    ▼
              Reader Module
                    │
                    ▼
             Cleaner Module
                    │
                    ▼
            Validator Module
                    │
                    ▼
             Reporter Module
                    │
                    ▼
              Loader Module
```

---

## Features

- Read customer data from CSV
- Clean incoming data
- Validate business rules
- Generate validation reports
- Export processed data
- Modular project structure
- Git version control with meaningful commit history

---

## Current Validation Rules

- Missing Customer ID
- Duplicate Customer ID
- Negative Age
- Negative Salary
- Invalid Department

---

## Project Structure

```
01_local_etl_pipeline/
│
├── config/
│   └── settings.py
│
├── data/
│
├── output/
│
├── src/
│   ├── cleaner.py
│   ├── loader.py
│   ├── reader.py
│   ├── reporter.py
│   ├── utils.py
│   └── validator.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- Pandas
- Git
- GitHub
- pathlib

---

## Future Enhancements

- Read data from REST APIs
- Store output in Google Cloud Storage (GCS)
- Load analytical data into BigQuery
- Process large datasets using PySpark
- Orchestrate pipelines using Apache Airflow
- Real-time processing with Kafka
- Data transformations using dbt

---

## Author

**Indranil Banerjee**

Building production-style Data Engineering projects by solving real engineering problems.