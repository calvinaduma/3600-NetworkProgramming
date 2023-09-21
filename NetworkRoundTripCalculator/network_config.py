# TODO: Define a variable named 'config' that contains a dictionary with the entries
#       'packet_length', 'num_links', 'bandwidths', 'distances', 'transmission_speeds', 'processing_delays', and 'average_packet_arrival_rate'
#       These variables will contain all of the information we need to compute a packets round trip latency through a network.
#       'packet_length' should store the length of the packet in bytes
#       'num_links' should store the number of links the packet will pass through
#       the remaining entries should store lists of length 'num_links', where each entry in the list corresponds with the value associated with that link

config = { 'packet_length' : 46428.513311494215,'num_links' : 3,'bandwidths': [774276662, 702822540, 91575029],'distances' : [808859, 176733, 65478],'transmission_speeds' : [285102627, 199861213, 285102627],'processing_delays' : [0.00345, 0.00171, 0.00189],'average_packet_arrival_rates' : [4293, 5683, 743] }
#config['packet_length'] = 64000.0
#config['num_links'] = 4.0
#config['bandwidths'] = [100.0,300.0,500.0,700.0]
#config['distances'] = [1250.0,500.0,750.0,1000.0]
#config['transmission_speeds'] = [300000000.0,500000000.0,700000000.0,900000000.0]
#config['processing_delays'] = [0.000001,0.000005,0.000002,0.000003]
#config['average_packet_arrival_rates'] = [2.0,3.0,4.0,5.0]
# print(config.keys())
