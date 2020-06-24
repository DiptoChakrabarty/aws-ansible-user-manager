import boto3
import botocore
import paramiko

key = paramiko.RSAKey.from_private_key_file()
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect/ssh to an instance
try:
    # Here 'ubuntu' is user name and 'instance_ip' is public IP of EC2
    client.connect(hostname=instance_ip, username="ubuntu", pkey=key)

    # Execute a command(cmd) after connecting/ssh to an instance
    stdin, stdout, stderr = client.exec_command(cmd)
    print stdout.read()

    # close the client connection once the job is done
    client.close()
    break

except Exception, e:
    print e