def compress(chars):
    if len(chars) == 0:
        return 0

    anchor = 0
    write_idx = 0
    count = 1

    for i in range(1, len(chars)):
        if chars[i] == chars[i-1]:
            count += 1
        else:
            chars[write_idx] = chars[anchor]
            write_idx += 1
            if count > 1:
                count_str = str(count)
                for j in range(len(count_str)):
                    chars[write_idx] = count_str[j]
                    write_idx += 1
            anchor = i
            count = 1

    chars[write_idx] = chars[anchor]
    write_idx += 1
    if count > 1:
        count_str = str(count)
        for j in range(len(count_str)):
            chars[write_idx] = count_str[j]
            write_idx += 1

    return write_idx

chars = ["a","a","b","b","c","c","c"]
new_length = compress(chars)
print(new_length)
print(chars[:new_length])
