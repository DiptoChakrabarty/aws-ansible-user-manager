import boto3
import botocore
import paramiko
from dotenv import load_dotenv
load_dotenv()

path=os.getenv("PATH")
key = paramiko.RSAKey.from_private_key_file(path)
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect/ssh to an instance
try:
    # Provide username and   public IP of EC2
    instance_ip = input("Add the instance Ip address : ")
    username = input("What is the username : ")
    client.connect(hostname=instance_ip, username=username, pkey=key)

    # Execute a command(cmd) after connecting/ssh to an instance
    cmd = input("Enter your command : ")
    stdin, stdout, stderr = client.exec_command(cmd)
    print(stdout.read())

    # close the client connection once the job is done
    client.close()
    

except Exception as e:
    print(e)