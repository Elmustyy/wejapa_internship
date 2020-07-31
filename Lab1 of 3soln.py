# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# the decrease in the rainfall variable by 10% to account for runoff
rainfall_dec  = 5e6 * 0.1


# adding  the rainfall variable to the reservoir_volume variable

reservoir_volume = rainfall + reservoir_volume
print(reservoir_volume)

# increasing the reservoir_volume by 5% to account for stormwater that flows into the reservoir in the days following the storm

reservoir_volume_storm = reservoir_volume +0.05
print(reservoir_volume_storm)

# decrease reservoir_volume by 5% to account for evaporation

reservoir_volume_evaporation = reservoir_volume -0.05
print(reservoir_volume_evaporation)

# subtracting 2.5e5 cubic metres from reservoir_volume to account for water that's piped to arid regions.

reservoir_volume_arid = reservoir_volume - 2.5e5
print(reservoir_volume_arid)
