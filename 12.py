res = set()
for n in range(4, 10_000):
    st = "8" + n * "4"
    while "11" in st or "444" in st or "8888" in st:
        if "11" in st:
            st = st.replace("11", "4", 1)
        if "444" in st:
            st = st.replace("444", "88", 1)
        if "8888" in st:
            st = st.replace("8888", "1", 1)

    s = sum(int(i) for i in st)
    res.add(s)

print(max(list(res)))
