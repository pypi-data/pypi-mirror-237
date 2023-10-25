from src.jobs.bronze.bronze import BronzeLayer

if __name__ == "__main__":
    job = BronzeLayer()
    job.launch(model_data_name="seven-day-load-forecast-by-forecast-zone")
