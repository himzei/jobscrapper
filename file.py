import csv 

def save_to_file(file_name, jobs): 
    with open(f"./{file_name}.csv", "w", encoding="cp949") as file:
      csv_writer = csv.writer(file)
      csv_writer.writerow(["No","제목","회사","지역","link"])

      for index, job in enumerate(jobs): 
          csv_writer.writerow([index, job["title"], job["company"], job["location"], job["link"]])

    