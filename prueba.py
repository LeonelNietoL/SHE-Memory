import sys
from dataclasses import dataclass

# @dataclass
# class NombreCompleto:
#     nombre            : str
#     apellidoPaterno   : str
#     apellidoMaterno   : str

# full_name = NombreCompleto(sys.argv[1], sys.argv[2], sys.argv[3])
# print(full_name.nombre)
# print(full_name.apellidoPaterno)
# print(full_name.apellidoMaterno)



@dataclass
class GetMemoryUpdateInfo:
    UID            : str
    KEY_NEW        : str
    KEY_AuthID     : str
    ID             : int
    AuthID         : int
    C_ID           : int
    F_ID           : int
    PROTOCOL       : str

get_memory_update_info = GetMemoryUpdateInfo(UID=sys.argv[1], KEY_NEW=sys.argv[2], KEY_AuthID=sys.argv[3], 
                                             ID=int(sys.argv[4], 16), AuthID=int(sys.argv[5], 16), C_ID=int(sys.argv[6], 16),
                                             F_ID=int(sys.argv[7], 16), PROTOCOL=sys.argv[8])

print(bytes.fromhex(get_memory_update_info.UID))
print(bytes.fromhex(get_memory_update_info.KEY_NEW))
print(bytes.fromhex(get_memory_update_info.KEY_AuthID))
print(type(get_memory_update_info.ID))
print(get_memory_update_info.AuthID)
print(get_memory_update_info.C_ID)
print(get_memory_update_info.F_ID)