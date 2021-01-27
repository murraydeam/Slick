import rpyc
import datetime

AD_SERVER_IP = '172.21.96.33'
# AD_SERVER_IP = '172.16.100.81'
AD_BOT_PORT = 19961
DOMAIN_CONTROLLER = 'DC=pyad01,DC=local'
users_ou = 'OU=All,OU=Employee,{}'.format(DOMAIN_CONTROLLER)
groups_ou = 'OU=Employee_Groups,{}'.format(DOMAIN_CONTROLLER)


def send_command(command):
    if not command:
        return
    try:
        connection = rpyc.connect(AD_SERVER_IP, AD_BOT_PORT)
        connection.root.run_command(command)
    except Exception as Err:
        print('Error in send command: ', str(Err))
        print('Check Server IP and Port...')


def create_user(username, employee_id, display_name, active=False):
    """
    Create New user in AD
    :param username:
    :param employee_id:
    :param display_name:
    :param active:
    :return:
    """
    if active:
        disabled = 'no'
    else:
        disabled = 'yes'

    description = "User added by AD BOT on  {}".format(datetime.datetime.now())
    default_password = 'DefaultP@55w0rD'

    dn = '"CN={},{}"'.format(username, users_ou)
    groups = '"cn=All,{}" ' \
             '"cn=USB_Deny,{}" '.format(groups_ou,
                                        groups_ou)
    command = 'dsadd user ' \
              '{} ' \
              '-samid "{}" ' \
              '-upn "{}" ' \
              '-display "{}" ' \
              '-empid "{}" ' \
              '-desc "{}" ' \
              '-disabled {} ' \
              '-pwd {} ' \
              '-pwdneverexpires yes ' \
              '-mustchpwd yes ' \
              '-memberof {} ' \
              '-acctexpires never ' \
              ''.format(
                dn,
                username,
                username,
                display_name,
                employee_id,
                description,
                disabled,
                default_password,
                groups,
                )
    send_command(command)


# Manage existing user account


def manage_user(username, mode):
    """
    This function can manage active directory users
    :param username:
    :param mode:
    :return:
    """
    dn = 'CN={},{}'.format(username, users_ou)
    cmd = ''
    if mode == 'disable':
        cmd = 'dsmod user {} -disabled yes'.format(dn)
    elif mode == 'enable':
        cmd = 'dsmod user {} -disabled no'.format(dn)
    elif mode == 'delete':
        cmd = 'dsrm -noprompt "cn={},{}"'.format(username, users_ou)
    send_command(cmd)


# Change user password


def pword_change(username, new_password):
    """
    This function can change active directory password
    :param new_password:
    :param username:
    :return:
    """
    new_pword = input("Enter a general password for this user..\n"
                      "If you would like to use the default Password leave blank and hit enter... ")
    if new_pword is None:
        dn = 'CN={},{}'.format(username, users_ou)
        cmd = 'dsmod user {} -pwd {}'.format(dn, new_password)
        send_command(cmd)
    else:
        dn = 'CN={},{}'.format(username, users_ou)
        cmd = 'dsmod user {} -pwd {}'.format(dn, new_password)
        send_command(cmd)


# Change AD group


def ad_group(group_name, mode):
    """
    Add and Remove Group
    :param group_name:
    :param mode:
    :return:
    """
    cmd = ''
    if mode == 'add':
        group_description = 'Group created by AD Bot'
        cmd = 'dsadd group "cn={}, {}"' \
              ' -desc "{}"'.format(group_name, groups_ou, group_description)
    elif mode == 'remove':
        cmd = 'dsrm -noprompt "cn={},{}"'.format(group_name, groups_ou)
    send_command(cmd)


# Change AD user to a new Group


def group_user(group_name, mode, username):
    """
    Add and Remove User from groups
    :param group_name:
    :param mode:
    :param username:
    :return:
    """
    dn = 'CN={},{}'.format(username, users_ou)
    cmd = ''
    if mode == 'add':
        cmd = 'dsmod group "cn={},{}"' \
              ' -addmbr "{}"'.format(group_name, groups_ou, dn)
    elif mode == 'remove':
        cmd = 'dsmod group "cn={},{}"' \
              ' -rmmbr "{}"'.format(group_name, groups_ou, dn)
    send_command(cmd)


def user_info(username):
    """
    Show the provieded users Account info
    (Password expiration, Full Name, Last Logon, Local/Global Group Memberships)
    :param username:
    :reutrn:
    """
    dn = 'CN={}'.format(username)
    cmd = 'net user ' \
          '{} ' \
          ''.format(
            username
            )

    # Continue writing this function...

    pass


# The line below is for testing only

create_user("dmurray", "123456", "Deandre Murray")
