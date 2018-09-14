# pyKeyring

A simple and secure tool to store passwords

## Introdution 

pyKeyring is a tool to store encrypted passwords in a simple database file. 

## Usage

pyKeyring is much simple to use.

### Create a database
```console
foo@bar:~$ keyring -f /path/to/keyring.db create
```
The default database file is named keyring.db. If you don't use the -f argument, pyKeyring will use this name. 

### Insert a password
```console
foo@bar:~$ keyring add password_label
```
The password_label is used to label your password :)

### Get a password
```console
foo@bar:~$ keyring get password_label
```

If you don't want to print the password in the terminal you can use the argument -c to copy the password to clipboard.

```console
foo@bar:~$ keyring get -c password_label
```

### Update a password
```console
foo@bar:~$ keyring update password_label
```

### Remove a password
```console
foo@bar:~$ keyring remove password_label
```