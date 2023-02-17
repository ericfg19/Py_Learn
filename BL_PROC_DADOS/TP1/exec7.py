time_red = 2
time_blue = 1.2
time_yellow = 1

minutes_red = 60 * time_red
minutes_blue = 60 * time_blue
minutes_yellow = 60 * time_yellow

rate_hose_red = 1 / minutes_red
rate_hose_blue = 1 / minutes_blue
rate_hose_yellow = 1 / minutes_yellow

rate_hose_combined = rate_hose_red + rate_hose_red + rate_hose_yellow

time = 1 / rate_hose_combined
print(time)