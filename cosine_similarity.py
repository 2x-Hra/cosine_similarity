from csv import reader
from csv import writer
import math 


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np



def strTofloat(Arr2D):
    '''
        this function will change type of a 2d STRING array to a 2d FLOAT array
    '''
    csv_int_arr = []
    for arr_el in Arr2D:
        arr_el = [float(i) for i in arr_el] 
        
        csv_int_arr.append(arr_el)

    return csv_int_arr

def normCal (v):
    # v= [1, 2, 3, 4]

    ans = 0
    n = len(v)
    for i in range(n):
        ans += (v[i])**2
    return math.sqrt(ans)

def dotProduct(v1,v2):
    n = len(v1)
    ans = 0
    for i in range(n):
        ans += v1[i] * v2[i]

    return ans


def cosine(v1,v2):
    norm_v1 = normCal(v1)
    norm_v2 = normCal(v2)
    dp = dotProduct(v1,v2)

    return ( dp / (norm_v1*norm_v2))

def cosine_center(center,data_arr):
    '''
        calculate the cosine_similarity for the center to all the elemnts
    '''
    result = []
    counter = 0
    cosinus = 0
    while(counter < len(data_arr)):
        cosinus = cosine(center,data_arr[counter])
        result.append(cosinus)
        counter += 1
    return result

def maximum_cal(arr1_cosinus, arr2_cosinus,csv_arr):
    counter = 0
    min_res = []
    cosine_cntr1 = [] 
    cosine_cntr2 = [] 

    while(counter < len(csv_arr)):
        if(arr1_cosinus[counter] >= arr2_cosinus[counter]):
           cosine_cntr1.append(csv_arr[counter])
        if(arr2_cosinus[counter] > arr1_cosinus[counter]):
            cosine_cntr2.append(csv_arr[counter])
  
        counter +=1
        
    return (cosine_cntr1 , cosine_cntr2)

def avg_cal (arr2d):
    arr_x = []
    arr_y = []
    arr_z = []
    arr_c = []
    avg_x = 0
    avg_y = 0
    avg_z = 0
    avg_c = 0
    counter = 0
    while(counter <len(arr2d)):
        counter1 =0
        while(counter1 < 4):
            arr_x.append(arr2d[counter][0])
            arr_y.append(arr2d[counter][1])
            arr_z.append(arr2d[counter][2])
            arr_c.append(arr2d[counter][3])

            counter1 += 1
        counter += 1

    avg_x = sum(arr_x)/len(arr_x)
    avg_y = sum(arr_y)/len(arr_y)
    avg_z = sum(arr_z)/len(arr_z)
    avg_c = sum(arr_c)/len(arr_c)

    new_cntr = [avg_x, avg_y, avg_z, avg_c]

    return new_cntr

def kmeans(csv_arr):
    center1 = csv_arr[0]
    center2 = csv_arr[1]
    arr1_cosine = []
    arr2_cosine = []
    new_points1 = []
    new_points2 = []
    counter = 0
    arr1_temp =[]
    arr2_temp =[]
    i =0
    while(True):
        arr1_cosine = cosine_center(center1,csv_arr)
        arr2_cosine = cosine_center(center2,csv_arr)
        arr1_temp = []
        arr2_temp = []
        for point in new_points1:
            arr1_temp.append(point)
        for point in new_points2:
            arr2_temp.append(point)
        new_points1, new_points2 = maximum_cal(arr1_cosine,arr2_cosine,csv_arr)
        center1 = avg_cal(new_points1)
        center2 = avg_cal(new_points2)
        i +=1
        if(arr1_temp == new_points1 and arr2_temp == new_points2 ):
            print("THIS IS I "+ str(i) )
            
            break
        
    return (new_points1, new_points2)

def s_cal(points1, points2 ):
    counter = 0
    max_arr = []
    while(counter < len(points1)):
        el = points1[counter]
        arr_c = cosine_center(el,points2)
        max_arr.append(max(arr_c))

        counter +=1
    
    return max(max_arr)

# reading and ploter section in down below ~~~~~~~~~~~~~~~~~~ #




def rows_readFile(file_name):
    '''
        this function will read the file row by row
    '''
    
    csv_arr =[]
    with open(file_name, 'r') as csv_file:
        csv_reader = reader(csv_file)
        for row in csv_reader:
            csv_arr.append(row)
    return csv_arr

def column_readFile(file_name,col):
    '''
        read the file and return the column with number "col"
        for example if col == 2 then it will return the 2th column of the file
    '''
    arr_res = []
    with open(file_name, "r") as csv_file:
        csv_reader = reader(csv_file)
        for lines in csv_reader:
            arr_res.append(lines[col])
    return arr_res

def columnedFile(file_name):
    '''
        this function will read the file column by column and return all the columns in a 2d array
    '''
    counter =0
    file_col = []
    while(counter <4):
        temp_row = column_readFile(file_name,counter)
        
        file_col.append(temp_row)
        

        counter +=1

    file_col = strTofloat(file_col)

    return file_col
def ploter(columned_file):
    '''
        this function will plot 4D dots
    '''
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = columned_file[0]
    y = columned_file[1]
    z = columned_file[2]
    c = columned_file[3]

    img = ax.scatter(x, y, z, c=c, cmap=plt.magma())
    fig.colorbar(img)
    plt.show()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

'''
    kari ke man kardam ine ke az Kmeans va cluster bandi estefade kardam
    2ta center ro entekhab mikonam ( element haye aval va dovome file) 
    va be in soorat cluster bandi mishavand ke
    C.S har center ba baghie element ha hesab mishavad
    va C.S har element k ba centeri ke bsihtr bood dar dasteye oon center gharar migirad

    va inkar inghadr edame peyda mikonad ta listaye jadidemun ba list haye ghabli yeki shavad (list == cluster)


'''

arr = rows_readFile("dataset.csv")
arr_csv = strTofloat(arr)
a1, a2 = kmeans(arr_csv)

'''
    inja dar vaghe miad mige ke onsore aval ro 0 dar nazar begire
    va baghie element haee ke dar in daste hastand ro 0 dar nazar migirm
'''
if(arr_csv[0] in a1):
    file = open("result.txt","w")
    for el in arr_csv:
        if(el in a1):
            file.write("0" + "\n")
        else:
            file.write("1\n")
        
else:
    file = open("result.txt", "w")
    for el in arr_csv:
        if(el in a2):
            file.write("0\n")
        else:
            file.write("1\n")

file.write(str(s_cal(a1,a2)))

file.close()



print("s is equal to :" + str(s_cal(a1,a2)))

# ploter(columnedFile("dataset.csv")) # this Line will plot the dataset File

with open('result1.csv', 'w',newline='') as write_file:
    csv_writer = writer( write_file )
    for c in a1:
        csv_writer.writerow(c)

with open('result2.csv', 'w',newline='') as write_file:
    csv_writer = writer( write_file )
    for c in a2:
        csv_writer.writerow(c)

# ploter(columnedFile("result1.csv"))