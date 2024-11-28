cnt = 0

for i in range(1 << 11):
  if i & (1 << 1) and not (i & (1 << 0)): continue
  if i & (1 << 2) and not (i & (1 << 1) and i & (1 << 0)): continue
  if i & (1 << 3) and not (i & (1 << 1) and i & (1 << 0)): continue
  if i & (1 << 4) and not (i & (1 << 1) and i & (1 << 0) or i & (1 << 6) and i & (1 << 5) and i & (1 << 0)): continue
  if i & (1 << 5) and not (i & (1 << 0)): continue
  if i & (1 << 6) and not (i & (1 << 5) and i & (1 << 0)): continue
  if i & (1 << 7) and not (i & (1 << 5) and i & (1 << 0)): continue
  if i & (1 << 8) and not (i & (1 << 5) and i & (1 << 0) or i & (1 << 9) and i & (i << 0)): continue
  if i & (1 << 9) and not (i & (1 << 0)): continue
  if i & (1 << 10) and not (i & (1 << 9) and i & (i << 0)): continue

  cnt += 1

print(cnt)
