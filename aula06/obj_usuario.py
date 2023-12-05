import os
os.system ("clear")


from classe_usuario import Usuario

admin = Usuario ("Admin","P@$$w0rd","Administrador")
admin.login ("admin","P@$$w0rd")
admin.alterar_senha ("admin","808")
admin.login ("admin","808")