def min_time_to_cross(t, test_cases):
    results = []
    
    for n, c, s in test_cases:
        # Find all positions of 'g'
        g_positions = [i for i in range(n) if s[i] == 'g']
        
        # Find current position based on color c
        current_position = s.index(c)
        
        # Calculate minimum time to reach 'g'
        min_time = float('inf')
        
        # Check each position of 'g'
        for g_pos in g_positions:
            if g_pos >= current_position:
                wait_time = g_pos - current_position
            else:
                wait_time = (n - current_position) + g_pos
            
            min_time = min(min_time, wait_time)
        
        results.append(min_time)
    
    return results

# Reading input
import sys
input = sys.stdin.read
data = input().splitlines()

t = int(data[0])
test_cases = []

for i in range(1, len(data), 2):
    n_c = data[i].split()
    n = int(n_c[0])
    c = n_c[1]
    s = data[i + 1]
    test_cases.append((n, c, s))

# Get results
results = min_time_to_cross(t, test_cases)

# Print results
for result in results:
    print(result)
