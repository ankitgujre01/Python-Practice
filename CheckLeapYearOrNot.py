
year = int(input("Enter a year: "))

# Step 1: Calculate the extra time accumulated in 4 years
DaysInAYear = 365
ExtraHoursPerYears = 5
ExtraMinutesPerYear = 48
ExtraSecondsPerYear = 47.5

# Accumulate extra time over 4 years
TotalExtraHours = ExtraHoursPerYears * 4
TotalExtraMinutes = ExtraMinutesPerYear * 4
TotalExtraSeconds = ExtraSecondsPerYear * 4

# Convert accumulated extra time to days
ExtraHoursToDays = TotalExtraHours // 24
ExtraMinutesToDays = TotalExtraMinutes // (24 * 60)
ExtraSecondsToDays = TotalExtraSeconds // (24 * 60 * 60)

# Total extra days added in 4 years
TotalExtraDays = ExtraHoursToDays + ExtraMinutesToDays + ExtraSecondsToDays

# Step 2: Leap year logic
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
