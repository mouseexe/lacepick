import re

def contains(word, string): return bool(re.search(r'\b' + re.escape(word.lower()) + r'\b', string.lower()))

def rev_dir(s, p={'(': ')', '[': ']', '{': '}', '<': '>'}):
    st, r, i = [], "", 0
    while i < len(s):
        if s[i] in p:
            j, c = i + 1, 1
            while j < len(s) and c:
                if s[j] == s[i]: c += 1
                elif s[j] == p[s[i]]: c -= 1
                j += 1
            st.append((i, j)); i = j - 1
        else: r += s[i]
        i += 1
    rem = s
    while st: a, b = st.pop(); r = s[a:b][1:-1][::-1] + r; rem = rem[:a] + rem[b:]
    return rem[::-1] + r