from gcms import GCMS
from object import Color
from exceptions import NoBinFoundException
if __name__=="__main__":

    gcms = GCMS()

    gcms.add_bin(1234, 230)
    gcms.add_bin(1235,10)
    gcms.add_bin(4321, 400)
    gcms.add_bin(4320,20)
    gcms.add_bin(1111, 15)

    # gcms.add_object(2892, 8, Color.BLUE )
    
    try:
        gcms.add_object(8989, 6, Color.BLUE )
    except: 
        print("Object 1 was not able to be added")
    
    try:
        gcms.add_object(2892, 8, Color.YELLOW )
    except: 
        print("Object 2 was not able to be added")

    try:
        gcms.add_object(4839, 9, Color.GREEN )
    except: 
        print("Object 3 was not able to be added")

    try:
        gcms.add_object(8983, 8, Color.BLUE)
    except: 
        print("Object 5 was not able to be added")

    try:
        gcms.add_object(89803, 8, Color.BLUE)
    except: 
        print("Object 5 was not able to be added")

    try:
        gcms.add_object(8983, 80, Color.BLUE)
    except: 
        print("Object 5 was not able to be added")
    
    try:
        gcms.add_object(893, 8, Color.GREEN)
    except: 
        print("Object 5 was not able to be added")

    try:
        gcms.add_object(983, 8, Color.YELLOW)
    except: 
        print("Object 5 was not able to be added")


        


    print(gcms.bin_info(1234))
    print(gcms.bin_info(4321))
    print(gcms.bin_info(1111))
    print(gcms.bin_info(1235))
    print(gcms.bin_info(4320))
    
    
    
