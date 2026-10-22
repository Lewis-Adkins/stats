import numpy as np

signal = np.array([0,-1,0,1])

np.set_printoptions(precision=2, suppress=True)
def get_a0(signal:np.array)-> float:
    return signal.mean(axis = 0)

def get_fq(signal: np.array)-> dict[str,any]:

    N = signal.shape[0]

    if N % 2 == 0:   
        q_even = int(N / 2)
        f_i_even = np.arange(1, q_even+1) / N

        return {"q": q_even, "f_i":f_i_even}
    else:
        q_odd  = int((N-1) / 2)
        f_i_odd  = np.arange(1,q_odd+1) / N

        return {"q": q_odd, "f_i":f_i_odd}

def mult_f_t(vec1: np.array, vec2: np.array)->np.array:

    return np.repeat(vec1.reshape(1,-1), repeats= len(vec2), axis = 0).T * vec2 

def get_ai(signal: np.array)-> float:
    N = signal.shape[0] 
    fq = get_fq(signal)

    t= np.arange(0, N)

    f_i_times_t = mult_f_t(fq['f_i'], t)

    cos_term = np.cos(2 * np.pi * f_i_times_t) 


    a_i = (2 / N) *(signal*cos_term).sum(axis = 1)

    return a_i

def get_bi(signal: np.array)-> float:
    N = signal.shape[0] 
    fq = get_fq(signal)

    t= np.arange(0, N)

    f_i_times_t = mult_f_t(fq['f_i'], t)

    sin_term = np.sin(2 * np.pi * f_i_times_t) 

    b_i = (2 / N) *(signal*sin_term).sum(axis = 1)

    return b_i    

def part_1(signal: np.array)-> tuple[float]:
    a0 = get_a0(signal)
    ai = get_ai(signal)
    bi = get_bi(signal)
    print(fr"a0: {a0:.4f} " "\n" fr"ai: {ai}" "\n" fr"bi: {bi}") # my bi is switched from your test case but i think its still correct

def dft(signal: np.array, use_numpy:bool = False)-> tuple[np.array]: #part_2
    if not use_numpy:
        a0 = get_a0(signal)
        ai = get_ai(signal)

        bi = get_bi(signal)
        return a0, ai, bi
    else:
        return np.fft.fft(signal)






def main():
    part_1(signal)
    print(dft(signal, True))
main()