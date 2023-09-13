
activities_time = {
    "westminster": 0.5,
    "theatre": 0.5,
    "gallery": 1,
    "museum": 2,
    "sobor": 0.5,
}
activities_grade = {
    "westminster": 7,
    "theatre": 6,
    "gallery": 9,
    "museum": 9,
    "sobor": 8,
}


data = {}
data[0.5] = {
    "westminster": None,
    "theatre": None,
    "gallery": None,
    "museum": None,
    "sobor": None,
}
data[1] = {
    "westminster": None,
    "theatre": None,
    "gallery": None,
    "museum": None,
    "sobor": None,
}
data[1.5] = {
    "westminster": None,
    "theatre": None,
    "gallery": None,
    "museum": None,
    "sobor": None,
}
data[2] = {
    "westminster": None,
    "theatre": None,
    "gallery": None,
    "museum": None,
    "sobor": None,
}


data_selected_activities = {}
for case in data:
    data_selected_activities[case] = {
        "westminster": [],
        "theatre": [],
        "gallery": [],
        "museum": [],
        "sobor": [],
    }

previous_cases = []

for case in data:
    previous_max_act = None
    max_act_names = []
    previous_act = None

    for activity in data[case]:
        if not previous_max_act:
            if activities_time[activity] <= case:
                data[case][activity] = activities_grade[activity]
            else:
                data[case][activity] = 0
            
            max_act_names = [activity]
            data_selected_activities[case][activity] =  max_act_names.copy()
            previous_max_act = activity

        else:
            # check time
            if activities_time[activity] <= case:

                available_time = case - activities_time[activity]

                if available_time > 0:
                    
                    for prev_case in previous_cases[::-1]:
                        prev_case_grade = data[prev_case][previous_act]
                        
                        prev_case_activities = data_selected_activities[prev_case][previous_act]
                        prev_case_time = 0
                        
                        if prev_case_activities:
                            for prev_case_act in prev_case_activities:
                                prev_case_time += activities_time[prev_case_act]

                            if prev_case_time <= available_time:
                                break
                    
                    prev_activity_time = 0
                    for act_name in max_act_names:
                        prev_activity_time += activities_time[act_name]

                    if previous_cases: # try to add activities from previous case
                        if prev_activity_time <= available_time: # prev activity and prev case fits in time
                            
                            if prev_case_grade + activities_grade[activity] > data[case][previous_max_act]: # stack prev case w current act
                                data[case][activity] = prev_case_grade + activities_grade[activity]

                                prev_case_activities_copy = prev_case_activities.copy()
                                prev_case_activities_copy.extend([activity])


                                max_act_names = prev_case_activities_copy
                                data_selected_activities[case][activity] = max_act_names.copy()
                                previous_max_act = activity

                                prev_case_activities = prev_case_activities_copy.copy()


                            else: # stack prev act w current
                                data[case][activity] = activities_grade[previous_max_act] + activities_grade[activity]
                                max_act_names = max_act_names.extend(activity)
                                data_selected_activities[case][activity] =  max_act_names.copy()
                                
                                previous_max_act = activity


                        else: # if prev activity doesnt fit # stack prev case w current act
                            data[case][activity] = prev_case_grade + activities_grade[activity]
                            
                            prev_case_activities_copy = prev_case_activities.copy()
                            prev_case_activities_copy.extend([activity])
                            max_act_names = prev_case_activities_copy


                            data_selected_activities[case][activity] = max_act_names.copy()
                            previous_max_act = activity
                            prev_case_activities = prev_case_activities_copy.copy()


                    else: # if not prev cases
                        if prev_activity_time <= available_time: # can fit prev activity # stack prev act w current
                            data[case][activity] = activities_grade[previous_max_act] + activities_grade[activity]
                            max_act_names = max_act_names.extend(activity)
                            data_selected_activities[case][activity] =  max_act_names.copy()
                            
                            previous_max_act = activity

                        
                        else: # cant fit prev -> find max
                            if activities_grade[activity] > data[case][previous_max_act]: # curr act is max
                                data[case][activity] = activities_grade[activity]

                                max_act_names = [activity]
                                data_selected_activities[case][activity] = max_act_names.copy()
                                previous_max_act = activity

                            else: # prev act is max
                                data[case][activity] = data[case][previous_max_act]

                                data_selected_activities[case][activity] = max_act_names.copy()
                                previous_max_act = activity
                        
                            
                    
                else: # no avail time -> find max
                    if activities_grade[activity] > data[case][previous_max_act]:
                        data[case][activity] = activities_grade[activity]
                        
                        max_act_names = [activity]
                        
                        data_selected_activities[case][activity] =  max_act_names.copy()

                        previous_max_act = activity

                    else:
                        data[case][activity] = data[case][previous_max_act]
                        data_selected_activities[case][activity] =  max_act_names.copy()

                previous_max_act = activity

            else: # curr activity doesnt fit in time -> use prev activity
                data[case][activity] = data[case][previous_max_act]
                data_selected_activities[case][activity] =  max_act_names.copy()

        previous_act = activity

    previous_cases.append(case)
        


print(data)
print('\n\n',data_selected_activities)

