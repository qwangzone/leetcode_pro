# batch_file_rename.py
# Created: 6th August 2012

'''
This will batch rename a group of files in a given directory,
once you pass the current and new extensions
'''
#just checking
__author__ = 'Craig Richards'
__version__ = '1.0'

import os
import argparse

def batch_rename(work_dir, old_ext, new_ext):
    '''
    This will batch rename a group of files in a given directory,
    once you pass the current and new extensions
    '''
    # files = os.listdir(work_dir)
    '''批量更换目标目录的文件后缀'''
    for filename in os.listdir(work_dir): #文件目录列表
        # Get the file extension
        split_file = os.path.splitext(filename)  #获取单个目录的路径和文件后缀的列表，如果只有文件夹，则后缀为空
        file_ext = split_file[1] #获取文件目录中的后缀，若目录中无这类文件，则为空
        # Start of the logic to check the file extensions, if old_ext = file_ext
        if old_ext == file_ext: #若旧的后缀名存在
            # Returns changed name of the file with new extention
            newfile = split_file[0] + new_ext #把新的后缀名更新到旧的

            # Write the files
            #更新目录名
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )
'''提示运行时必须要输入的参数与参数类型'''
def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1, help='the directory where to change extension')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
    return parser

def main():
    '''
    This will be called if the script is directly invoked.
    '''
    # adding command line argument
    parser = get_parser()
    #获取输入的目录名字典
    args = vars(parser.parse_args())
    # Set the variable work_dir with the first argument passed
    #获取目录
    work_dir = args['work_dir'][0]
    print(work_dir)
    # Set the variable old_ext with the second argument passed
    old_ext = args['old_ext'][0]

    if old_ext[0] != '.':
        old_ext = '.' + old_ext
    # Set the variable new_ext with the third argument passed
    new_ext = args['new_ext'][0]

    if new_ext[0] != '.':
        new_ext = '.' + new_ext
    batch_rename(work_dir, old_ext, new_ext)


if __name__ == '__main__':
    main()
