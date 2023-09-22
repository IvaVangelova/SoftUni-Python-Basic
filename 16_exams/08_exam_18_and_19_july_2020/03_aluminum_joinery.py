window_frames_count = int(input())
type_window_frame = input()
delivery = input()
total = 0
total_90X130 = 110 * window_frames_count
total_100X150 = 140 * window_frames_count
total_130X180 = 190 * window_frames_count
total_200X300 = 250 * window_frames_count

if type_window_frame == "90X130":
    if 30 < window_frames_count <= 60:
        total = total_90X130 * 0.95
    elif window_frames_count > 60:
        total = total_90X130 * 0.92
    else:
        total = total_90X130
elif type_window_frame == "100X150":
    if 40 < window_frames_count <= 80:
        total = total_100X150 * 0.94
    elif window_frames_count > 80:
        total = total_100X150 * 0.90
    else:
        total = total_100X150
elif type_window_frame == "130X180":
    if 20 < window_frames_count <= 50:
        total = total_130X180 * 0.93
    elif window_frames_count > 50:
        total = total_130X180 * 0.88
    else:
        total = total_130X180
elif type_window_frame == "200X300":
    if 25 < window_frames_count <= 50:
        total = total_200X300 * 0.91
    elif window_frames_count > 50:
        total = total_200X300 * 0.86
    else:
        total = total_200X300

if window_frames_count < 10:
    print("Invalid order")
else:
    if delivery == "With delivery":
        total += 60
    if window_frames_count > 99:
        total *= 0.96
    print(f"{total:.2f} BGN")
