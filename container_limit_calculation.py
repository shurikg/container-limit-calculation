import argparse

def scale_iteration_calculation(min, max, iteration_num):
    scale = []
    step = (max-min)/iteration_num
    for index in range(iteration_num+1):
        scale.append(min + index*step)
    
    return scale

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-mic', '--min_cpu', action="store", dest="min_cpu", default=0.1, type=float)
parser.add_argument('-mac', '--max_cpu', action="store", dest="max_cpu", default=2, type=float)
parser.add_argument('-mim', '--mim_memory', action="store", dest="min_memory", default=0.1, type=float)
parser.add_argument('-mam', '--max_memory', action="store", dest="max_memory", default=2, type=float)
parser.add_argument('-sic', '--scale_iteration_cpu', action="store", dest="cpu_iteration", default=5, type=int)
parser.add_argument('-sim', '--scale_iteration_memory', action="store", dest="memory_iteration", default=5, type=int)

args = parser.parse_args()
print( args)
cpu_iteration = scale_iteration_calculation(args.min_cpu, args.max_cpu, args.cpu_iteration)
mem_iteration = scale_iteration_calculation(args.min_memory, args.max_memory, args.memory_iteration)

for current_cpu in cpu_iteration:
    for current_memory in mem_iteration:
        print ("Running with {} cpu and {} mem".format(current_cpu, current_memory))

print(scale_iteration_calculation(args.min_cpu, args.max_cpu, args.cpu_iteration))
