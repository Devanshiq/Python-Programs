#fh=open('demo.txt','a')
#fh.write("helllllllloooooooo ")
#for i in range(10):
 #   fh.write(" this is line no %d \n " %(i+1))
#fh.close()
# with open('demo.txt','a') as fh:
#     for i in range(10):
#         fh.write(" this is line no %d \n " % (i + 1))
#
# fh=open('demo.txt','r')
# print(fh.read())
# print(fh.readline())
# print(fh.readline(4))
# print(fh.readlines())   #it will return in form of list
# print(fh.readlines()[2])
#
# for line in fh:
#     print(line.split(' '))
#     print(len(line.split(' ')))
#
#
# fh.close()


import argparse
if __name__=='__main__':
    # initialize the parser
    parser= argparse.ArgumentParser(
        description="my math script"
    )
    #add the parameters positional/optional arguments
    #parse the arguments
    # parser.add_argument('num1',help="Number1",type=float)                      #positional arguments
    # parser.add_argument('num2', help="Number2",type=float)
    # parser.add_argument('operation', help="provide operator",default='+')

    parser.add_argument('-n','--num1', help="Number1", type=float)                   #optional arguments defined with the help of double hyphen
    parser.add_argument('-i','--num2', help="Number2", type=float)
    parser.add_argument( '-o','--operation', help="provide operator", default='+')


args=parser.parse_args()
print(args)
result=None
if args.operation=='+':
    result= args.num1+args.num2
if args.operation == '-':
    result= args.num1-args.num2
if args.operation == '*':
    result= args.num1*args.num2
if args.operation == 'pow':
    result= pow(args.num1,args.num2)

print("result ",result)

