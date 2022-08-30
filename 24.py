s = open('files').readline()
c = m = s[0]
for i in range(1, len(s)):
    if s[-1] == s[i]:
        c+=s[i]
        m = max(m, c, key=len)
    else:
        c = s[i]
print(m, len(m))