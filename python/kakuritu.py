import sys

def main():
    print ("haloo")

    args = sys.argv

    #引き数にファイルがあれば、それを使用
    if len(args) <= 2:
        path = "hairetu"
    else:
        path = args[1]


    f = open(path, "r")

    for line in f:
	       print("read file")
	       print(line)
	       if line == "5":
		             print("add 5")
		             perint(int(args[2])+int(line))

    # file close
    f.close()

main()
