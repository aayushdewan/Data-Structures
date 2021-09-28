def max_prof(w, v, max_w, n):
    if max_w ==0 or n == 0:
        return 0
    elif w[n-1] <= max_w:
        return max(v[n-1]+max_prof(w, v, max_w-w[n-1], n-1), max_prof(w, v, max_w, n-1))
    else:
        return (max_prof(w, v, max_w, n-1))

print(max_prof([1,3,4,5], [1,4,5,7], 7, 4))

