all_radios = {}

all_radios["k_one"] = ["id", "nv", "ut"]
all_radios["k_two"] = ["wa", "id", "mt"]
all_radios["k_three"] = ["or", "nv", "ca"]
all_radios["k_four"] = ["nv", "ut"]
all_radios["k_five"] = ["ca", "az"]


all_states = set()

for radio in all_radios:
    for state in all_radios[radio]:
        all_states.add(state)


covered = set()
used_radios = []


max_radio_cover = len(all_states.difference(covered).difference(set(all_radios[list(all_radios.keys())[0]])))
max_radio_name = list(all_radios.keys())[0]

while not (covered == all_states) and all_radios:
    for radio in all_radios:
        curr_diff = len(all_states.difference(covered).difference(set(all_radios[radio])))
        if curr_diff < max_radio_cover:
            max_radio_cover = curr_diff
            max_radio_name = radio

    for state in all_radios[max_radio_name]:
        covered.add(state)
    
    used_radios.append(max_radio_name)

    all_radios.pop(max_radio_name)

    max_radio_cover = len(all_states.difference(covered).difference(set(all_radios[list(all_radios.keys())[0]])))
    max_radio_name = list(all_radios.keys())[0]




print(used_radios)
print(covered)
