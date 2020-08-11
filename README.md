# aws-user-adder

- Add Users in your ec2 server using  public keys and ip address 
- Also add your keys to the instance

### How to configure

```sh

- Activate virtual env using source  venv/bin/activate
- Add your pem file path in ansible.cfg -> private_key_file
- ssh-add <pem file>
- In hosts file add in this format { instance ip address}  ansible_ssh_user={ user to connect}  ansible_ssh_private_key_file= { pvt key path }
- For ubuntu user will be ubuntu and centos user is ec2-user
- Add your users key to add in instance in ssh directory
- Name the key as  {username}.pub
- Add all users under the vars users 

```

### Running the script 

```sh

- To launch new instance
  ansible-playbook  --vault-password-file=".password" -i ./hosts ec2_launch.yml

- To manage users
  ansible-playbook ec2_users.yml

```