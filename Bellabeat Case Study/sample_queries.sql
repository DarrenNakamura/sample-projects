-- The orignal CSV file had the datetime entries in a format that
-- BigQuery would not parse upon upload, so I had to upload it with
-- that field as a string, and then parse it into datetime using the
-- queries below.

-- Create clean_date_time column
ALTER TABLE `curious-scarab-446715-k6.fitbit_data.weight_log_info`
ADD COLUMN clean_date_time datetime

-- Parse string into datetime
UPDATE `curious-scarab-446715-k6.fitbit_data.weight_log_info`
SET clean_date_time = PARSE_DATETIME('%m/%d/%Y %I:%M:%S %p', date_time)
WHERE 1 = 1

-- The main question for analysis is what time of day would be
-- best to advertise to potential Bellabeat customers. The
-- following analyses are intended to look for patterns in step
-- counts across different times of day.

-- Get the average steps across all users by hour over the
-- data collection period between 3/12/2016 to 4/11/2016
SELECT clean_date_time, ROUND(AVG(steps), 1) AS average_steps
FROM `curious-scarab-446715-k6.fitbit_data.hourly_steps`
GROUP BY clean_date_time
ORDER BY clean_date_time
LIMIT 1000

-- Count the number of individual instances of a user logging
-- greater than 7500 steps in one hour period (Result: 12)
SELECT COUNT(*)
FROM `curious-scarab-446715-k6.fitbit_data.hourly_steps`
WHERE steps > 7500