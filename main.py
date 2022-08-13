from foundry.services.multipass.multipass import Multipass


multipass = Multipass("/Users/anjor/.py-foundry.json")

print(multipass.get_me())