import csv
import operator
import sys

class Event:
	def __init__(self, filename):
		with open(filename, 'rb') as csvfile:
			event = csv.reader(csvfile)
			self.data = [row for row in event]

	def myKey(self, elem):
		return elem[0]

	def deviceChannelPaths(self):
		device_id = {}
		for elem in self.data:
			if elem[1] in device_id:
				device_id[elem[1]].append((elem[0], elem[3]))
			else:
				device_id[elem[1]] = [(elem[0], elem[3])]

		output = []
		for elem in device_id:
			device_id[elem] = sorted(device_id[elem], key=self.myKey)
			device_id[elem] = ', '.join([row[1] for row in device_id[elem]])
			output.append('%s: ' % elem + device_id[elem])

		output_string = ''
		output = sorted(output)
		for elem in output:
			output_string += elem + '\n'
		return output_string.rstrip('\n')

	def deviceId(self):
		device_id = {}
		for elem in self.data:
			if elem[2] in device_id:
				device_id[elem[2]].append((elem[0], elem[1], elem[3]))
			else:
				device_id[elem[2]] = [(elem[0], elem[1], elem[3])]
		return device_id

	def commonPaths(self):
		device_id = self.deviceId()
		for elem in device_id:
			device_id[elem] = sorted(device_id[elem], key=self.myKey)
			new_dict = {}
			for item in device_id[elem]:
				if item[1] in new_dict:
					new_dict[item[1]].append(item[2])
				else:
					new_dict[item[1]] = [item[2]]
			device_id[elem] = new_dict

		answer_dict = {}
		for elem in device_id:
			if elem:
				for key in device_id[elem]:
					path = ', '.join([row for row in device_id[elem][key]])
					if path in answer_dict:
						answer_dict[path] += 1
					else:
						answer_dict[path] = 1
		
		sorted_dict = sorted(answer_dict.items(), key=operator.itemgetter(1), reverse=True)
		output_string = ''
		for item in sorted_dict[:20]:
			output_string += '%s: ' % item[1] + item[0] + '\n'
		return output_string.rstrip('\n')

	def userChannelPaths(self):
		user_channel_paths = self.deviceId()

		empty_user_dict = {}
		if '' in user_channel_paths:
			for elem in user_channel_paths['']:
				if elem[1] in empty_user_dict:
					empty_user_dict[elem[1]].append(elem)
				else:
					empty_user_dict[elem[1]] = [elem]
				
		output = []
		for key in user_channel_paths:
			if key:
				key_dict = {}
				for user_device_id in user_channel_paths[key]:
					if user_device_id[1] not in key_dict:
						key_dict[user_device_id[1]] = True
				for keys in key_dict:
					if keys in empty_user_dict:
						user_channel_paths[key].extend(empty_user_dict[keys])
				user_channel_paths[key] = sorted(user_channel_paths[key], key=self.myKey)
				output.append('%s: ' % key + ', '.join([row[2] for row in user_channel_paths[key]]))
		output_string = ''
		output = sorted(output)
		for elem in output:
			output_string += elem + '\n'
		return output_string.rstrip('\n')

def main():
	myEvent = Event(sys.argv[1])
	#print myEvent.deviceChannelPaths()
	#print myEvent.commonPaths()
	print myEvent.userChannelPaths()

if __name__ == '__main__':
	main()
