class ArgsParser:
    @staticmethod
    def parseArgs(args , index):
        try:
            return args[index];
        except:
            raise Exception("parsing error occured");

    @staticmethod
    def parseURL(url ):
        if(url[len(url)-1] != '/'):
            return url;
        return url[:len(url)-1];
if __name__ =="main":
    pass;
