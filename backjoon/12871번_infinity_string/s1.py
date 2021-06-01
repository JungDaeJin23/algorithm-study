# , f(s)는 s를 무한번 붙인 문자열  s = "abc" 인 경우에 f(s) = "abcabcabcabc..."
# repeating(recurring) decimal?
#  s와 t의 길이는 50보다 작거나 같은 자연수이고, 알파벳 소문자
# f(s)와 f(t)가 같으면 1을, 다르면 0
# Brute force


s = input()
t = input()

s_idx = 0
t_idx = 0

if len(s) < len(t):
    shorter_one = s
    longer_one = t
else:
    shorter_one = t
    longer_one = s

if len(longer_one) % len(shorter_one) == 0:
    quotient = len(longer_one) // len(shorter_one)
    if longer_one == shorter_one * quotient:
        print(1)
    else:
        print(0)
else:
    print(0)


# s_infinity_string = ''
# t_infinity_string = ''
#
# while not s_is_circulated or not t_is_circulated:
#     s_infinity_string += s[s_idx]
#     t_infinity_string += t[t_idx]
#
#     s_idx = (s_idx + 1) % len(s)
#     t_idx = (t_idx + 1) % len(t)
#     if s_idx == 0:
#         s_is_circulated = True
#     if t_idx == 0:
#         t_is_circulated = True
# else:
#     if s_infinity_string == t_infinity_string:
#         if s_idx == 0 and t_idx == 0:
#             print(1)
#         else:
#             print(0)
#     else:
#         print(0)

# while not s_is_circulated or not t_is_circulated:
#     if s[s_idx] != t[t_idx]:
#         print(0)
#         break
#     s_idx = (s_idx + 1) % len(s)
#     t_idx = (t_idx + 1) % len(t)
#     if s_idx == 0:
#         s_is_circulated = True
#     if t_idx == 0:
#         t_is_circulated = True
# else:
#     if s_idx == t_idx == 0:
#         print(1)
#     else:
#         print(0)
