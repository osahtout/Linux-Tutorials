def format_line(line):
    line = line.rstrip()
    line = line.replace("# ", "")
    line = line.replace("#", "")
    line = line.replace(" ", "-")
    line_in_bracket = "["+line+"](#"+line.lower()+")\n"
    return line_in_bracket



try:

    mkfile = input("Enter path of mardown file: ")
    if not mkfile:
        mkfile = eval(input("Enter path of markdown file"))
        
    if ".md" not in mkfile:
        raw_name = mkfile
        mkfile = mkfile+".md"
    else:
        raw_name = mkfile.replace(".md", "")

    new_file = open(raw_name+"_ToC.md", "w")
    fi = open(mkfile, 'r')

    line = fi.readline()

    while line:
        if line[0] is "#":

            if line.count("#") is 1:
                line = format_line(line)
                new_file.write("- "+line)

            elif line.count("#") is 2:
                line = format_line(line)
                new_file.write("    - "+line)

            elif line.count("#") is 3:
                line = format_line(line)
                new_file.write("        - "+line)

        line = fi.readline()


    fil = open(mkfile, 'r')
    line2 = fil.readline()

    while line2:
        new_file.write(line2)
        line2 = fil.readline()

finally:
    fi.close() 
    fil.close()
    new_file.close()



print("done")