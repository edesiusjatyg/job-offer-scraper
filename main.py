from csv_operations import CsvOperations

def main():
    csv = CsvOperations()
    if not csv.check_csv("result.csv"):
        csv.create_csv(
            "result.csv",
            "job_title,company_name,location,job_type,experience_level,education_req,salary_range,job_requirements,job_responsibilities,posted_date,source_platform"
        )
    

if __name__ == "__main__":
    main()