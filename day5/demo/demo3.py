# encoding: UTF-8

# 设计一个函数返回给定文件名的后缀名

def get_suffix(filename, has_dot = False):
	
  # 获取文件名的后缀名

  # :param filename: 文件名
  # :param has_dot: 返回的后缀名是否需要带点
  # :return: 文件的后缀名
  
  pos = filename.rfind('.')
  if 0 < pos < len(filename) - 1:
  	index = pos
  	if has_dot:
  		index = pos - 1
  	return filename[index:]
  else:
  	return ''


if __name__ == '__main__':
	get_suffix('test.py')
	