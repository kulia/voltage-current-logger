from sys import argv

def main():
	filename = str(argv[1]) + '.txt'
	# filename = 'test.txt' # For debugging
	path_raw = 'raw-data/'
	path_processed = 'processed-data/'

	f_processed = open(path_processed + filename, 'w')
	f_raw = open(path_raw + filename, 'r')

	data = []

	num_of_samples = 0;
	num_of_discard = 0;
	total_time_diff = 0;
	max_time_diff = 0;
	min_time_diff = 1000000000000;

	t = 0;
	t_prev = 0;
	t_init = 0;

	start = True
	first = True

	i = 0
	for line in f_raw:
		i += 1
		data = str(line).split(' ')

		num_of_samples += 1
		t_prev = t
		
		if len(data) == 3:
			data[2] = data[2].replace('\r', '')
			data[2] = data[2].replace('\n', '')
			data[0] = str(abs(int(data[0])))

			if not '' in data and all(x.isdigit() for x in data):
				data = [ int(x) for x in data]

				t = data[0]

				temp = str(long(data[0] + long(argv[1])))
				temp += '\t'
				temp += str(data[1])
				temp += '\t'
				temp += str(data[2])
				temp += '\n'

				f_processed.write(temp)

				if first:
					t_init = t
					first = False

				if not start:
					t_diff = t-t_prev
					if t_diff < 1: 
						print 'Was the clock reset at line', i, '?'
					else:
						if max_time_diff < t_diff: 
							max_time_diff = t_diff
							print 'New max diff time:', t, t_prev, t_diff, max_time_diff, i
						elif min_time_diff > t_diff: 
							min_time_diff = t_diff
							print 'New min diff time:', t, t_prev, t_diff, min_time_diff, i
						
				else:
					start = False
			else:
				num_of_discard += 1
		else:
			num_of_discard += 1

	total_time_diff = t - t_init

	print 'Total time:', total_time_diff, ' us', t, t_init

	print 'Number of samples:', num_of_samples
	print 'Samples discarded:', num_of_discard
	print 'Avarage Fs:', 1000000 * (num_of_samples-num_of_discard)/total_time_diff, 'Hz'
	
	if min_time_diff > 0: print 'Max Fs:', 1000000 / min_time_diff
	
	print 'Min Fs:', 1000000 / max_time_diff
	print 'T_max:', max_time_diff, ' us'
	print 'T_min:', min_time_diff, ' us'

if __name__ == '__main__':
	main()