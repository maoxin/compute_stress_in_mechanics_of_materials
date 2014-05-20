# compute the main stress and computed stress
from pprint import pprint

def compute_main_stress(sig_x, sig_y, sig_z, tau_xy):
    sig_1 = float(sig_x + sig_y) / 2 + \
            0.5 * ((sig_x - sig_y) ** 2 + 4 * tau_xy ** 2) ** 0.5
            
    sig_2 = float(sig_x + sig_y) / 2 - \
            0.5 * ((sig_x - sig_y) ** 2 + 4 * tau_xy ** 2) ** 0.5
            
    sig_3 = sig_z
    
    sig_list = [sig_1, sig_2, sig_3]
    new_list = sorted(sig_list, reverse=True)
    
    return new_list
    
def compute_3rd_4th_stress(sig_1, sig_2, sig_3):
    third = sig_1 - sig_3
    forth = (0.5 * ((sig_1 - sig_2)**2 + (sig_1 - sig_3)**2 + \
            (sig_2 - sig_3)**2)) **0.5
    
    return [third, forth]

def compute_without_exact_process(sig_x, sig_y, sig_z, tau_xy):
    # compute main stress
    sig_1, sig_2, sig_3 = compute_main_stress(sig_x, sig_y, sig_z, tau_xy)
    
    # compute computed stress 
    third, forth = compute_3rd_4th_stress(sig_1, sig_2, sig_3)
    
    stress = {
        'sigma': {
            'sig_1': sig_1,
            'sig_2': sig_2,
            'sig_3': sig_3,
        },
        'computed_sigma': {
            'third': third,
            'forth': forth,
        }
    }
    
    return stress

def compute_with_list(inputs, func):
    lst = []
    for ipt in inputs:
        lst.append(func(*ipt))
        
    return lst

if __name__ == '__main__':
    
    # a home work data.
    sig_inputs = [
        [40, 40, 0, 60],
        [60, -80, 0, -40],
        [-40, 50, 0, 0],
        [0, 0, 0, 45],
    ]

    stress_group = compute_with_list(sig_inputs, compute_without_exact_process)
    pprint(stress_group)


