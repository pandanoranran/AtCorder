n, k = map(int, input().split())
a = n % k
b = k - a
print(min(a, b))

"""   
example
n = 11 k = 3とおく
1回目 |11 - 3| = 8
2回目 |8 - 3| = 5
3回目 |5 - 3| = 2
となりこれはn%k =11%3 =2と同じことになる。
最後にk - n%kの操作を行うと最小の値が導かれる。
これとn%kが最小になる場合があるので比較して小さくなる方を出力する
"""
