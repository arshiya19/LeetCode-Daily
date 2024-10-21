s = "ABBAABZB"

st = list(s)

prev = 0
current = 1
min_strokes = 1  # Start with 1 stroke for the first character

while current < len(st):
    if st[prev] != st[current]:  # Increment stroke count only if a change occurs
        min_strokes += 1
        prev = current  # Update prev to current when a change is detected

    current += 1  # Always move current to the next character

print(min_strokes)