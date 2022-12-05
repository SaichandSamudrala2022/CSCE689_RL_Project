import os
import argparse
import time

def parse_arguments():
    parser = argparse.ArgumentParser('Benchmark Generator Parser')
    #parser.add_argument('--benchNumber',type=int,\
    #    dest='benchmarkNumber',default=20)
    #parser.add_argument('--gridSize',type=int,dest='gridSize',default=16)
    #parser.add_argument('--netNum',type=int,dest='netNum',default=5)
    #parser.add_argument('--capacity',type=int,dest='cap',default=4)
    #parser.add_argument('--maxPinNum',type=int,dest='maxPinNum',default=5)
    #parser.add_argument('--reducedCapNum',type=int,dest='reducedCapNum',default=1)
    parser.add_argument('--RL_algo',type=str,dest='RL_algo',default='PPO')

    return parser.parse_args()


if __name__ == '__main__':
	# Remember to copy results to other directory when running new parameters
	#start_time = time.time()
	filename = None
	args = parse_arguments()
	#benNum = args.benchmarkNumber
	#gridSize = args.gridSize; netNum = args.netNum
	#cap = args.cap; maxPinNum = args.maxPinNum
	#reducedCapNum = args.reducedCapNum
	RL_algo = args.RL_algo  
  
	'''  # Vasudev 12/2
	# Generating problems module (A*)
	# Make sure previous benchmark files: "benchmark","capacityplot",
	# and 'solution' are removed
	os.system('rm -r ./benchmark')
	os.system('rm -r ./capacityplot_A*')
	os.system('rm -r ./solutionsA*')
	os.system('rm -r ./solutionsDRL')
	os.chdir('BenchmarkGenerator')
	# os.chdir('..')
	print('**************')
	print('Problem Generating Module')
	print('**************')
	os.system('python BenchmarkGenerator.py --benchNumber {benNum} --gridSize {gridSize}\
	 --netNum {netNum} --capacity {cap} --maxPinNum {maxPinNum} --reducedCapNum {reducedCapNum}'\
	 .format(benNum=benNum,gridSize=gridSize,\
	 	netNum=netNum,cap=cap,maxPinNum=maxPinNum,reducedCapNum=reducedCapNum))

	# Solve problems with DRL 
	os.chdir('..') # Go back to main folder
	'''
	if not os.path.exists('solutionsDRL'):
		os.makedirs('solutionsDRL')
	reduced_path = 'benchmark_reduced'
	if not os.path.exists(reduced_path):
		os.makedirs(reduced_path)

	list = os.listdir('benchmark_reduced')
	benchmarkNum = len(list)
  
	for i in range(benchmarkNum):
		os.system('taskset -c ' +str(i) + ' python -u Router.py ' + str(RL_algo) + " " + str(i) +" | tee ./logs/"+RL_algo+"_benchmark_"+ str(i+1)+" &")
    # If the experiment is to be run on a machine with less than 10 cores, comment the previous line and uncomment the below line
		#os.system('python -u Router.py ' + str(RL_algo) + " " + str(i) +" | tee ./logs/"+RL_algo+"_benchmark_"+ str(i+1)+" &")
  	