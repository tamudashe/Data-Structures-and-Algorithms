import pprint as pp 

def find_duplicate(paths):
    res_dict = {}
    for i in paths:  # O(n) n -> length of input array
        files = i.split(" ")
        path = files[0]

        for test_file in files[1:]:  # O(k) k -> average number of files in a directory
            filename, content = test_file.split("(")
            p = path + "/" + filename
            # add to list
            if content in res_dict: res_dict[content].append(p)
            else: res_dict[content] = [path]
    result = []
    for i in res_dict: # O(n) n -> number of unique files
        content = res_dict[i]
        if len(content) > 1: result.append(content)
    return result


# test cases
test = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
print(find_duplicate((test)))
"""
O(nk) -> O(n)
"""
