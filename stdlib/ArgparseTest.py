import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("echo")
# parser.add_argument("ec", help="echo the string you use here")
# args = parser.parse_args()
# print(args.echo)
# print(args)

# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number", type=int)
# args = parser.parse_args()
# print(args.square**2)


# parser = argparse.ArgumentParser()
# parser.add_argument("--verbosity", help="increase output verbosity")
# args = parser.parse_args()
# if args.verbosity:
#     print("verbosity turned on")
#
# parser.add_argument("-v", "--verbosity", help="increase output verbosity")
# args = parser.parse_args()

parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")


# 如果你觉得这些功能还不满足你日常使用的话argparse还能支持可选参数，如: choices=[0, 1, 2] 让参数只能在 0 1 2 中选择一个
# default=0 参数默认值是0
# 等等 这些就是argparse 模块经常用到的功能了，如果希望继续丰富自己的参数，可以参考官方文档
