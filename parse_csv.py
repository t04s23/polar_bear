import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('polar_bear_data.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS deployments')
print("table dropped successfully");
# create table again
conn.execute('CREATE TABLE deployments (BearID INTEGER, PTT_ID INTEGER, capture_lat REAL, capture_long REAL, Sex TEXT, Age_class TEXT, Ear_applied TEXT)')
print("table created successfully");

conn.execute('DROP TABLE IF EXISTS status')
print("table dropped successfully");
# create table again
conn.execute('CREATE TABLE status (status_id INTEGER PRIMARY KEY AUTOINCREMENT, deployID INTEGRER, received TEXT, latitude REAL, longitude REAL, temperature REAL, deployment_id INTEGER)')
print("table created successfully");

# open the file to read it into the database
with open('PolarBear_Telemetry_southernBeaufortSea_2009_2011/USGS_WC_eartag_deployments_2009-2011.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        BearID = int(row[0])
        PTT_ID = int(row[1])
        capture_lat = float(row[6])
        capture_long = float(row[7])
        Sex = row[9]
        Age_class = row[10]
        Ear_applied = row[11]

        cur.execute('INSERT INTO deployments VALUES (?,?,?,?,?,?,?)', (BearID, PTT_ID, capture_lat, capture_long, Sex, Age_class, Ear_applied))
        conn.commit()
print("data parsed successfully");

# open the file to read it into the database
with open('PolarBear_Telemetry_southernBeaufortSea_2009_2011/USGS_WC_eartags_output_files_2009-2011-Status.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)
        if(row[1] == ''):
          continue

        pttID = int(row[1])
        received = row[2]
        latitude = row[4]
        longitude = row[5]
        temperature = row[9]
        deploymentID = row[0]

        cur.execute('INSERT INTO status VALUES (NULL,?,?,?,?,?,?)', (pttID, received, latitude, longitude, temperature, deploymentID))
        conn.commit()
print("data parsed successfully");



conn.close()
        
