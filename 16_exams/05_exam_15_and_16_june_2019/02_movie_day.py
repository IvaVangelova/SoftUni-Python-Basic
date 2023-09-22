time_for_pictures = int(input())
scenes_count = int(input())
duration_of_scenes = int(input())
field_preparation = time_for_pictures * 0.15

time_needed = scenes_count * duration_of_scenes + field_preparation
left_time = time_needed - time_for_pictures
if time_needed <= time_for_pictures:
    print(f"You managed to finish the movie on time! You have {round(abs(left_time))} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(left_time)} minutes.")
