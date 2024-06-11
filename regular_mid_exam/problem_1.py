import math

biscuits_per_day_per_worker = int(input())
workers_in_our_factory = int(input())
competing_factory_production = int(input())
n_days = 30

total_produced_month = 0
for day in range(1, n_days+1):
    if day % 3 == 0:
        total_produced_per_day = math.floor((biscuits_per_day_per_worker * workers_in_our_factory) * 0.75)
    else:
        total_produced_per_day = biscuits_per_day_per_worker * workers_in_our_factory
    total_produced_month += total_produced_per_day

diff = abs(total_produced_month - competing_factory_production)
diff_percentage = (diff/competing_factory_production) * 100

print(f"You have produced {total_produced_month} biscuits for the past month.")
if total_produced_month > competing_factory_production:
    print(f"You produce {diff_percentage:.2f} percent more biscuits.")
elif total_produced_month < competing_factory_production:
    print(f"You produce {diff_percentage:.2f} percent less biscuits.")