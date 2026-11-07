# fix_the_stats.py (fixed)
# Count failed logins and the average session length.
events = ["FAILED", "SUCCESS", "FAILED", "SUCCESS", "SUCCESS"]
minutes = [0, 30, 0, 15, 45]

# Bug 1 (semantic): the counters must start at 0 before the loop, not inside it.
failed = 0
for event in events:
    if event == "FAILED":
        failed += 1

print(f"Failed logins: {failed}")

total = 0
count = 0
for value in minutes:
    if value > 0:
        total += value
        count += 1

# Bug 2 (semantic): use / for the average, not //.
# Bug 3 (semantic): print once, after the loop (it was indented inside).
print(f"Average session: {total / count} minutes")

# Bug 4 (semantic): range(1, 4) stops before 4; use range(1, 5) to print 1 to 4.
for level in range(1, 5):
    print(f"Level {level}")