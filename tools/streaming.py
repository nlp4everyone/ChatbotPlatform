
def stream(list_string:list):
    output = []
    for i in range(len(list_string)):
        temp_infor = list_string[:i]
        temp_infor = " ".join(temp_infor)
        output.append(temp_infor)
    output = output[1:]
    return output