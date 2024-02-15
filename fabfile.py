from fabric import Connection
result = Connection('e5c10126da09.3a2627c1.alu-cod.online',user="e5c10126da09", connect_kwargs={"password":"8b59ac3374695df3691a"}).run("whoami")
msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
print(msg.format(result))
