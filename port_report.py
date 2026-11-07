start_port = int(input("Start port: "))
end_port = int(input("End port: "))
print(f"Start port: {start_port}")
print(f"End port: {end_port}")
count = 0
for port in range(start_port, end_port + 1):
    if port <= 1023:
        category = "system"
    elif port <= 49151:
        category = "user"
    else:
        category = "dynamic"
    print(f"{port}: {category}")
    count += 1
print(f"Ports checked: {count}")