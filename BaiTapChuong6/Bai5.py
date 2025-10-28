'''
lst = [20, 1, -34, 40, -8, 60, 1, 3]

(a) lst
→ The whole list itself
    [20, 1, -34, 40, -8, 60, 1, 3]

(b) lst[0:3]
→ Elements from index 0 up to 2 (stop before 3)
    [20, 1, -34]

(c) lst[4:8]
→ Elements from index 4 up to 7
    [-8, 60, 1, 3]

(d) lst[4:33]
→ From index 4 to the end because 33 is beyond the list length
    [-8, 60, 1, 3]

(e) lst[-5:-3]
→ Negative indexes count from the end

-5 → element at index 3 (40)

-3 → element at index 5 (60, stop before it)
    [40, -8]

(f) lst[-22:3]
→ Start far before the list, so Python begins at index 0, stop before 3
    [20, 1, -34]

(g) lst[4:]
→ From index 4 to the end
    [-8, 60, 1, 3]

(h) lst[:]
→ Copy of the whole list
    [20, 1, -34, 40, -8, 60, 1, 3]

(i) lst[:4]
→ From index 0 to 3
    [20, 1, -34, 40]

(j) lst[1:5]
→ From index 1 to 4
    [1, -34, 40, -8]

(k) -34 in lst
→ Check if -34 exists
    True

(l) -34 not in lst
→ Opposite of above
    False

(m) len(lst)
→ Total number of elements
    8


'''