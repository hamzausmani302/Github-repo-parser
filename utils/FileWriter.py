import csv

class Writer:
    def __init__(self, filename):
        self.filename = filename;
    def write(self,content):
        with open(self.filename , "w" , encoding="utf-8") as f:
            f.write(content);


class CSVWriter(Writer):
    def __init__(self,  filename):
        super().__init__(filename)

    def write(self,users):
        f = open(self.filename, 'w' , encoding="utf-8");
        writer = csv.writer(f)
        
        for user in  users:
            row = [user.nick , user.fullName , user.followers , user.url]
            
            
            writer.writerow(row);
        f.close()
    def sort(self,arr):
        for i in range(len(arr)-1):
            for j in range(len(arr)-1):
                
                if(int(arr[j].followers) < int(arr[j+1].followers) ):
                    temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
        return arr;