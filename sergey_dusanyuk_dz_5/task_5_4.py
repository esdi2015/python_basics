from time import perf_counter

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]


# list

start = perf_counter()
result = []

for key, val in enumerate(src):
    if key != 0:
        prev_val = src[key-1]
        curr_val = val

        if curr_val > prev_val:
            result.append(val)


print(perf_counter() - start)
print(type(src))
print(result)


# generator

start = perf_counter()
result_gen = []
src_gen = (i for i in src)

for i in range(len(src)):
    if i == 0:
        curr_val_gen = next(src_gen)
    else:
        prev_val_gen = curr_val_gen
        curr_val_gen = next(src_gen)

        if curr_val_gen > prev_val_gen:
            result_gen.append(curr_val_gen)

print(perf_counter() - start)
print(type(src_gen))
print(result_gen)
