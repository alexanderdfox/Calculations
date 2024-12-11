import math

# Given values
dilated_time_years = 144000  # Dilated time in years
dilated_time_hours = 8  # Time in hours for the moving observer
seconds_in_hour = 3600
seconds_in_year = 365.25 * 24 * seconds_in_hour  # average number of seconds in a year

# Convert hours to seconds and years to seconds
dilated_time_seconds = dilated_time_hours * seconds_in_hour
stationary_time_seconds = dilated_time_years * seconds_in_year

# Exact speed of light in m/s
c = 299792458  # Speed of light in m/s

# Calculate the velocity for the time dilation of 144,000 years being 8 hours
v_time_dilation = c * math.sqrt(1 - (dilated_time_seconds / stationary_time_seconds) ** 2)

# Given Lorentz factor for the second calculation
gamma = 7

# Calculate the velocity for a Lorentz factor of 7
v_lorentz_factor = c * math.sqrt(1 - (1 / gamma) ** 2)

# Calculate the difference in velocities
velocity_difference = abs(v_time_dilation - v_lorentz_factor)

# Conversion factor from m/s to mph (1 m/s = 2.23694 mph)
mps_to_mph = 2.23694

# Convert the velocities to mph
v_time_dilation_mph = v_time_dilation * mps_to_mph
v_lorentz_factor_mph = v_lorentz_factor * mps_to_mph
velocity_difference_mph = velocity_difference * mps_to_mph

# Speed of the fastest rocket (Parker Solar Probe) in mph
rocket_speed_mph = 430000  # Speed of the fastest rocket in mph

# Calculate the difference in speed between the provided velocity and the fastest rocket
velocity_difference_rocket_mph = v_time_dilation_mph - rocket_speed_mph

# Print the results
print(f"Velocity for 8 hours dilating into 144,000 years: {v_time_dilation} m/s ({v_time_dilation_mph} mph)")
print(f"Velocity for Lorentz factor of 7: {v_lorentz_factor} m/s ({v_lorentz_factor_mph} mph)")
print(f"Difference in velocities: {velocity_difference} m/s ({velocity_difference_mph} mph)")
print(f"\nThe speed {v_time_dilation_mph} mph is {velocity_difference_rocket_mph} mph faster than the fastest rocket speed ({rocket_speed_mph} mph).")

# Given values
distance_alpha_centauri_ly = 4.367  # Distance to Alpha Centauri in light-years
light_year_in_miles = 5.879e12  # 1 light-year in miles
speed_mph = 670617740.99852  # Speed in mph

# Calculate the distance to Alpha Centauri in miles
distance_alpha_centauri_miles = distance_alpha_centauri_ly * light_year_in_miles

# Calculate the time it would take to reach Alpha Centauri in hours
time_hours = distance_alpha_centauri_miles / speed_mph

# Convert time from hours to years
hours_in_year = 365.25 * 24  # number of hours in a year
time_years = time_hours / hours_in_year

# Print the result
print(f"It would take approximately {time_years} years to reach Alpha Centauri at {speed_mph} mph.")

# Given values
distance_alpha_centauri_miles = 2.565e13  # Distance to Alpha Centauri in miles
spacex_dragon_speed_mph = 17500  # Speed of SpaceX Dragon in mph

# Calculate the time it would take to reach Alpha Centauri in hours
time_hours = distance_alpha_centauri_miles / spacex_dragon_speed_mph

# Convert time from hours to years
hours_in_year = 365.25 * 24  # number of hours in a year
time_years = time_hours / hours_in_year

# Print the result
print(f"It would take approximately {time_years} years for SpaceX Dragon to reach Alpha Centauri at {spacex_dragon_speed_mph} mph.")