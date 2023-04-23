- Role install dedcon server on debian i386 and Centos 7
- Dockerfile contains dockerized environment for run play-book on Centos 7

## Command to run

 1) docker build -t ansible-test:1 .
 2) docker run --rm -v $(pwd):/work ansible-test:1 ansible-playbook /work/deploy.yml
 
## Note
 
 You have to create playbook deploy.yml whith following content before run docker container: 
    
 ---------------------
    - hosts: localhost
      roles:
        - ansible-role-dedcon