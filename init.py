import os
import shutil

# # # # # # #
# function()
# # # # # # #

def mkdir(path):
 
	folder = os.path.exists(path)
 
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
	
		print("---"+path+ ": OK  ---")
 
	else:
		print("---  There is this folder!  ---")






# # # # # # #
# code()
# # # # # # #

# 1.创建文件夹
build= os.getcwd()+"/build"
src= os.getcwd()+"/src"
test=os.getcwd()+"/test"
extern=os.getcwd()+"/extern"
print(build)
mkdir(build)    
mkdir(src)
mkdir(test)
mkdir(extern)

# 2.创建主函数
main=src+"/main.cc"
if os.path.exists(main):
  print("There is main.cc")
else:
  f = open(main, 'w')
  f.write("#include <iostream>\n\n")
  f.write("int main(int agrc,char** agrv)\n")
  f.write("{\n\n")
  f.write("    std::cout<<\"Hello World!\"<<std::endl;\n")
  f.write("    return 0;\n")
  f.write("}\n")
  f.close()
  print("Create main.cc")

# 3.创建CMakeLists.txt
cmake=os.getcwd()+"/CMakeLists.txt"
if os.path.exists(cmake):
  print("There is CMakeLists.txt")
else:
    #  copy CMakeLists.txt
    source_file = os.getcwd()+'/cmake/txt/MainConfig.cmake'
    target_file = os.getcwd()+'/CMakeLists.txt'
    shutil.copyfile(source_file, target_file)
    print("Create CMakeLists.txt")

src_cmake=src+"/CMakeLists.txt"
if os.path.exists(src_cmake):
  print("There is src/CMakeLists.txt")
else:
    #  copy CMakeLists.txt
    source_file = os.getcwd()+'/cmake/txt/SrcConfig.cmake'
    target_file = os.getcwd()+'/src/CMakeLists.txt'
    shutil.copyfile(source_file, target_file)
    print("Create src/CMakeLists.txt")
    







