import numpy as np
from amarium import make_full_filename, delete_file



from particular.monte_carlo.monte_carlo_init import init_lj

def test_lj(): 
    delete_file("Simulations/MCInit/LJ_pos_128.npy")
    
    number_particles = 128
    epsilon = 0.25
    sigma = 0.25 
    box_len = 8
    file_name = f"LJ_pos_{number_particles}"
    
    dir_name = "Simulations/MCInit"
    ref_name = make_full_filename(prefix = dir_name, file_name = file_name) + ".npy"
    init_lj(sigma = sigma, 
            epsilon = epsilon, 
            number_particles = number_particles, 
            box_len = box_len, 
            file_name = file_name, 
            dir_name = dir_name)

    data = np.load("Simulations/MCInit/LJ_pos_128.npy")
    assert len(data) == number_particles, str(data.shape)