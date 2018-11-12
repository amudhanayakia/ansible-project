#!/usr/bin/env python
import json
import csv
import argparse


def get_inventory_data():
	f = open( 'hosts.csv', 'r' )

	reader = csv.DictReader( f, fieldnames = ("hostvars","ansible_host",
		"ansible_user","ansible_ssh_private_key_file","ansible_sudo"))
	store = []
	hosts = []
	for row in reader:
	    frame = {row["hostvars"]:{
	    "ansible_host":row["ansible_host"],
	    "ansible_ssh_private_key_file": row["ansible_ssh_private_key_file"],
	    "ansible_sudo": row["ansible_sudo"],
	    "ansible_user": row["ansible_user"]
	    } }
	    store.append(frame)
	    hosts.append(row["hostvars"])

        fh = open('./list.txt', 'w')
        outt = json.dumps(hosts)
        fh.write(outt)
        f.close()
      
	# Save the JSON
	f = open( './data.json', 'w')
	out = json.dumps(store, indent=4)
	f.write(out)

	tf = open( './temp1.txt', 'w' )

	with open("./data.json") as f:
	  for line in f:
	   if (":") in line:
	      tf.write(line)
	   elif ("}") and (",") in line:
	      tf.write(line)

	tf.close()

	tf1 = open( './temp2.txt', 'w' )
	line_num = 1
	with open("./temp1.txt") as f:
	  for line in f:
	    if ("hostvars") in line:
	        tf1.write(line)
                line_num += 1               
	    elif line_num >1 and line_num <7 :
               line_num +=1              
            elif line_num >=7:
                 tf1.write(line)
	     

	tf1.write("}")

	tf1.close()


	tf2 = open( 'inv.txt', 'w' )


#	tf2.write("[")
	tf2.write("{")
	tf2.write("\"_meta\" : {")


        with open("./temp2.txt") as f:
          for line in f:
            tf2.write(line)
        
        

	tf2.write("}")
        tf2.write("},")
        
        
        tf2.write("\"all\": {")
        tf2.write("\"children\": [],")
        tf2.write("\"hosts\":")

        tf2.write(outt)

        tf2.write(",")
        tf2.write("\"vars\": {}}")



        tf2.write("}")

#        tf2.write("]")
	tf2.close()
        f.close()


def read_cli_args():
                global args
                parser = argparse.ArgumentParser()
                parser.add_argument('--list', action='store_true')
                parser.add_argument('--host', action='store')
                args = parser.parse_args()


#Default main function
if __name__ == "__main__":
        global args
        read_cli_args()
 #       inventory_data = get_inventory_data()
        get_inventory_data()
        str = open('inv.txt', 'r').read()
        inventory_data = json.loads(str)
        if args and args.list:
                print(json.dumps(inventory_data)) 



