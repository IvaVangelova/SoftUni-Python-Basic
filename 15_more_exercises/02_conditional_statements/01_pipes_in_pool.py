pool_capacity_liters = int(input())
flow_rate_first_pipe_per_hour = int(input())
flow_rate_second_pipe_per_hour = int(input())
worker_hours_absent = float(input())

hours_fill_water_first_pipe = flow_rate_first_pipe_per_hour * worker_hours_absent
hours_fill_water_second_pipe = flow_rate_second_pipe_per_hour * worker_hours_absent

total_hours = hours_fill_water_first_pipe + hours_fill_water_second_pipe

fullness = pool_capacity_liters - total_hours

total_percent_full = (total_hours / pool_capacity_liters) * 100
percent_first_pipe = (hours_fill_water_first_pipe / total_hours) * 100
percent_second_pipe = (hours_fill_water_second_pipe / total_hours) * 100


if fullness >= 0:
    print(f"The pool is {total_percent_full:.2f}% full."
          f" Pipe 1: {percent_first_pipe:.2f}%."
          f" Pipe 2: {percent_second_pipe:.2f}%.")

else:
    print(f"For {worker_hours_absent} hours "
          f"the pool overflows with {abs(fullness)} liters.")
