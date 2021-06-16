A, B = input().split()
idx = 0
if len(A) < len(B):
    shorten = A
    longer = B
else:
    shorten = B
    longer = A
gap_idx = len(longer) - len(shorten)
ans = ''
idx = len(shorten)-1
tmp = digit_shift = 0
while idx >= 0:
    digit_shift = (tmp+digit_shift)//10
    tmp = int(shorten[idx]) + int(longer[idx + gap_idx])
    ans = str((tmp + digit_shift)%10) + ans
    idx -= 1
gap_idx -= 1
tmp += digit_shift
while gap_idx >= 0:
    digit_shift = tmp//10
    tmp = int(longer[gap_idx]) + digit_shift
    ans = str(tmp%10) + ans
    gap_idx -= 1
if tmp//10:
    ans = '1' + ans
print(ans)
# c = int(A) + int(B)
# print(c, str(c) == ans)
