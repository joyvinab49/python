import sys
script, encoding, error = sys.argv
# http://c.biancheng.net/view/4305.html


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    # str.strip(rm)删除头尾的字符序列
    # 若rm为空 则默认删除空白符 包括\n \r \t ' '
    # 只要字符串开头结尾存在rm就会删除 跟顺序无关
    # 如：123abc321.strip(12) 结果是：3abc3
    next_lang = line.strip()
    # 编码过程 str → bytes(字节类型)
    # 语法格式：str.encode([encoding="utf-8"][,errors="strict"])
    # encoding='utf-8'指定进行编码时采用的字符编码 默认是utf-8
    # 若只有encoding一个参数 可以直接写编码格式 如："utf-8"
    # errors="strict"指定遇到错误处理方式 默认为strict
    # encode()对原字符串进行编码 不会直接修改原字符串
    raw_bytes = next_lang.encode(encoding, errors=errors)  # 将str转成bytes类型
    # 解码过程 bytes → str
    # 语法格式：bytes.decode([encoding="utf-8"][,errors="strict"])
    # encoding='utf-8' 指定解码时采用的字符编码 默认是utf-8
    # 对bytes类型数据解码 要选择和当初编码时一样的格式 否则报错
    # errors = "strict" 指定遇到错误处理方式 默认为strict
    # 编码解码的errors="xmlcharrefreplace" 意为使用 xml 的字符引用
    cooked_string = raw_bytes.decode(encoding, errors=errors)  # 将bytes转成str类型

    print(raw_bytes, "<==>", cooked_string)


language = open("23 languages.txt", encoding="utf-8")

main(language, encoding, error)
