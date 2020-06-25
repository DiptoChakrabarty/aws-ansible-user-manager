import boto3,os,argparse
import botocore
import paramiko
from dotenv import load_dotenv
load_dotenv()

#path=os.getenv("PATH")
path=""
key_name=""
parser = argparse.ArgumentParser()
parser.add_argument("--ip")
parser.add_argument("--username")
parser.add_argument("useradd")


print(path)
key = paramiko.RSAKey.from_private_key_file(path)
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect/ssh to an instance
try:
    # Provide username and   public IP of EC2
    instance_ip = args.ip
    username = args.username
    client.connect(hostname=instance_ip, username=username, pkey=key)

    # Execute a command(cmd) after connecting/ssh to an instance
    user = args.useradd
    cmd = "sudo useradd " + user
    print(cmd)
    stdin, stdout, stderr = client.exec_command(cmd)
    print(stdout.read())

    #transfer file
    transfer = "scp  -i {} {}  {}@{}:/home/{}/".format(path,path,path,username,ip,username)
    stdin, stdout, stderr = client.exec_command(trasfer)
    print(stdout.read())

    #add to authorized keys
    add = "cat {} >>  /home/{}/.ssh/authorized_keys".format(keyname,username)
    stdin, stdout, stderr = client.exec_command(add)
    print(stdout.read())


    # close the client connection once the job is done
    client.close()
    

except Exception as e:
    print(e)