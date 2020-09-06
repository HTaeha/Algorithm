from copy import deepcopy

def solution(directory, command):
    for data in command:
        s_str = data.split(" ")
        cmd_name = s_str[0]
        dir_name = s_str[1]
        if len(s_str) == 3:
            dir_name2 = s_str[2]
        if cmd_name == 'mkdir':
            directory = mkdir(directory, dir_name)
        elif cmd_name == "cp":
            directory = cp(directory, dir_name, dir_name2)
        elif cmd_name == "rm":
            directory = rm(directory, dir_name)

    directory = sorted(directory)

    return directory

def mkdir(directory, dir):
    directory.append(dir)
    return directory

def cp(directory, dir, dir2):
    temp_dir = deepcopy(directory)

    s_dir = dir.split("/")
    del s_dir[0]
    s_dir2 = dir2.split("/")
    del s_dir2[0]

    for i, data in enumerate(directory):
        s = data.split("/")
        del s[0]
        flag = True
        for j, d in enumerate(s_dir):
            if s[j] != d:
                flag = False
                break
        if flag:
            temp_dir.append(dir2 + data)

    return temp_dir

def rm(directory, dir):
    temp_dir = deepcopy(directory)
    del_list = []

    s_dir = dir.split("/")
    del s_dir[0]

    for i, data in enumerate(directory):
        s = data.split("/")
        del s[0]
        flag = True
        for j, d in enumerate(s_dir):
            if s[j] != d:
                flag = False
                break
        if flag:
            del_list.append(i)

    print(del_list)
    for del_i in del_list:
        temp_dir.remove(directory[del_i])

    return temp_dir



if __name__ == "__main__":
    directory = [
        "/",
        "/hello",
        "/hello/tmp",
        "/root",
        "/root/abcd",
        "/root/abcd/etc",
        "/root/abcd/hello"
    ]
    command = [
        "mkdir /root/tmp",
        "cp /hello /root/tmp",
        "rm /hello"
    ]
    solution(directory, command)