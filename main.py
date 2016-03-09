

if __name__ == "__main__":
    # from keyboard get input
    str = raw_input("input your physics address: ");
    dev = int(str, 16)
    offset = dev & 31
    page_no = (dev>>5) & 31
    index = (dev>>10) & 31
    #get memory
    list = [[]]
    page_1 = 17;
    #step1
    page_2 = list[page_1][index]
    #step2
    page_3 = list[page_2][page_no]
    #step3
    data = list[page_3][offset]
    print data