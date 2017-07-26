# coding: utf-8

# import os
import sys
import subprocess
import json
# import time


# todo : install azure package automatically
def az_vm():
    pass

# todo : az vm -h
def az_vm_h():
    pass

# todo : store log to db
def db():
    pass


# Get OS version in order to determine encoding
def get_os_info():

    os = sys.platform

    if 'win' in os:
        encoding = 'big5'
    else:
        encoding = 'utf-8'

    result = (os, encoding)

    return result


# Execute OS command
def exec_command(cmd):

    s = subprocess.check_output(cmd, shell=True)
    result = json.loads(s.decode(get_os_info()[1]))

    return result


# Azure login function
def azure_login():

    cmd_login = 'az login -u {} -p {}'.format(az_account, az_password)

    result = exec_command(cmd_login)
    if result[0].get('state') == 'Enabled':
        return True
    else:
        return False


# Azure server status
def get_status():

    cmd_get_status = 'az vm get-instance-view -g {} -n {}'.format(resource_group, vm_name)

    result = exec_command(cmd_get_status)
    status = result.get('instanceView').get('statuses')[1].get('displayStatus')

    print(status)


def azure_changeIP():
    cmd_deallocate = 'az vm deallocate -g {} -n {}'.format(resource_group, vm_name)
    cmd_start = 'az vm start -g {} -n {}'.format(resource_group, vm_name)

    # if login successfully, execute "deallocate" command to
    # release resource, and execute "start" to change IP address
    if azure_login():
        result = exec_command(cmd_deallocate)
        if result.get('status') == 'Succeeded':
            result = exec_command(cmd_start)
            if result.get('status') == 'Succeeded':
                print('reboot succeeded !')
            else:
                print('reboot failed !')
        else:
            print('deallocate failed !')
    else:
        print('login failed !')


if __name__ == '__main__':

    # Azure account & password
    az_account = 'xxxxxxx@payeasy.com.tw'
    az_password = 'xxxxxxx'

    # Azure resource group & vm name
    resource_group = 'Payeasy_Docker_Services'
    vm_name = 'Docker-Services'

    azure_changeIP()
    # get_status()

