current_time = 6*3600+52*60
mile_1 = 8*60+15
mile_2_3_4 = 3*(7*60+12)
end_time = current_time + mile_1 + mile_2_3_4
end_time_h = end_time//3600
end_time_m = end_time%60
print(f"{end_time_h}:{end_time_m}")