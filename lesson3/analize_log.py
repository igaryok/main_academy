file_writen = open("app_analize.log", "w")

with open("app.log") as file_open:
    for line in file_open:
        if "[ERROR]" in line:
            # get ip from sting
            line_ip = line[:line.find(" ")]
            # get time from string
            line_time = line[line.find(" ")+12:line.find(" ")+27]
            # get describe from string
            line_describe = line[line.find("]")+4:]

            print(line_ip, line_time, line_describe)

            file_writen.write("{0} {1} {2} \n".format(line_ip, line_time, line_describe))
            file_writen.flush()

file_writen.close()

print("Well done!")