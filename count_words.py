# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 20:26:47 2017

@author: Gin
"""

"""问题
用 Python 实现函数 count_words()，该函数输入字符串 s 和数字 n，返回 s 中 n 个出现频率最高的单词。返回值是一个元组列表，包含出现次数最高的 n 个单词及其次数,即 [(<单词1>, <次数1>), (<单词2>, <次数2>), ... ]，按出现次数降序排列。
您可以假设所有输入都是小写形式，并且不含标点符号或其他字符（只包含字母和单个空格）。如果出现次数相同，则按字母顺序排列。
例如：
print count_words("betty bought a bit of butter but the butter was bitter",3)
输出：
[('butter', 2), ('a', 1), ('betty', 1)]
"""
def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    top_n = {}
    # TODO: Count the number of occurences of each word in s
    for word in s.split():
        if word not in top_n:
            top_n[word] = 0
        top_n[word]+=1
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    top_n=sorted(top_n.iteritems(), key=lambda d:(-d[1],d[0])) 
    #top_n=sorted(top_n)
    # TODO: Return the top n words as a list of tuples (<word>, <count>)

    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()