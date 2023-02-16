from ldap3 import Server, Connection, ALL
import credential_ldap as cl


controlador_dominio = 'AD aqui'

server_ldap = Server(controlador_dominio, get_info=ALL)
conn_ldap = Connection(server_ldap, cl.user_ldap, cl.pass_ldap, auto_bind=True)

conn_ldap.search('dc=ADICIONAR CONFORME AQUI,dc=local', '(&(objectclass=user)(!(objectclass=computer)))', attributes=['sAMAccountName','memberOf'])

gps_discard_ldap = ('CN=USB_Liberado', 'CN=USB_Bloqueado', 'CN=CD_Bloqueado', 'CN=CD_Liberado')
